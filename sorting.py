#! /usr/bin/env python

import string 

list_a = []#the list that will contain the string

def sorting(imput):
  'this will take a string split it into a list then sort it'
  list_a.append(imput.split())
  return list_a.sort()
   
   
def main():
   'this is main'
   imput = raw_input('>Enter list separated by SPACE: ')
   imput = sorting(imput)
   print imput
   
if __name__ == '__main__':
   main()
