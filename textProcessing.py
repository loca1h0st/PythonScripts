#! /usr/bin/env python

import sys

def word(sentence):
  lists = sentence.split()
  return len(lists)
  
def vowel(sentence):
  count = 0
  for x in sentence:
    x = x.lower()
    if x.find('a')!=-1 or x.find('e')!=-1 or x.find('i')!=-1\
    or x.find('o')!=-1 or x.find('u')!=-1:
      count = count + 1
  return count

def consonants(sentence):
  lists = sentence.split()
  count = 0
  for words in lists:
    for word in words:
      count = count + 1
  count = count - vowel(sentence)
  return count
      
      
      
if __name__ == '__main__':
  #main()
  print word('this try this for a change')
  print vowel('this try this for a changee')
  print consonants('this try this for a change')
  
  
  
  
