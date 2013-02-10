#! /usr/bin/env python

from locale import currency

def tax(money):
   return money * 0.06

def main():
  money = int(raw_input('>Enter Total: '))
  print '> total after tax:$',
  print tax(money) + money
  
if __name__ == '__main__':
  main()
  
