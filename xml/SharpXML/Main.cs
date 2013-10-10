using System;
using System.Text.RegularExpressions;
using System.Text;
using System.Collections.Generic;
using System.IO;

namespace XMLparser {
	class MainClass {
		class Element {
			public String Tag {
				get; set;
			}
			
			public Dictionary<String, String> Attributes = null;
			public String Data = null;
			
			public List<Element> Branches;
			
			public Element() {
				Branches = new List<Element>();
				Attributes = new Dictionary<string, string>();
			}

			public Element(string tag, string data = null) {
				Tag = tag;
				Data = data;
			}

			public Element(Element element) {
				Branches = new List<Element>(element.Branches);
				Attributes = new Dictionary<string, string>(element.Attributes);
				Data = new string(element.Data.ToCharArray());
				Tag = new string(element.Tag.ToCharArray());
			}
		}
		
		private static List<Element> GetCollection(Element node, Func<Element, bool> condition) {
			List<Element> collection = new List<Element>();
			
			Action<Element> traverse = (X) => {
				if(condition(X))
					collection.Add(X);
				for(int i = 0; i < X.Branches.Count; i++)
				traverse(X.Branches[i]);
			};
			traverse(node);
			
			return collection;
		}
		
		private static void FormatDocument(Element node, int depth = 0) {
			for(int i = 0; i < depth; i++)
				Console.Write("  ");
			Console.Write("<{0}", node.Tag);
			if(node.Attributes.Count > 0) {
				foreach(KeyValuePair<string, string> kvp in node.Attributes) {
					Console.Write(" {0}=\"{1}\"", kvp.Key, kvp.Value);
				}
			}
			Console.Write(">");
			
			if(node.Branches.Count == 0) {
				Console.Write(node.Data);
				Console.Write("</{0}>\n", node.Tag);
			} else {
				Console.WriteLine();
				foreach(Element elem in node.Branches)
					FormatDocument(elem, depth + 1);
				
				for(int i = 0; i < depth; i++)
					Console.Write("  ");
				Console.Write("</{0}>\n", node.Tag);
			}
		}
		
