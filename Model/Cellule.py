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
    """ cette fonction sert à vérifier un nombre peut représenter le contenu d'une cellule"""
    res = False
    if type(entier) == int:
        if entier == const.ID_MINE or (entier <= 8 and entier >= 0) :
            res = True
    return res

def construireCellule(contenu: int=0, visible: bool=False) -> dict :
    """la fonction sert à initialiser un dictionnaire representant le contenu de la cellule et sa visibilité"""
    if isContenuCorrect(contenu) == False:
        raise ValueError(" construireCellule : le contenu ",contenu, " n’est pas correct ")
    if type(visible) != bool :
        raise TypeError(" construireCellule : le second paramètre", type(visible)," n’est pas un booléen ")
    dict={const.CONTENU: contenu, const.VISIBLE: visible}
    return dict

def getContenuCellule(cell: dict) ->int :
    """sert a récupérer le contenu d'une cellule a partir du dictionnaire """
    if type_cellule(cell)==False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule")
    return cell[const.CONTENU]

def isVisibleCellule(cell: dict) -> bool :
    """permet de vérifier la visibilitée de la cellule"""
    if type_cellule(cell)==False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell[const.VISIBLE]

def setContenuCellule(cell: dict, contenu: int) -> None :
    """ permet de modifier le contenu la cellule"""
    if type_cellule(cell)==False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if type(contenu)!= int:
        raise TypeError(" la valeur du contenu ",contenu ," n’est pas correcte.")
    if isContenuCorrect(contenu) == False:
        raise ValueError(" la valeur du contenu ",contenu ," n’est pas correcte.")
    cell[const.CONTENU]= contenu
    return None

def setVisibleCellule(cell: dict, visible: bool) -> None:
    """ permet de mofifer la visibilitée d'une cellule"""
    if type_cellule(cell)==False:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visible)!= bool:
        raise TypeError("etVisibleCellule : Le second paramètre n’est pas un booléen")
    cell[const.VISIBLE] = visible
    return None

def contientMineCellule(cell: dict) ->bool:
    if type_cellule(cell)==False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    res=False
    if cell[const.CONTENU]==const.ID_MINE:
        res=True
    return res









