#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import libxslt
import libxml2
import optparse

def transform(xml_file, xsl_file, out_file):
  """ xslt трансформация xml-документа"""
  print "Открываем документ " + xml_file
  xml_doc = libxml2.parseFile(xml_file)
  xsl_doc = libxml2.parseFile(xsl_file)
  xsl = libxslt.parseStylesheetDoc(xsl_doc)
  out_doc = xsl.applyStylesheet(xml_doc, None)
  print out_doc
  xsl.saveResultToFilename(out_file, out_doc, 0)
  xsl.freeStylesheet()
  out_doc.freeDoc()
  xml_doc.freeDoc()

def main():
  op = optparse.OptionParser(description = U"Пример использования XSLT преобразований",
                             prog="xslt",
                             version="0.1",
                             usage=U"%prog")

  op.add_option("-i", "--input", dest="xml", help=U"Входной документ", metavar="XML_FILE")
  op.add_option("-o", "--output", dest="out", help=U"Выходной документ", metavar="OUT_FILE")
  op.add_option("-x", "--xsl", dest="xsl", help=U"Преобразование", metavar="XSL_FILE")
                             
  options, arguments = op.parse_args()
  if options.xml and options.xsl and options.out:
    transform(options.xml, options.xsl, options.out)
  else:
    op.print_help()

if __name__ == '__main__':
  main()
