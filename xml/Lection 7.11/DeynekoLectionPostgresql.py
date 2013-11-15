#!/usr/bin/env python
#-*- coding: UTF-8 -*-


import sys
import libxml2

def open ( xml_file ):
	doc = libxml2.parseFile( xml_file )
	ctxt = doc.xpathNewContext ()
	students = ctxt.xpathEval( " // student " )
	print students
	print "\n"
	ctxt.xpathFreeContext()
	doc.freeDoc()

def task1 ( xml_file ):
	doc = libxml2.parseFile( xml_file )
	ctxt = doc.xpathNewContext ()
	department = ctxt.xpathEval( " faculty[@name='Кибернетика и Безопасность']/sector/department " )
	print department
	print "\n"
	ctxt.xpathFreeContext()
	doc.freeDoc()

def task2 ( xml_file, year ):
	doc = libxml2.parseFile( xml_file )
	ctxt = doc.xpathNewContext ()
	students = ctxt.xpathEval( " // group[@entry_year>year]/student ")
	print students
	print "\n"
	ctxt.xpathFreeContext()
	doc.freeDoc()

def task3 ():
	asss = 5


def main ( argv ):
	if len(argv) == 3:
		task2 (argv[1], argv[2])

	elif len ( argv ) == 2:
		open ( argv[1])
		task1( argv[1])
	else:
		sys.stderr.write(" Usage : % s xml_file " % (argv[0],))
	
		

if __name__ == '__main__':
	main (sys.argv)
