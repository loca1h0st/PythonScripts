#! /usr/bin/env python

def isprime(num):
 prime = primelist()
 #primetest(prime)
 
 for indx in range(len(prime)):
  if str(num) == prime[indx]:
    return True
    break;
  else:
    return False
 '''if num in prime: return True
 else: return False'''
  
def primelist():
  f = open('/home/loca1h0st/Documents/pythonScript/PRIMES1T.TXT', 'r')
  #numbers2 = f.read()
  numbers = []
  for line in f:
   numbers.append(line.split())
  return numbers
  
def primetest(lists):
  #lists = primelist()
  for indx in range(len(lists)/600):
    print lists[indx]

if __name__ == '__main__':
 print isprime(raw_input('> '))
# primetest()
# primelist()
# print isprime(9)
# print isprime(2)
# print isprime(1)
# print isprime(12)
# print isprime(3)
# print isprime(5)

