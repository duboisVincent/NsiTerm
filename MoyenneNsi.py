liste = [12,15,78,84,15] 

def MoyenneElement(Liste):
    moyenne = 0
    Len = len(liste)
    for i in liste:
        moyenne += i
    moyenne = moyenne / Len
    return moyenne
print("La moyenne de la liste est",MoyenneElement(liste))

def MoyenneIndice(Liste):
    moyenne = 0
    Len = len(liste)
    long = len(liste)
    for i in range(long):
        moyenne = moyenne + liste[i]
    moyenne = moyenne / Len
    return moyenne
print("La moyenne de la liste est",MoyenneIndice(liste))

k = 0
while k != sum(liste):
    k = k + 1
    if k == sum(liste):
        print("La moyenne de la liste est",k/ len(liste))
    