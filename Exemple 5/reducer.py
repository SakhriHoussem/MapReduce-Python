#!/usr/bin/env python

from operator import itemgetter
import sys
import math
ecartype=0
current_age = None
moyenne_salaire = 0
current_counter = 0
sumSalaire = 0
salaireList= list()
age = None

def calculMoyenne(sum,n):
    return sum/n  #calcule moyenne du salaire

def ecartType(ValueList,moyList,n,som = 0):
    for i in ValueList: #parcourir la list
        som += (i-moyList)**2  # calcul la sum du (x - x bar)**2
    ecartype = som/n #la som / nembre d element
    return math.sqrt(ecartype)

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    age, salaire ,counter = line.split('\t', 3)

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
    if current_age == age:
        sumSalaire += salaire #calcule la somme de salaire des employers par age
        current_counter +=  counter #calcule le nombre du employer par age
        salaireList.append(salaire) #sauvgarder les valeurs de la cle dans une list pour calcule d ecart type
    else:
        if current_age:
            moyenne_salaire = calculMoyenne(sumSalaire,current_counter)  #calcule moyenne du salaire
            ecartype = ecartType(salaireList,moyenne_salaire,current_counter) #calcule ecart type du salaire

            del salaireList[:]
             # write result to STDOUT
            print '%s\t%s\t%s\t%s' % (current_age,moyenne_salaire ,ecartype ,current_counter)
        current_age = age #passer a la cle suivant
        current_counter = counter #initialisation du conteur de l age suivant
        sumSalaire = salaire #initialisation du salaire de l age suivant
        salaireList.append(salaire) #sauvgarder les valeurs de la cle dans une list pour calcule d ecart type
        ecartype=0  #intialiser l ecart type de la cle suivant


    # do not forget to output the last word if needed!
if current_age == age:
    #pour la dernier ligne
    moyenne_salaire = calculMoyenne(sumSalaire,current_counter)  #calcule moyenne du salaire
    ecartype = ecartType(salaireList,moyenne_salaire,current_counter)  #calcule ecart type du salaire
    del salaireList[:]
    print '%s\t%s\t%s\t%s' % (current_age, moyenne_salaire ,ecartype , current_counter)
