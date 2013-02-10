#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep

while True:
   if os.path.exists(fname):
      print "ERROR: '%s' already exists" % fname
   else:
      break

#get file contet (text) lines
all = []

print "\nEnter Lines('.' by itself to quit).\n"

while True:
   entry = raw_input('> ')
   if entry == '.':
      break
   else:
      all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'
