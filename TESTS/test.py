from math import comb
from itertools import combinations, islice, product
import random


# calcule possibilité de a parmis liste1, etc
def calcul_possibilitees(liste1, liste2, liste3, nb_exo1, nb_exo2, nb_exo3):
    return comb(len(liste1), nb_exo1) * comb(len(liste2), nb_exo2) * comb(len(liste3), nb_exo3)


def evaluate_combinations(list1, list2, list3, nb_exo1, nb_exo2, nb_exo3, nb_sujets):
    # Retourne les listes de combinaisons de liste, nb_exo
    sublists1 = list(combinations(list1, nb_exo1))
    sublists2 = list(combinations(list2, nb_exo2))
    sublists3 = list(combinations(list3, nb_exo3))
    # Retourne la liste tronquée à nb_sujets sujets
    return list(product(sublists1, sublists2, sublists3))[:nb_sujets]


total_possibilities = 0

listeJava = ["j1", "j2", "j3", "j4", "j5", "j6", "j7"]
listeCompile = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"]
listePHP = ["p1", "p2", "p3", "p4", "p5"]

nbExoJava = 4
nbExoCompile = 3
nbExoPHP = 3

nbSujet = 88

print(evaluate_combinations(listeJava, listeCompile,
      listePHP, nbExoJava, nbExoCompile, nbExoPHP, nbSujet)[0])

print("Le nombre total de possibilités de questionnaire est de :", calcul_possibilitees(
    listeJava, listeCompile, listePHP, nbExoJava, nbExoCompile, nbExoPHP))

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
    return(lrep)

listeJava=evaluate_sublists(lJava, 4)
listeCompile=evaluate_sublists(lCompile, 3)
listePHP=evaluate_sublists(lphp, 3)





def evaluate_combinations(list1, list2, list3):

    combs = product(list1, list2, list3)
    random.shuffle(combs)
    sto = 0
    for comb in islice(combs, 88):
        sto+=1

        print(comb)
    print(sto)

evaluate_combinations(listeJava, listeCompile, listePHP)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = ["x", "y", "z"]
