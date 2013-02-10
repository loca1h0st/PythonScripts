#! /usr/bin/env python

import string

def time_convertor(string1):
   list1 = string1.split(':')
   
   x = int(list1[1]) * 60
   y = int(list1[0]) * 3600

   return int(string1[3]) + x + y

def main():
  print 'Enter time(hr:min:sec): ',
  enter = raw_input()
  
  conversion = time_convertor(enter)

  print conversion,
  print 'seconds'

if __name__ == '__main__':
   main()
