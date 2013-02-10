#! /usr/bin/env python

import sys
import os

def gradeScale(num):
   letter = ''
   if num in range(90,101):
      letter = 'A'
   elif num in range(80,90):
      letter = 'B'
   elif num in range(70,80):
      letter = 'C'
   elif num in range(60,70):
      letter = 'D'
   elif num in range(60):
      letter = 'F'
   return letter

def main():
   num = int(raw_input('Grade (number value): '))
   print gradeScale(num)

if __name__ == '__main__':
  main()



