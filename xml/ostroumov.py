#!/usr/bin/python
#-*- coding: UTF-8 -*-

import libxml2
import optparse

def createNewFile(fileName):
  doc= libxml2.newDoc('1.0')
  root = libxml2.newNode('foo')
  doc.setRootElement(root)
  doc.saveFile(fileName)
  doc.freeDoc()

def delete_xml_tag(xml_file,tag_name):
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
      if children.name == tag_name:
        children.unlinkNode()
  doc.saveFile(xml_file)
  #f.close
  doc.freeDoc()

def add_child_to_parent(xml_file,parent,child):
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
      if children.name == parent:
        node = libxml2.newNode(child)
        node.name = child
        children.addChild(node)
  doc.saveFile(xml_file)
  #f.close
  doc.freeDoc()


def add_child_to_parent(xml_file,parent,child,atribute_name,name):
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
      if children.name == parent:
        node = libxml2.newNode(child)
        node.name = child
        node.setProp(atribute_name, name)
        children.addChild(node)
  doc.saveFile(xml_file)
  #f.close
  doc.freeDoc()
def change_atribute(xml_file,node_name,atribute_type,old,new):
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
      if children.name == node_name:
        if children.prop(atribute_type)==old:
          children.unsetProp(atribute_type)
          children.setProp(atribute_type, new)
          #children.addChild(node1)
  doc.saveFile(xml_file)
  #f.close
  doc.freeDoc()
def delete_atribute(xml_file,node_name,atribute_type,old):
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
      if children.name == node_name:
        if children.prop(atribute_type)==old:
          children.unsetProp(atribute_type)
          #children.addChild(node1)
  doc.saveFile(xml_file)
  #f.close
  doc.freeDoc()
def add_atribute(xml_file,node_name,atribute_type,new):
  print "+"
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  for children in root.children:
    if children.type == "element":
      if children.name == node_name:
        print "+"
        children.setProp(atribute_type,new)
        #children.addChild(node1)
  doc.saveFile(xml_file)
  #f.close
  doc.freeDoc()

def print_xml(xml_file):
  doc = libxml2.parseFile(xml_file)
  root = doc.children
  print root.name
  for children in root.children:
    if children.type == "element":
	  print children.name
	  print children.properties
    
  doc.freeDoc()

def open(xml_file):
  """Открытие xml файла"""
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext()
  students = ctxt.xpathEval("//student[../@entry_year<2011]")
  #students = ctxt.xpathEval("//student")
  for student in students:
    print student.prop('name')
  doc.freeDoc()
  ctxt.xpathFreeContext()
  
def validate(xml_file, dtd_file):
  """Проверка xml файла на соответствие dtd"""
  doc = libxml2.parseFile(xml_file)
  dtd = libxml2.parseDTD(None, dtd_file)
  ctxt = libxml2.newValidCtxt()
  res = doc.validateDtd(ctxt, dtd)
  if res == 1:
    print "Документ " + xml_file + " соответствует " + dtd_file
    open(xml_file)
  else:
    print "Документ " + xml_file + " НЕ соответствует " + dtd_file
  doc.freeDoc()
  dtd.freeDtd()
  del ctxt

def main():
  op = optparse.OptionParser(description = U"Пример использования парсера",
                             prog="university.py",
                             version="0.1",
                             usage="%prog xml_file [dtd_file]")
  options, arguments = op.parse_args()
  arguments_count = len(arguments)
  if arguments_count == 1:
	print_xml(arguments[0])
    #open(arguments[0])
  elif arguments_count == 2:
    if(arguments[0]=='new'):
      createNewFile(arguments[1])
    else:
      delete_xml_tag(arguments[0],arguments[1])
  elif arguments_count == 3:
    add_child_to_parent(arguments[0],arguments[1],arguments[2])
  elif arguments_count == 5:
    if arguments[1]=='del':
      delete_atribute(arguments[0],arguments[2],arguments[3],arguments[4])
    elif arguments[1] == 'add':
      add_atribute(arguments[0],arguments[2],arguments[3],arguments[4])
  elif arguments_count == 6:
    if arguments[1]=='atr':
      add_child_to_parent(arguments[0],arguments[2],arguments[3],arguments[4],arguments[5])
    elif arguments[1]=='chatr':
      change_atribute(arguments[0],arguments[2],arguments[3],arguments[4],arguments[5])    
  else:
    op.print_help()
    
if __name__ == '__main__':
  main()
