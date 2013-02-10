#! /usr/bin/env python

def leapyear(yr):
  if yr % 4 == 0 and yr % 100 != 0:
     return True
  elif yr % 100 == 0 and yr % 400 == 0:
     return False
  else:
     return False
     
  
def main():
  year = int(raw_input('> '))
  print leapyear(year)
  

if __name__ == '__main__':
  main()

