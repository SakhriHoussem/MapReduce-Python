#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
current_word = list()
key = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, word = line.split('\t', 1)

    if current_key == key:
        current_word.append(word)  #ajoute le mot dans la list de meme cle
    else:
        if current_key:

             # write result to STDOUT
            print '%s\t%s' % (current_key, current_word)
            del current_word[:]
        current_key = key  # passe a la cle suivant
        current_word.append(word) # ajoute la la list la valeur de la cle suivant
    # do not forget to output the last word if needed!
if current_key == key:
    print '%s\t%s' % (current_key, current_word)

