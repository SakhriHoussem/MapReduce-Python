#!/usr/bin/env python

import sys
wordList = dict()
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')


    print '%s\t%s\t%s' % (words[1],words[4],1)# affiche cle valeur
