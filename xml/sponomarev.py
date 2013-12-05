#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import libxml2
import optparse
import gettext
import sys, locale

def kaf(xml_file):
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext()
  students = ctxt.xpathEval("//department[../../@name='Кибернетика и Безопасность']")
  for student in students:
    print student.prop('name');
  doc.freeDoc()
  ctxt.xpathFreeContext()

def year(xml_file, year):
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext()
  students = ctxt.xpathEval("//student[../@entry_year>"+year+"]")
  for student in students:
    print student.prop('name');
  doc.freeDoc()
  ctxt.xpathFreeContext()

def family(xml_file, family):
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext()
  students = ctxt.xpathEval("//group[/student[@name=="+family+"]]")
  for student in students:
    print student.prop('name');
  doc.freeDoc()
  ctxt.xpathFreeContext()

def main():
  op = optparse.OptionParser(description = U"Пример использования парсера",
                             prog="xml",
                             version="0.1",
                             usage=U"%prog [ключ]... xml_file")

  op.add_option("-k", "--kaf", dest="kaf", help=U"Вывести список кафедр факультета КиБ")
  op.add_option("-y", "--year", dest="year", help=U"Вывести перечень студентов, поступивших после указанного года")
  op.add_option("-f", "--family", dest="family", help=U"Вывести список групп, в которых есть студент с заданной фамилией")
  op.get_option('--version').help=U"показать версию и выйти"
  op.get_option('--help').help=U"показать помощь и выйти"
                             
  options, arguments = op.parse_args()

  if options.kaf:
    kaf(options.kaf)
  elif options.year:
  	year(arguments[0], options.year)
  elif options.family:
  	year(arguments[0], options.family)	
  else:
    op.print_help()
    
if __name__ == '__main__':
  main()