#!/usr/bin/env python

from operator import itemgetter
import sys

current_age = None
max_salaire = 0
min_salaire = 0
current_counter = 0
age = None

wordList = dict()
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    age, salaire,counter = line.split('\t', 3)

    try:
        salaire = int(salaire)
    except ValueError:
            # salaire was not a number, so silently
            #ignore/discard this line
            continue
    try:
        counter = int(counter)
    except ValueError:
            # counter was not a number, so silently
            #ignore/discard this line
            continue
    if min_salaire == 0:
        min_salaire == salaire  #initialiser  une valeur au minimum pour la premier cle,valeur
    if current_age == age:
        if max_salaire < salaire:  # le maximum
            max_salaire = salaire
        if min_salaire > salaire: #le minimum
            min_salaire = salaire
        current_counter += 1 #calcule le nombre du employer par age
    else:
        if current_age:
             # write result to STDOUT
            print '%s\t%s\t%s\t%s' % (current_age, max_salaire , min_salaire , current_counter)
        current_age = age  #passer a la cle suivant
        current_counter = counter  #initialisation du conteur de l age suivant
        current_salaire = salaire #initialisation du salaire de l age suivant
        min_salaire =salaire #intialiser premier salaire de la cle suivant comme un minimum
        max_salaire = salaire  #intialiser premier salaire de la cle suivant comme un maximum

    # do not forget to output the last word if needed!
if current_age == age:
    print '%s\t%s\t%s\t%s' % (current_age, max_salaire , min_salaire , current_counter)

