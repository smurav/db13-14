#!/usr/bin/python
#-*- coding: UTF-8 -*-
import libxml2

def ParseXML(xmlFile):
	xmlDoc = OpenXML(xmlFile)
  	

	xmlDoc.freeDoc()

def walkTree(xmlNode):
	child = xmlNode.children
	while child is not None:
		if not child.isBlankNode():
			if child.type == "element":
				childCount = int(child.xpathEval('count(*)'))
				depth = int(child.xpathEval('count(ancestor::*)')) - 1
				if childCount == 0:
					# If the count of child elements is 0 then we
					# have a node only containing text
					print  depth * '\t' + child.name + ' : ' + child.content
				else:
					# If the node contains other child elements then
					# we can recurse down the tree
					print depth * '\t' + child.name
					walkTree(child)
		child = child.next

def PrintXML(xmlDoc):
	xmlRoot = xmlDoc.gerRootElement()
	walkTree(root)


def AddNodeNextSubling(nameNode, nameSubl, namePar):
	newNode = libxml2.newNode(nameNode)
	#namePar.AddChild(newNode)
	nameSubl.AddNextSibling(newNode)
	#newNode.setContent('Hello')

def AddNodePrevSubling(nameNode, nameSubl, namePar):
	newNode = libxml2.newNode(nameNode)
	#namePar.AddChild(newNode)
	nameSubl.AddPrevSibling(newNode)

def SetContentToNode(content, nameNode, namePar):
	newNode.setContent(content)

def DeleteContentInNode(content, nameNode, namePar):
	newNode.setContent("")


def DeleteNode(nameNode, namePar):

def AddAttribute(nameAttr, nameNode):
	doc = libxml2.parseFile("foo.xml")
	nodes=doc.xpathEval('/archive/article[2]')
	newNode = nodes[0].newChild(None, 'counter', None)
	newNode.newProp('count', '1')
	print nodes[0].serialize()

def DeleteAttribute(nameAttr, nameNode):	

def AddContent(Content, nameNode, namePar):
	nameNode.addContent(Content)

def DelContent(Content, nameNode, namePar):
	


def OpenXML(xmlFile):
	xmlDoc = libxml2.parseFile(xmlFile)
	return xmlDoc
	

	



"""
child = root.children
	# the children property returns the FIRST child of a node
	while child is not None:
		if child.type == "element":
			# do something with the child node
			print child.name
		child = child.next

	import libxml2
	doc = libxml2.parseDoc('<foo att1="value 1" att2="value 2"/>')
	root = doc.getRootElement()
	for property in root.properties:
		if property.type=='attribute':
			# do something with the attributes
			print property.name
			print property.content
	doc.freeDoc()
"""





def main():
  op = optparse.OptionParser(description = U"{Жопа жопа жопа жопа}",
                             prog="university.py",
                             version="0.1",
                             usage="%prog xml_file [dtd_file]")
  options, arguments = op.parse_args()
  arguments_count = len(arguments)
  if arguments_count == 1:
        ParseXML(arguments[0])
  else:
    op.print_help()
    
if __name__ == '__main__':
  main()