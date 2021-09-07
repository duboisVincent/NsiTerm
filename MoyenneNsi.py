liste = [12,15,78,84,15]

def MoyenneElement(liste):
    moyenne = 0
    for i in liste:
        moyenne += i
    return moyenne
print("La moyenne de la liste est",MoyenneElement(liste))

def MoyenneIndice(liste):
    moyenne = 0
    long = len(liste)
    for i in range(long):
        moyenne = moyenne + liste[i]
    return moyenne
print("La moyenne de la liste est",MoyenneIndice(liste))

k = 0
while k != sum(liste):
    k = k + 1
    if k == sum(liste):
        print("La moyenne de la liste est de",k)
