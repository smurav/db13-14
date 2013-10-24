#!/usr/bin/python
#-*- coding: UTF-8 -*-

import libxml2
import optparse

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
  
def find_node(root, tag, prop, data):
    for children in root.children:
        if children.name == tag and children.prop(prop) == data:
            return children
	#Замена атрибута prop во всех элементах с данным тегом и значением атрибута data
def update_attr(xml_file, tag, prop, data, datanew):
    doc = libxml2.parseFile(xml_file)
    root = doc.children
    for children in root.children:
        if children.name == tag and children.prop(prop) == data:
            print children.name
            children.setProp(prop, datanew)
            print 'Success update'
    doc.saveFile('save.xml')
    doc.freeDoc()
    #Удаление атрибута prop из всех элементов с данным тегом и значением атрибута data 
def delete_attr(xml_file, tag, prop, data):
	doc = libxml2.parseFile(xml_file)
	root = doc.children
	for children in root.children:
		if children.name == tag and children.prop(prop) == data:
			children.unsetProp(prop)
			print 'Success delete'
	doc.saveFile('save.xml')
	doc.freeDoc()
	#Добавление атрибута prop_new ко всем элементам с данным тегом
def add_attr(xml_file, tag, prop_new, data_new):
    doc = libxml2.parseFile(xml_file)
    root = doc.children
    for children in root.children:
        if children.name == tag:
            print children.name
            children.newProp(prop_new, data_new)
            print 'Success add atribute'
    doc.saveFile('save.xml')
    doc.freeDoc()

def elem_notexist(root, tag, prop, data):
	for children in root.children:
		if children.name == tag and children.prop(prop) == data:
			return false
		else:
			return true
			
	#Добавление элемента
def insert(xml_file, tag_add, prop_add, data_add):
	doc = libxml2.parseFile(xml_file)
	root = doc.children
	elem = libxml2.newNode(tag_add)
	root.addChild(elem)
	elem.setProp(prop_add, data_add)
	print "Вставлен новый элемент"
	#else:
	#	print 'Такой элемент уже существует'
	doc.saveFile('save2.xml')
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

def main():
  op = optparse.OptionParser(description = U"Пример использования парсера",
                             prog="university.py",
                             version="0.1",
                             usage="%prog xml_file [dtd_file]")
  options, arguments = op.parse_args()
  arguments_count = len(arguments)
  insert(arguments[0], arguments[1], arguments[2], arguments[3])
  if arguments_count == 1:
	print_xml(arguments[0])
    #open(arguments[0])
  elif arguments_count == 2:
    validate(arguments[0], arguments[1])
  elif arguments_count == 4:
	delete_attr(arguments[0], arguments[1], arguments[2], arguments[3])
	#add_attr(arguments[0], arguments[1], arguments[2], arguments[3])
  elif arguments_count == 5:
    update_attr(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])
  else:
    op.print_help()

if __name__ == '__main__':
  main()

