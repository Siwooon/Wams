import math
from itertools import combinations, product, islice
from random import *
# max nombre de sujets

total_possibilities = 0


# Calcule le nombre de possibilités pour chaque catégorie de questions
java_possibilities = math.comb(7, 4)
compilation_possibilities = math.comb(9, 3)
php_possibilities = math.comb(5, 3)

# Ajoute le nombre total de possibilités pour le nombre de questions actuel
total_possibilities += java_possibilities * compilation_possibilities * php_possibilities

# Affiche le nombre total de possibilités
print("Le nombre total de possibilités de questionnaire est de :", total_possibilities)


# _______________________________________________________


lJava = ["j1", "j2", "j3", "j4", "j5", "j6", "j7"]
lCompile = ["c1", "c2", "c3","c4", "c5", "c6", "c7", "c8", "c9"]
lphp = ["p1", "p2", "p3", "p4", "p5"]

dicoTout={}
#itération sur les étiquettes différentes dans la db
    #itération sur les questions possédant cette étiquette comme première étiquette
        #dico[étiquette].append(question)

def evaluate_sublists(lst, n):
    lrep=[]
    for comb in combinations(lst, n):
        lrep.append(comb)
    print(lrep)
    return(lrep)

listeJava=evaluate_sublists(lJava, 4)
listeCompile=evaluate_sublists(lCompile, 3)
listePHP=evaluate_sublists(lphp, 3)





def evaluate_combinations(list1, list2, list3):

    for i in range(88):
        combs = product(list1, list2, list3)
        a = randint(0, total_possibilities)
        if a*10 < total_possibilities : a=a*10
        print(list(islice(combs, a, a+1)))
   



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = ["x", "y", "z"]

evaluate_combinations(listeJava, listeCompile, listePHP)