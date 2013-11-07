#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import libxml2
import optparse
import datetime

def open(xml_file):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//student")
	print students
	ctxt.xpathFreeContext()
	doc.freeDoc()
	
def departments(xml_file):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//faculty[@name='Кибернетика и Безопасность']//department")
	for student in students:
		print student.prop('name');
	ctxt.xpathFreeContext()
	doc.freeDoc()
		
def students_in_year(xml_file, year):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//group[@entry_year > "+year+"]//student")
	for student in students:
		print student.prop('name');
	ctxt.xpathFreeContext()
	doc.freeDoc()
	
def task3(xml_file, name):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//group[student[@name="+name+"]]")
	for student in students:
		print student.prop('name');
	ctxt.xpathFreeContext()
	doc.freeDoc()

def task4(xml_file, group):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//group[@entry_year="+group+"]//student")
	print len(students)
	ctxt.xpathFreeContext()
	doc.freeDoc()
	
def task5(xml_file, department):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	print department
	students = ctxt.xpathEval("//department[@name="+department+"]//group//student")
	print len(students)
	ctxt.xpathFreeContext()
	doc.freeDoc()

def task6(xml_file):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//department[@number='36']/../..")
	for student in students:
		print student.prop('name');
	ctxt.xpathFreeContext()
	doc.freeDoc()
	
def task7(xml_file, group):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	now = datetime.datetime.now()
	letter = ctxt.xpathEval("//group[@number="+group+"]/../..")
	year = ctxt.xpathEval("//group[@number="+group+"]")
	year1 = now.year - year[0].prop('entry_year')
	print(letter.prop('letter') + year1+"-"+year.prop('number'))
	ctxt.xpathFreeContext()
	doc.freeDoc()


def main(argv):
	op = optparse.OptionParser(description = U"Пример использования парсера",
                             prog="xml",
                             version="0.1",
                             usage=U"%prog [ключ]... xml_file")
	op.add_option("-y", "--year", dest="year", help=U"год поступления", metavar="Entry_Year")
	op.add_option("-n", "--name", dest="name", help=U"фамилия студента", metavar="Student_Name")
	op.add_option("-g", "--group", dest="group", help=U"Група", metavar="Group")
	op.add_option("-d", "--department", dest="department", help=U"Кафедра", metavar="Department")
	

	options, arguments = op.parse_args()
	arguments_count = len(arguments)

	task6(arguments[0])
	
	if options.year:
		students_in_year(arguments[0], options.year)
	elif options.name:
		task3(arguments[0], options.name)
	elif options.group:
		task7(arguments[0], options.group)
	elif options.department:
		task5(arguments[0], options.department)

if __name__ == '__main__':
	main(sys.argv)	
