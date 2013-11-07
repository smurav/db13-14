#!/usr/bin/env python

import sys
import libxml2


def task1(doc):
	print "task 1"

	ctxt = doc.xpathNewContext()

	for department in ctxt.xpathEval("//department/@name"):
		print department.content

	ctxt.xpathFreeContext()

def task2(doc, year_val):
	print "task 2"

	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//group[@entry_year > " + str(year_val) + "]/student/@name")

	for student in students:
		print student.content

	ctxt.xpathFreeContext()

def task3(doc, last_name):
	print "task 3"

	ctxt = doc.xpathNewContext()
	print ctxt.xpathEval("//student[starts-with(@name, '" + last_name + "')]/..")

	ctxt.xpathFreeContext()

def task4(doc, year, number, department):
	print "task 4"

	ctxt = doc.xpathNewContext()
	students = ctxt.xpathEval("//department[@number=" + str(department) + "]" +
		"//group[@entry_year=" + str(year) + "and @number=" + str(number) + "]/student")

	print len(students)

	ctxt.xpathFreeContext()

def task5(doc, number):
	print "task 5"

	ctxt = doc.xpathNewContext()
	print len(ctxt.xpathEval("//department[@number=" + str(number) + "]/group/student"))

	ctxt.xpathFreeContext()

def task6(doc, number):
	print "task 6"

	ctxt = doc.xpathNewContext()
	print ctxt.xpathEval("//department[@number=" + str(number) + "]/../@name")[0].content

	ctxt.xpathFreeContext()

def task7(doc, year, number, department):
	print "task 7"

	ctxt = doc.xpathNewContext()

	departments = ctxt.xpathEval("//department[@number=" + str(department) + "]" +
		"//group[@entry_year=" + str(year) + "and @number=" + str(number) + "]")
	ctxt.setContextNode(departments[0])
	path = ""
	for i in range(0, 4):
		ctxt.setContextNode(ctxt.xpathEval("..")[0])
		path = str("'" + ctxt.xpathEval("@name")[0].content + "'" + "/") + path
	path += str(year) + "/" + str(number)

	print path

	ctxt.xpathFreeContext()

def task8(doc):
	print "task 8"

	ctxt = doc.xpathNewContext()

	faculties = ctxt.xpathEval("//faculty")

	amount = []
	for faculty in faculties:
		ctxt.setContextNode(faculty)
		amount += [len(ctxt.xpathEval("sector/department/group/student"))]

	max_index = amount.index(max(amount))
	min_index = amount.index(min(amount))

	ctxt.setContextNode(faculties[max_index])
	print "Max: " + ctxt.xpathEval("@name")[0].content
	ctxt.setContextNode(faculties[min_index])
	print "Min: " + ctxt.xpathEval("@name")[0].content

	ctxt.xpathFreeContext()



def open(xml_file):
	doc = libxml2.parseFile(xml_file)

	task1(doc)
	task2(doc, 2010)
	task3(doc, "Ostroumov")
	task4(doc, 2011, 1, 36)
	task5(doc, 36)
	task6(doc, 36)
	task7(doc, 2011, 1, 3)
	task8(doc)

	doc.freeDoc()

def main(argv):
	if len(argv) != 2:
		sys.stderr.write("Usage : % s xml_file" %(argv[0] ,))
	else:
		open(argv[1])

if __name__ == "__main__":
	main(sys.argv)