from visualisation_arbre_PO import *
from random import randint

# IMPLEMENTATION DE LA CLASSE NOEUD

class Noeud:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

# PARTIE 2 - CODE ET TESTS A ECRIRE

class Arbre:
    def __init__(self, noeud=None):
        self.racine = noeud

    def est_vide(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est vide
        return (bool) : True si l'arbre est vide, False sinon
        
        TESTS :
        >>> arbre.est_vide()
        False
        
        >>> arbrefeuille.est_vide()
        False
        
        >>> arbrevide.est_vide()
        True
        
        '''
        if self.racine == None:
            return True
        else:
            return False
        
    def est_feuille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est une feuille
        return (bool) : True si l'arbre est une feuille, False sinon
        
        TESTS :
        >>> arbre.est_feuille()
        False
        
        >>> arbrefeuille.est_feuille()
        True
        
        >>> arbrevide.est_feuille()
        False
        '''
        if self.racine.gauche == None and self.racine.droit == None:
            return True
        else:
            return False


    def valeur_racine(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie la valeur de la racine de l'arbre
        return (int, str, etc...) : Valeur de la racine de l'arbre
        précondition : A compléter
        
        TESTS :
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert self.est_vide, "Un arbre vide n'a pas de racine" # A compléter
        # Code de la fonction à compléter
        return self.racine.valeur
    
    def SAG(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
        return (Arbre) : sous-arbre gauche
        précondition : A compléter
        
        TESTS :
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert self.est_vide, " " # A compléter
        # Code de la fonction à compléter
    
    def SAD(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre droit de l'arbre
        return (Arbre) : sous-arbre droit
        précondition : A compléter
        
        TESTS :
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert ..., " " # A compléter
        # Code de la fonction à compléter
    
    def taille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la taille d'un arbre
        return (int) : Taille de l'arbre
        
        TESTS :
        '''
        #A compléter

    def hauteur(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
                donnée dans l'énoncé
        return (int) : Hauteur de l'arbre
        
        TESTS :
        '''
        #A compléter

    def est_egal(self, arbre):
        '''
        DOCUMENTATION :
        Description de la fontion : détermine si deux arbres sont identiques ou différents
        arbre (Arbre) : arbre sur lequel on va tester l'égalité
        return (bool) : True si les deux arbres sont identiques, False sinon 
        
        TESTS :
        '''
        #A compléter   

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter   
        
def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    

    # PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2


    # PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
    noeud = Noeud(2, Noeud(8, Noeud(6, None, None), Noeud(9, None, None)), Noeud(1, Noeud(7, None, None), None))
    arbre = Arbre(noeud)
    noeudfeuille = Noeud(2,None,None)
    arbrefeuille = Arbre(noeudfeuille)
    arbrevide = Arbre()
    # PARTIE 2 - Question 3
        
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter

# PARTIE 2 - Question 4
    # A compléter
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