		private static void Parse(StreamReader reader) {
			Regex regex_tag_start = new Regex(@"<\s*(?<tag>\w+)\s*(?<attr>[^>/]*?)>");
			Regex regex_tag_single = new Regex(@"<\s*(?<tag>\w+)\s*(?<attr>[^>]*?)\s*/\s*>");
			Regex regex_tag_end = new Regex(@"<\s*/(?<tag>\w+)\s*>");
			Regex regex_attr = new Regex("(?<name>\\w+)\\s*=\\s*\"(?<val>[^\"]*)\"");
			Regex regex_attr_splitter = new Regex("(?<==\"[^\"]*\")");
			Regex regex_comment_start = new Regex(@"<!--");
			Regex regex_comment_end = new Regex(@"-->");
			
			
			Stack<Element> tagStack = new Stack<Element>();
			int lastOpenTagPos = 0;
			
			
			Queue<string> tagQueue = new Queue<string>();
			StringBuilder string_buffer = new StringBuilder();
			Match current_match = null;
			string input = null;
			string[] tag_array = null;
			while(!reader.EndOfStream) {
				input = reader.ReadLine();
				
				tag_array = Regex.Split(input, @"(?=<)");
				foreach(string s in tag_array)
					tagQueue.Enqueue(s);
				
				while(tagQueue.Count > 0) {
					string_buffer.Append(tagQueue.Dequeue());
					
					//Console.WriteLine("BUFFER:     *" + string_buffer.ToString() + "*");
					
					// COMMENT START
					if ((current_match = regex_comment_start.Match(string_buffer.ToString())).Success) {
						//Console.WriteLine("comment_start");
						
						Element tempElem = new Element();
						
						tempElem.Tag = "<!--";
						tagStack.Push(tempElem);
						string_buffer.Remove(current_match.Groups[0].Index, current_match.Groups[0].Length);
						lastOpenTagPos = current_match.Groups[0].Index;
					}
					
					
					// COMMENT END
					if ((current_match = regex_comment_end.Match(string_buffer.ToString())).Success) {
						//Console.WriteLine("comment end");
						
						tagStack.Pop();
						string_buffer.Remove(lastOpenTagPos, current_match.Groups[0].Index + current_match.Groups[0].Length - lastOpenTagPos);
					}
					
					
					// COMMENT CONDITION
					if(tagStack.Count > 0 && tagStack.Peek().Tag.Equals("<!--"))
						continue;
					
					
					// OPENING TAG
					if ((current_match = regex_tag_start.Match(string_buffer.ToString())).Success &&
					    !regex_tag_end.IsMatch(current_match.Groups[0].Value)) {
						//Console.WriteLine("tag_start");
						
						Element tempElem = new Element();
						
						if(tagStack.Count > 0)
							tagStack.Peek().Branches.Add(tempElem);
						
						tempElem.Tag = current_match.Groups["tag"].Value;
						string[] tag_attr = regex_attr_splitter.Split(current_match.Groups["attr"].Value);
						//Console.WriteLine("ATTR = *" + current_match.Groups["attr"].Value + "*");			// ATTR
						foreach(string attr in tag_attr) {
							if(Regex.IsMatch(attr, @"^\s*$"))
								continue;
							tempElem.Attributes.Add(
								regex_attr.Match(attr).Groups["name"].Value,
								regex_attr.Match(attr).Groups["val"].Value
								);
						}
						
						tagStack.Push(tempElem);
						string_buffer.Remove(current_match.Groups[0].Index, current_match.Groups[0].Length);
						lastOpenTagPos = current_match.Groups[0].Index;
					}
					
					
					// CLOSING TAG
					if ((current_match = regex_tag_end.Match(string_buffer.ToString())).Success) {
						//Console.WriteLine("tag_end");
						
						if(tagStack.Peek().Branches.Count == 0) {
							tagStack.Peek().Data = string_buffer.ToString(
								lastOpenTagPos, 
								current_match.Groups[0].Index - lastOpenTagPos
								);
							string_buffer.Remove(lastOpenTagPos, current_match.Groups[0].Index + current_match.Groups[0].Length - lastOpenTagPos);
						} else
							string_buffer.Remove(current_match.Groups[0].Index, current_match.Groups[0].Length);
						
						if(tagStack.Count > 1)
							tagStack.Pop();
						else {
							//foreach(Element e in GetCollection(tagStack.Peek(), (A) => A.Tag.Equals("root")))
							//	Console.WriteLine("<{0}> branches: {1}", e.Tag, e.Branches.Count);
							
							Console.WriteLine("\n*** DOM ***\n");
							FormatDocument(tagStack.Pop());
							Console.WriteLine();
						}
					}
					
					
					// SINGLE TAG
					if ((current_match = regex_tag_single.Match(string_buffer.ToString())).Success) {
						//Console.WriteLine("tag_single");
						
						Element tempElem = new Element();
						tagStack.Peek().Branches.Add(tempElem);
						
						tempElem.Tag = current_match.Groups["tag"].Value;
						string[] tag_attr = regex_attr_splitter.Split(current_match.Groups["attr"].Value);
						//Console.WriteLine("ATTR = *" + current_match.Groups["attr"].Value + "*");			// ATTR
						foreach(string attr in tag_attr) {
							if(Regex.IsMatch(attr, @"^\s*$"))
								continue;
							tempElem.Attributes.Add(
								regex_attr.Match(attr).Groups["name"].Value,
								regex_attr.Match(attr).Groups["val"].Value
								);
						}
						
						string_buffer.Remove(current_match.Groups[0].Index, current_match.Groups[0].Length);
					}
				}
			}
		}

		private static void InsertElement (Element node, Element root) {
			root.Branches.Add(node);
		}

		private static void InsertElement(Element node, Element root, Func<Element, bool> condition, bool onlyFirst = true) {
			List<Element> elements = GetCollection(root, condition);

			for(int i = 0; i < ((onlyFirst) ? 1 : elements.Count); i++)
				elements.Add(new Element(node));
		}
		
		public static void Main (string[] args) {
			try {
				StreamReader reader = new StreamReader (new FileStream (@"test.xml", FileMode.Open));
				Parse (reader);
				reader.Close();
			} catch (IOException e) {
				Console.WriteLine("Can't open file");
			}
		}
	}
}