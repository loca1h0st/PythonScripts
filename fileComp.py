#! /usr/bin/env python

'script will compare two text files -- 9-6'

def file_comp(filename1, filename2):
  try:
    filenameA = open(filename1, 'rU')
    filenameB = open(filename2, 'rU')
    
    
    for lineA, lineB in filenameA, filenameB:
      wordA = lineA.split()
      wordB = lineB.split()
      
      for x, y in wordA, wordB:
        if x != y: print wordA.index() + x.index()   
        
  except Exception, e:
    print("<p>Error: %s</p>" % str(e))
    
def main():
  fI = raw_input('> ')
  fII = raw_input('> ')
  file_comp(fI, fII)
if __name__ == '__main__':
  main()
