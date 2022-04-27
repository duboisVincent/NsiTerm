def moyenne(liste):
    long = len(liste)
    somme = 0
    if len(liste) == 0:
        return 'erreur'
    else:
        for val in liste:
            somme += val
    return somme/long

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i = 0
    j = len(tab) - 1
    while i != j :
        if tab[i]== 0:
            i = i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab