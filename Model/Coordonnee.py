# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(numL: int, numC: int) -> tuple :
    ''' la fonction sert à créer une coordonnée sous la forme d'un tuple(L, C) en recevant la ligne et la colonne'''
    if type(numL) != int or type(numC) != int:
        raise TypeError("construireCoordonnee : Le numéro de ligne type_du_premier_paramètre ou le numéro de colonne type_du_second_paramètre ne sont pas des entiers")
    if numL<0 or numC<0:
        raise ValueError("construireCoordonnee : Le numéro de ligne", numL," ou de colonne ", numC," ne sont pas positifs")
    tuple = (numL, numC)
    return tuple

def getLigneCoordonnee (coordonnee: tuple) -> int:
    ''' la fonction sert a récupérer la ligne dans une coordonnee'''
    if type(coordonnee) != tuple:
        raise TypeError(" getLigneCoordonnee : Le paramètre n’est pas une coordonnée ")
    return coordonnee[0]
coo=(1,2)

def getColonneCoordonnee(coordonnee: tuple) -> int:
    ''' la fonction sert a récupérer la colonne dans une coordonnee'''
    if type(coordonnee)!=tuple:
        raise TypeError(" getColonneCoordonnee : Le paramètre n’est pas une coordonnée ")
    return coordonnee[1]





