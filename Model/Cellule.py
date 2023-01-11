# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(entier:int) ->bool :
    """ cette fonction sert à vérifier un nombre peut représenter le contenu d'une cellule, optionnel fait"""
    res = False
    if type(entier) == int:
        if entier == const.ID_MINE or (entier <= 8 and entier >= 0) :
            res = True
    return res

def construireCellule (contenu: int=0, visible: bool=False) -> dict :
    """la fonction sert à initialiser un dictionnaire representant le contenu de la cellule et sa visibilité"""
    if type(contenu) != int or isContenuCorrect(contenu) == False:
        raise ValueError(" construireCellule : le contenu ",contenu, " n’est pas correct ")
    if type(visible) != bool :
        raise TypeError(" construireCellule : le second paramètre", type(visible)," n’est pas un booléen ")
    dict={const.CONTENU: contenu, const.VISIBLE: visible}
    return dict








