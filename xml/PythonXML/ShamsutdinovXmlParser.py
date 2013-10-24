#!/usr/bin/python
#-*- coding: UTF-8 -*-

import libxml2
import optparse

from xml.dom.minidom import *

def print_xml(xml_file):
	
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
	  print "{0}: {1}".format(children.name, children.properties )
    
  doc.freeDoc()
  
def add_node(xml_file, name, tag_name, attribute_name, attribute_value, value) :
	
	doc = parse(xml_file)
	nodes = doc.getElementsByTagName(name)
	for node in nodes:
		newNode = doc.createElement(tag_name)
		if attribute_name != "" :
			newNode.setAttribute(attribute_name, attribute_value)
		if value != "" :
			text = doc.createTextNode(value)
			newNode.appendChild(text)
		node.appendChild(newNode)
	
	print ""
	print doc.toxml()
	print ""
	
def delete_node(xml_file, name) :
	
	xmldoc = parse(xml_file)
	doc_root = xmldoc.documentElement
	nodes = xmldoc.getElementsByTagName(name)
	
	for node in nodes:
		parent = node.parentNode
		parent.removeChild(node)

	nodeList = xmldoc.childNodes
	print ""
	for node in nodeList:
		print node.toxml()
	print ""

def main():
  op = optparse.OptionParser(description = U"Парсер Xml",
                             prog="ShamsutdinovXmlParser.py",
                             version="0.1",
                             usage="%prog xml_file")
  options, arguments = op.parse_args()
  arguments_count = len(arguments)
  
  
  if arguments_count == 1:
    print_xml(arguments[0])
  
  elif arguments_count == 2:
    delete_node(arguments[0], arguments[1])

  elif arguments_count == 6:
    add_node(arguments[0], arguments[1], arguments[2], 
    arguments[3], arguments[4], arguments[5])
  else:
    print "Arguments:\nto add: file_name, toWhere, tag_name, att_name, att_val, val\nto delete: file_name, tag_name"
    
if __name__ == '__main__':
  main()


	
	
