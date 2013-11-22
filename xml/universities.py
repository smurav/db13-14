#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import libxml2
import optparse
import gettext
import sys, locale
def open(xml_file):
  """Открытие xml файла"""
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext()
  
  #students = ctxt.xpathEval("//student[../@entry_year<2011]")
  students = ctxt.xpathEval("//student")
  for student in students:
    print student.prop('name');
  doc.freeDoc()
  ctxt.xpathFreeContext()
  
def validate_xsd(xml_file, xsd_file):
  """Проверка xml файла на соответствие XML схеме"""
  doc = libxml2.parseFile(xml_file)
  ctxt = libxml2.schemaNewParserCtxt(xsd_file)
  schema = ctxt.schemaParse()
  del ctxt
  validation_ctxt = schema.schemaNewValidCtxt()
  validation_err = validation_ctxt.schemaValidateDoc(doc)
  del validation_ctxt
  del schema
  del doc
  if validation_err == 0:
    print "Документ " + xml_file + " соответствует " + xsd_file
    open(xml_file)
  else:
    print "Документ " + xml_file + " НЕ соответствует " + xsd_file
  
def validate_dtd(xml_file, dtd_file):
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
                             prog="xml",
                             version="0.1",
                             usage=U"%prog [ключ]... xml_file")

  op.add_option("-d", "--dtd", dest="dtd", help=U"DTD диагарамма", metavar="DTD_FILE")
  op.add_option("-s", "--xsd", dest="xsd", help=U"XML схема", metavar="XSD_FILE")
  op.get_option('--version').help=U"показать версию и выйти"
  op.get_option('--help').help=U"показать помощь и выйти"
                             
  options, arguments = op.parse_args()
  arguments_count = len(arguments)
  if arguments_count != 1:
    op.print_help()
  elif options.dtd:
    validate_dtd(arguments[0], options.dtd)
  elif options.xsd:
    validate_xsd(arguments[0], options.xsd)
  else:
    open(arguments[0])
    
if __name__ == '__main__':
  main(sys.arguments)








  #!/usr/bin/env python
#-*- coding: UTF-8 -*-

import libxml2
import optparse
import gettext
import sys, locale

def open ( xml_file ):
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile( xml_file )
  ctxt = doc.xpathNewContext ()
  students = ctxt.xpathEval("//students")
  for student in students:
    print student.prop('name');
  doc.freeDoc()
  ctxt.xpathFreeContext()

def kaf ( xml_file ):
  print "Открываем документ " + xml_file
  doc = libxml2.parseFile( xml_file )
  ctxt = doc.xpathNewContext ()
  students = ctxt.xpathEval("department")
  #students = ctxt.xpathEval("//group[@entry_year=2011]/student")
  for student in students:
    print student.prop('name');
  doc.freeDoc()
  ctxt.xpathFreeContext()

def main (argv):
  op = optparse.OptionParser(description = U"Пример использования парсера",
        prog="xml",
        version="0.1",
        usage=U"%prog [ключ]... xml_file")
  op.add_option("-1", dest="kaf", help=U"Вывести список кафедр факультета КиБ")
  #op.add_option("-s", "--xsd", dest="xsd", help=U"XML схема", metavar="XSD_FILE")
  op.get_option('--version').help=U"показать версию и выйти"
  op.get_option('--help').help=U"показать помощь и выйти"
  if len(argv) == 2:
    op.print_help()
  elif options.kaf:
    kaf(argv[0], options.dtd)
  elif options.xsd:
    validate_xsd(arguments[0], options.xsd)
  else:
    open(arguments[0])

if __name__ == '__main__':
  main(sys.argv)