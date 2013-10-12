#!/usr/bin/python
#-*- coding: UTF-8 -*-

import libxml2
import optparse

def open(xml_file):
  """Открытие xml файла"""
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext()
  
  students = ctxt.xpathEval("//student[../@entry_year<2011]")
  #students = ctxt.xpathEval("//student")
  for student in students:
    print student.prop('name');
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
    open(arguments[0])
  elif arguments_count == 2:
    validate(arguments[0], arguments[1])
  else:
    op.print_help()
    
if __name__ == '__main__':
  main()
