#! /usr/bin/env python

def arithmetic(i):
  'take i and determine what arithmetic to preform'
  i = i.split()
  x = int(i[0])
  y = int(i[2])
  
  if i[1] == '-':
     return x - y
  elif i[1] == '+':
     return x + y
  elif i[1] == '*':
     return x * y
  elif i[1] == '/':
     return x / y
  elif i[1] == '%':
     return x % y
  elif i[1] == '**':
     return x ** y

def main():
  'main, does what main do'
   value = raw_input('operation(N1 OP N2): ')
   print arithmetic(value)

if __name__ == '__main__':
   main()
