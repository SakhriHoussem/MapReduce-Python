#!/usr/bin/env python

from operator import itemgetter
import sys

current_magazin = None
current_prix = 0
magazin = None

wordList = dict()
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    magazin, prix = line.split('\t', 1)

    try:
        prix = int(prix)
    except ValueError:
            # prix was not a number, so silently
            #ignore/discard this line
            continue

    if current_magazin == magazin:
        current_prix += prix  #calculer la somme des prix par magazin
    else:
        if current_magazin:
             # write result to STDOUT
            print '%s\t%s' % (current_magazin, current_prix)  #print cle valeur
        current_magazin = magazin   #passer a la cle suivant (magazin)
        current_prix = prix  #initialisation le prix pour le magazin suivant

    # do not forget to output the last word if needed!
if current_magazin == magazin:
    print '%s\t%s' % (current_magazin, current_prix) #print cle valeur

