# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                                         and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nbLigne: int, nbColonne: int) -> list:
    """ permet de construire la grille du demineur"""
    if nbLigne <= 0 or nbColonne <= 0:
        raise ValueError("construireGrilleDemineur : Le nombre de lignes", nbLigne, " ou de colonnes", nbColonne,
                         " est négatif ou nul.")
    if type(nbLigne) != int or type(nbColonne) != int:
        raise TypeError("construireGrilleDemineur : Le nombre de lignes", type(nbLigne), " ou de colonnes ",
                        type(nbColonne), " n’est pas un entier")
    list = []
    l1 = []
    for i in range(nbLigne):
        for j in range(nbColonne):
            l1.append(construireCellule())
        list.append(l1)
        l1 = []
    return list


def getNbLignesGrilleDemineur(grille: list) -> int:
    """permet d'obtenir le nombre de lignes dans la grille"""
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """permet d'obtenir le nombre de colonnes dans la grille"""
    if type_grille_demineur(grille) == False:
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    nbCol = 1
    for j in range(len(grille[0])):
        nbCol += 1
    return j + 1


def isCoordonneeCorrecte(grille: list, coordonnee: tuple) -> bool:
    """permet de vérifier si une case est dans la grille"""
    res = False
    if type(grille) != list or type(coordonnee) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    if 0 <= coordonnee[0] < len(grille):
        if 0 <= coordonnee[1] < getNbColonnesGrilleDemineur(grille):
            return True
    return res

def getCelluleGrilleDemineur(grille: list, coordonnee: tuple) -> dict:
    """permet de récupérer les informations d'une cellule"""
    if type_grille_demineur(grille)==False or type_coordonnee(coordonnee)==False:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coordonnee)==False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coordonnee[0]][coordonnee[1]]

