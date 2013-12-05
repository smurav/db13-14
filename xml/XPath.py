#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import libxml2
import optparse
import datetime
import math

from xml.dom.minidom import *

def open(xml_file):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//osm//relation[@id='2784645']//tag")
	for student in students:
		print("K: " + student.prop('k') + " V: " + student.prop('v'))
	print("=======================================================")
	students = ctxt.xpathEval("//way[@id='41601758']//nd")
	X = []
	Y = []
	Per = 0
	for student in students:
		points = ctxt.xpathEval("//node[@id=" + student.prop('ref') + "]")
		for point in points :
			r_major = 6378137.000
			r_minor = 6356752.3142
			x = r_major*math.radians(float(point.prop('lon')))
			y = r_major*math.radians(float(point.prop('lat')))
			X.append(x)
			Y.append(y)
			print(str(x) + " " + str(y))
			
	for i in range(len(X) - 1):
		Per += math.sqrt(math.pow(X[i]-X[i+1], 2) + math.pow(Y[i]-Y[i+1], 2) )
	print(str(Per))
			
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
	department = ctxt.xpathEval("//group[@number="+group+"]/..")
	year1 = year[0].prop('entry_year')
	for let in letter:
		for yea in year:
			for dep in department:
				print(let.prop('letter') + year1+ "-" + dep.prop('number') + yea.prop('number'))
	ctxt.xpathFreeContext()
	doc.freeDoc()

def task8(xml_file):
	doc = libxml2.parseFile(xml_file)
	ctxt = doc.xpathNewContext()
	faculties = ctxt.xpathEval("//faculty")
	count = []
    
	for faculty in faculties:
		ctxt.setContextNode(faculty)
		count += [len(ctxt.xpathEval("sector/department/group/student"))]

	max_index = count.index(max(count))
	min_index = count.index(min(count))

	ctxt.setContextNode(faculties[max_index])
	print "Max: " + ctxt.xpathEval("@name")[0].content
	ctxt.setContextNode(faculties[min_index])
	print "Min: " + ctxt.xpathEval("@name")[0].content

	ctxt.xpathFreeContext()

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

	open(arguments[0])
	
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
