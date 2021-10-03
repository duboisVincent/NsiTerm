import doctest

liste1 = [1,2,3,4,5,6]
liste2 = [5,6,7,8,9,10]
def comparer_tableau(liste1,liste2):
    """
    rôle : comparer un élément de chaque
    liste et vérifier si il est présent dans l'autre
    paramètre : deux listes
    """
    element_commun = []
    for element in liste1:
        if element in liste2:
            element_commun += element
    print(element_commun)
    return
print(comparer_tableau(liste1,liste2))