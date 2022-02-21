from visualisation_arbre import *
from random import randint

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
    # Insérer votre code ici
arbre = [2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]]
show(arbre,"arbre")
arbre_vide = []
arbre_feuille  = [1,[[],[]]]
# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
    # Insérer votre code ici

# # PARTIE 2 - CODE ET TESTS A ECRIRE


def est_vide(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si un arbre est vide
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est vide, False sinon
    
    TESTS :
    >>> est_vide(arbre)
    False
    
    >>> est_vide(arbre_vide)
    True
    
    >>> est_vide(arbre_feuille)
    False
    '''
    return arbre == []

def est_feuille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si l'arbre est une feuille
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est une feuille, False sinon
    
    TESTS :
    >>> est_feuille(arbre)
    False
    
    >>> est_feuille(arbre_vide)
    False
    
    >>> est_feuille(arbre_feuille)
    False 
    '''
    # 50 est = à true mais sag et sad pas fait
    
    # A compléter
    return SAG == [] and SAD == []
        

def racine(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie la valeur du noeud racine
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int, str, etc...) : Valeur du noeud racine
    précondition : que arbre ne soit pas vide
    
    TESTS :
    >>> racine(arbre)
    2
    
    >>> racine(arbre_vide)
    False
    
    >>> racine(arbre_feuille)
    1
    '''
    assert not est_vide(arbre), "votre arbre est vide"
    return arbre[0]
    
    # Code de la fonction à compléter

def SAG(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre gauche
    précondition : A compléter
    
    TESTS :
    >>> SAG(arbre)
    
    
    >>> SAG(arbre_vide)
    
    
    >>> SAG(arbre_feuille)
    
    '''

    assert not est_vide(arbre[1]), " le sous arbre gauche est vide" # A compléter
    # Code de la fonction à compléter
    return arbre[1]
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
def SAD(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre droit de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre droit
    précondition : A compléter
    
    TESTS :
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail) 
    assert not es_vide(arbre[2]), " le sous arbre droit est vide" # A compléter
    # Code de la fonction à compléter
    return arbre[2]
def taille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la taille d'un arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Taille de l'arbre
    
    TESTS :
    '''
    # A compléter

def hauteur(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
            donnée dans l'énoncé
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Hauteur de l'arbre
    
    TESTS :
    >>> hauteur(arbre)
    6
    
    >>> hauteur(arbre_vide)
    0
    
    >>> hauteur(arbre_feuille)
    1
    '''
    return (arbre)

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def est_egal(arbre1, arbre2):
    '''
    DOCUMENTATION :
    Description de la fontion : détermine si deux arbres sont identiques ou différents
    arbre1 (list) : Arbre implémenté sous forme de listes imbriquées
    arbre2 (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si les deux arbres sont identiques, False sinon 
    
    TESTS :
    '''
    # A compléter

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    
    # PARTIE 2 - Question 3
    
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter
    
    # PARTIE 2 - Question 4 
    # A compléter