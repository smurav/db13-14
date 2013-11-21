#!/usr/bin/python
#-*- coding: UTF-8 -*-
import libxml2
import optparse
import gettext
import sys, locale

def departments( xml_file ):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//faculty[@name='Кибернетика и Безопасность']/*/department ")
  for el in departments:
    print el.prop('name')
  ctxt . xpathFreeContext ()
  doc . freeDoc ()

def students_year(xml_file,year):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//group[@entry_year>"+year+"]/student")
  for el in departments:
    print el.prop('name')
  ctxt . xpathFreeContext ()
  doc . freeDoc ()
def student_in_group(xml_file,name):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//group[student[@name='"+name+"']]")
  for el in departments:
    print el.prop('entry_year')
  ctxt . xpathFreeContext ()
  doc . freeDoc ()

def student_count_in_group(xml_file,year):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//group[@entry_year="+year+"]/student")
  count = len(departments)
  print count
  ctxt . xpathFreeContext ()
  doc . freeDoc ()
def student_count_in_department(xml_file,number):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//department[@number="+number+"]/*/student")
  count = len(departments)
  print count
  ctxt . xpathFreeContext ()
  doc . freeDoc ()
def namber_name_department(xml_file,number):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//department[@number="+number+"]")
  for el in departments:
    print el.prop('name')
  ctxt . xpathFreeContext ()
  doc . freeDoc ()
def faculty_name(xml_file,number):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//faculty[sector[department[@number="+number+"]]]")
  for el in departments:
    print el.prop('name')
  ctxt . xpathFreeContext ()
  doc . freeDoc ()
def faculty_min_max(xml_file):
  doc = libxml2 . parseFile ( xml_file )
  ctxt = doc. xpathNewContext ()
  departments = ctxt . xpathEval ("//faculty")
  leng = len(departments)
  i = 0
  j = 0
  while i<leng:
    for el in departments:
        ctxt . xpathEval ("//faculty")
  ctxt . xpathFreeContext ()
  doc . freeDoc ()
def main():
  #departments('mephi.xml')
  #students_year('mephi.xml','2010')
  #tudent_in_group('mephi.xml','Ostroumov')
  #student_count_in_group('mephi.xml','2011')
  #student_count_in_department('mephi.xml','36')
  #faculty_name('mephi.xml','36')
  #namber_name_department('mephi.xml','36')
  faculty_min_max('mephi.xml')
if __name__ == '__main__':
  main()
