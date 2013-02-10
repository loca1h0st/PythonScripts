#! /usr/bin/env python

import string 

list_a = []

def sorting(imput):
   list_a = append(imput.split(' '))
   list_a.sort()
   
   
def main():
   imput = raw_input('>Enter list separated by SPACE: ')
   sorting(imput)
   print imput
   
if __name__ == '__main__':
   main()
