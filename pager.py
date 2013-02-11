#! /usr/bin/env python

'page.py --file access script, problem 9-4'

import sys
import fileinput

def file_found(filename):
  try:
    file_input = open(filename, 'r')
    return file_input
  except Exception, e:
    print("<p>Error: %s</p>" % str(e))

def p():
  print x

def file_Access():
  filelines = file_found(raw_input('>PATH: '))
  x = 1
  while x < 26: 
    for lines in filelines:
      print lines; x += 1
      if x == 26: 
        if raw_input('>Enter C to continue: ').upper() == 'C':
          x = 1
        else:
          exit(1)

if __name__ == '__main__':
  file_Access()
