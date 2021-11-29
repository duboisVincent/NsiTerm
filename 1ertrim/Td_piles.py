def creer_pile():
    """ Créé une pile vide
    :return: Une pile vide représentée par la liste vide
    """
    return []


def est_vide(p):
    """ Teste si une pile est vide
    :param p: Une pile
    :return: True si p est vide, False sinon
    """
    return p == []


def empiler(p, e):
    """ Empile un élément au sommet d'une pile
    :param p: Une pile
    :param e: Un élément
    :return: None
    :Effets: Empile e au sommet de p
    """
    p.append(e)
    

def depiler(p):
    """ Dépile un élément au sommet d'une pile et le renvoie
    :param p: Une pile
    :return: L'élément au sommet de la pile
    :Précondition: p est non vide
    """
    assert not est_vide(p), "Impossible de dépiler une pile vide"
    return p.pop()

#Exo 1

def pile_alternee(n):
    p = creer_pile()
    for i in range (n):
        if i % 2 == 0:
            empiler(p, i)
        else:
            empiler(p,-i)
    return p
print(pile_alternee(7))

#Exo 2 - 1
def vider_pile(pile):
    while not est_vide(pile):
        depiler(pile)


p = creer_pile()
empiler(p, 2)
empiler(p, 8)
empiler(p, 12)
print(p)

vider_pile(p)
print(p)

pile_t = creer_pile()
empiler(pile_t, 1)
empiler(pile_t, 2)
empiler(pile_t, 3)

def sommet_pile(pile):
    if est_vide:
        return None
    else:
        temp = depiler(pile)
        empiler(pile, temp)
        return temp
print(sommet_pile(pile_t))

pile_texte = creer_pile()
empiler(pile_texte,"(")
empiler(pile_texte,")")
empiler(pile_texte,"(")
empiler(pile_texte,")")
empiler(pile_texte,"(")
empiler(pile_texte,")")

def bon_parenthésage(chaine):
    pile = creer_pile
    for l in chaine:
        if l == "(":
            empiler(pile , l)
        else:
            if est_vide == False:
                depiler(pile)
            else:
                return False
    return est_vide(pile)
print(bon_parenthésage("(())()"))
print(bon_parenthésage("()("))
print(bon_parenthésage("(())"))