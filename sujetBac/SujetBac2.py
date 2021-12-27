def moyenne(listev):
    assert listev != [],"erreur"
    nbv = len(listev)
    somme = 0
    for i in listev:
        somme = somme + i
    return somme/nbv

def tri(tab):
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i]=valeur
            j= j-1
    return tab

