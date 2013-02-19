#! /usr/bin/env python

#Name: Mahmoud Ibrahim
#UID:  U44784560
#Date: Feb 10, 2013

import sys

def prime_list(num):
  lis = range(2,num+1)
  for i in range(2,8):
      lis = filter(lambda x: x == i or x% i, lis)
  return lis
  
def prime_lists():
  lis = range(2,50)
  for i in range(2,8):
      lis = filter(lambda x: x == i or x% i, lis)
  return lis
    
def main():
  print 'Enter the the Prime number: '
  print prime_list(int(raw_input('> ')))
  
if __name__ == '__main__':
  main()
  #print prime_lists()
  #print prime_list(50)
