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
    if type_grille_demineur(grille) == False or type_coordonnee(coordonnee) == False:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coordonnee) == False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coordonnee[0]][coordonnee[1]]


def getContenuGrilleDemineur(grille: list, coordonnee: tuple) -> dict:
    """permet d'obtenir le contenu de la cellule passée en paramètre"""
    cell = getCelluleGrilleDemineur(grille, coordonnee)
    return getContenuCellule(cell)


def setContenuGrilleDemineur(grille: list, coordonnee: tuple, contenu: int) -> None:
    """permet de remplacer le contenu d'une cellule précise"""
    cell = getCelluleGrilleDemineur(grille, coordonnee)
    setContenuCellule(cell, contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coordonnee: tuple) -> bool:
    """permet de savoir si une cellule est visible """
    cell = getCelluleGrilleDemineur(grille, coordonnee)
    return cell[const.VISIBLE]


def setVisibleGrilleDemineur(grille: list, coordonnee: tuple, visible: bool) -> None:
    """ permet de changer la visibilitée d'une cellule"""
    cell = getCelluleGrilleDemineur(grille, coordonnee)
    setVisibleCellule(cell, visible)
    return None

def contientMineGrilleDemineur(grille: list, coordonnee: tuple) ->bool:
    """ permet de savoir si une case contient une mine"""
    res=False
    contenu=getContenuGrilleDemineur(grille, coordonnee)
    if contenu==const.ID_MINE:
        res=True
    return res

def getCoordonneeVoisinsGrilleDemineur(grille: list, coordonnee: tuple) -> list:
    """ permet d'obtenir la liste des coordonnées des cellules voisines"""
    if type_coordonnee(coordonnee)==False or type_grille_demineur(grille)== False:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coordonnee)==False:
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    lst=[]
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            coordonnee1=(coordonnee[0]+i,coordonnee[1]+j)
            if isCoordonneeCorrecte(grille,coordonnee1) and coordonnee1!= coordonnee:
                lst.append(coordonnee1)
    return lst

def placerMinesGrilleDemineur(grille: list, nb: int, coordonnee: tuple) -> None:
    """ permet de placer les mine mais pas dans la 1ere case choisit par l'utilisateur"""
    if  nb<0 or nb> (len(grille)*len(grille[0])-1) :
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if isCoordonneeCorrecte(grille, coordonnee)==False:
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    while nb>0:
        x=randint(0,len(grille)-1)
        y=randint(0,len(grille[0])-1)
        a=construireCoordonnee( x, y)
        if a!=coordonnee and getContenuGrilleDemineur(grille, a) != const.ID_MINE :
            setContenuGrilleDemineur(grille, a, const.ID_MINE)
            nb-=1
    compterMinesVoisinesGrilleDemineur(grille)
    print("nb:, nb")
    return None

def compterMinesVoisinesGrilleDemineur(grille: list) ->None:
    """ permet de compter les mines voisines"""
    for l in range(len(grille)):
        for c in range(len(grille[0])):
            coordonnee=(l, c)

            contenu = getContenuGrilleDemineur(grille, coordonnee)
            if not contenu==const.ID_MINE:
                voisins=getCoordonneeVoisinsGrilleDemineur(grille, coordonnee)
                cell = getCelluleGrilleDemineur(grille, coordonnee)
                bombe=0
                for a in voisins:
                    if getContenuGrilleDemineur(grille, a)==const.ID_MINE:
                        bombe+=1
                setContenuGrilleDemineur(grille,coordonnee,bombe)
    return None

def getNbMinesGrilleDemineur(grille: list) ->int:
    """ permet de compter le nombre de mine dans la grille"""
    if type_grille_demineur(grille)==False:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    nbMine=0
    for l in range(len(grille)):
        for c in range(len(grille[0])):
            coordonnee=(l,c)
            cell=getCelluleGrilleDemineur(grille, coordonnee)
            if cell[const.CONTENU]==const.ID_MINE:
                nbMine=nbMine+1
    return nbMine

def getAnnotationGrilleDemineur(grille: list, coordonnee: tuple) ->str:
    """ return l'annotation d'une cellule """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coordonnee))

def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """ permet de compter le nombre de mines restantes non notées par un flag"""
    nb=getNbMinesGrilleDemineur(grille)
    nbDecouvert=0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            coordonnee=(i, j)
            if getAnnotationGrilleDemineur(grille, coordonnee)==const.FLAG:
                nbDecouvert+=1
    return nb -nbDecouvert

def gagneGrilleDemineur(grille: list) ->bool:
    """ permet de vérifier si la partie est gagnée"""
    res=True
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if contientMineGrilleDemineur(grille, (i,j)) and isVisibleGrilleDemineur(grille, (i,j)) :
                res=False
            elif not contientMineGrilleDemineur(grille, (i,j)) and not isVisibleGrilleDemineur(grille, (i,j)) :
                res=False
            elif getAnnotationGrilleDemineur(grille, (i,j))!=const.FLAG and contientMineGrilleDemineur(grille, (i,j)):
                res=False
    return res


def perduGrilleDemineur(grille: list) -> bool:
    """ permet de vérifier si la partie est perdue"""
    res = False
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if contientMineGrilleDemineur(grille, (i,j)) and isVisibleGrilleDemineur(grille, (i, j)):
                res = True

    return res

def reinitialiserGrilleDemineur(grille: list) ->None:
    """ permet de réinitialiser la grille"""
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            cell=getCelluleGrilleDemineur(grille,(i,j))
            reinitialiserCellule(cell)
    return None



