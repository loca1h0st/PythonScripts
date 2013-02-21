#! /usr/dev/env python

import math

def facto(num):
  'factorial provided by the math module'
  return math.factorial(num)
  
def facto_mo(num):
 'factorial I wrote to output the result'
 holder = 1
 for x in range(1, num+1):
  holder *= x
 return holder



if __name__ == '__main__':
  print facto(5)
  print facto_mo(5)
