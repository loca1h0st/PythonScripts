#! /usr/dev/env python

import math

def facto(num):
  return math.factorial(num)
  
def facto_mo(num):
 holder = 1
 for x in range(1, num+1):
  holder *= x
 return holder



if __name__ == '__main__':
  print facto(5)
  print facto_mo(5)
