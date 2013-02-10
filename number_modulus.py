#! /usr/bin/env python

def even_num():
   num = 0
   for num in range(21):
      if num % 2 == 0:
         print num,
   print'\n'

def odd_num():
   num = 0
   for num in range(21):
       if num % 2 == 1:
          print num,
   print'\n'

def main():
  print 'Even Numbers: '
  even_num()
  print 'Odd Numbers: '
  odd_num()

 # print even_num() % odd_num()
'''Need to figure out the last paret part D 
the if n1 dividsible by n2 part'''


if __name__ == '__main__':
  main()
