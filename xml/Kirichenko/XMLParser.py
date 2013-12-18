#!/usr/bin/python
#-*- coding: UTF-8 -*-

import optparse

from xml.dom.minidom import *

def print_xml(xml_file):
        
  doc = parse(xml_file)        
  nodeList = doc.childNodes
  print ""
  for node in nodeList:
                print node.toxml()
  print ""

def insert_att(xml_file, name, att_name) :
        doc = parse(xml_file)
        nodes = doc.getElementsByTagName(name)
        for node in nodes:
                node.setAttribute(att_name, "")
        nodeList = doc.childNodes
        print ""
        for node in nodeList:
                print node.toxml()
        print ""
        
        
def update_att(xml_file, name, node_id, att_name, att_val) :
        doc = parse(xml_file)
        nodes = doc.getElementsByTagName(name)
        for node in nodes:
                if node.attributes['name'].value == node_id :
                        node.setAttribute(att_name, att_val)
        nodeList = doc.childNodes
        print ""
        for node in nodeList:
                print node.toxml()
        print ""
  
  
def insert_node(xml_file, name, tag_name, attribute_name, attribute_value, value) :
        
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
    
  elif arguments_count == 3:
        insert_att(arguments[0], arguments[1], arguments[2])
        
  elif arguments_count == 5 :
        update_att(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4] )

        
  elif arguments_count == 6:
    insert_node(arguments[0], arguments[1], arguments[2], 
    arguments[3], arguments[4], arguments[5])
  else:
    print "Arguments:\nto insert: file_name, parent, tag_name, att_name, att_val, val\nto delete: file_name, tag_name"
    print "to insert_att: xml_file, name, att_name"
    print "to update_att: xml_file, name, node_id, att_name, att_val"
if __name__ == '__main__':
  main()
