#! /usr/bin/env python

import string 

"""its not working 
we need to fix the formula
but the code runs fine, calcuation error"""

def fah_cel(temp):
   return 9/5 * temp + 32.0

"""its not working 
we need to fix the formula
but the script is entripted just fine,
calculation error"""

def cel_fah(temp):
   return (temp - 32.0) * (5/9)


def main():
   print ('Temperature is Fahrenheit or Celsius?(F or C)'),
   option = raw_input()
   degree = int(raw_input('Temperature: '))
   x = 8008
   
   if option.lower() == 'f':
      print fah_cel(degree)

   elif option.lower() == 'c':
      print cel_fah(degree)
   else:
      print 'invalid option; terminating'

if __name__ == '__main__':
   main()
