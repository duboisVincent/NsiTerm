#on prend le module randint

import random

#on prend un mot de notre liste

liste_mots = ["laitue", "hareng", "jambon", "pharynx", "phoque", "langue",
                "stylo","agent","fromage","whisky","billet","boyaux",
                "laser","joystick","crane","joyeux","cahier","camping","argent",
                "rivage","physique",]
chaine = (liste_mots[random.randint(0,21)])

#on retire nos accents

chaine = chaine.replace("é","e")
chaine = chaine.replace("è","e")
chaine = chaine.replace("ê","e")
chaine = chaine.replace("à","a")
chaine = chaine.replace("â","a") 
chaine = chaine.replace("ù","u")
chaine = chaine.replace("û","u")
chaine = chaine.replace("î","i")
chaine = chaine.replace("ô","o")

#le jeu en lui même
def jeu(chaine):
    #je cammoufle le mot avec des '_'
    chaine = (liste_mots[random.randint(0,21)])
    longueur = len(chaine)
    barre = ['_']
    barre = barre * longueur
    #l'utilisateur entre une lettre
    lettre_proposé = input("essayez une lettre ")
    #on verifie si la lettre est dans le mot
    for toutes_les_lettres in chaine:
        for lettre in chaine:
            if lettre == lettre_proposé:
                barre[lettre] = str(lettre_proposé)
    print(barre)