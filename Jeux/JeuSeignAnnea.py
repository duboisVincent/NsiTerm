import random
allowed_values = ["1","2","3"]
class Personnage:
    def __init__(self,nom_du_combatant,points_de_vie,valeurmaxpv,evite,status,jauge_magie):
        self.nom = nom_du_combatant
        self.vie = points_de_vie
        self.maxpv = valeurmaxpv
        self.esquive = evite
        self.effet = status
        self.p_magie = jauge_magie
        
    def perd_vie(self):
        chance_desquive = random.random()
        proba_critique_effet = random.random()
        if chance_desquive * 10 < self.esquive:
            print(self.nom + " à esquivé l'attaque!")
        if chance_desquive * 10 > self.esquive:
            if random.random() < 0.5:
                nbPoint = 1
                if proba_critique_effet > 0.8:
                    nbPoint = nbPoint * 2
                    self.vie = self.vie - nbPoint
                    print("Attaque critique! " + self.nom + " à reçu " +str(nbPoint) + " dégat!")
                    if proba_critique_effet > 0.9:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
                else:
                    self.vie = self.vie - nbPoint
                    print(self.nom + " à reçu " +str(nbPoint)+ " dégats!")
                    if proba_critique_effet > 0.9:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
            else:
                nbPoint = 2
                if proba_critique_effet > 0.8:
                    nbPoint = nbPoint * 2
                    self.vie = self.vie - nbPoint
                    print("Attaque critique! " + self.nom + " à reçu " +str(nbPoint)+ " dégats!")
                    if proba_critique_effet > 0.9:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
                else:
                    self.vie = self.vie - nbPoint
                    print(self.nom + " à reçu " +str(nbPoint)+ " dégats!")
                    if proba_critique_effet > 0.9:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
                    
    def set_hp(self):
        if self.vie > self.maxpv:
            while self.vie > self.maxpv:
                self.vie = self.vie - 1 
            
    def soin(self):
        valeur_soin = random.random()
        valeur_fin_status = random.random()
        soin_saigné = random.random()
        if valeur_fin_status > 0.80:
            self.status = ""
            print(self.nom + " n'a plus d'effet de status")
            if self.effet == "saigné":
                if soin_saigné >= 0.5:
                    valeur_soin = 0
        if valeur_soin >= 0 and valeur_soin <=0.25:
            self.vie = self.vie + 1
            print(self.nom + " S'est soigné de 1 dégats")
        if valeur_soin > 0.25 and valeur_soin <= 0.5:
            self.vie = self.vie + 2
            print(self.nom + " S'est soigné de 2 dégats")
        if valeur_soin > 0.5 and valeur_soin <= 0.75:
            self.vie = self.vie + 3
            print(self.nom + " S'est soigné de 3 dégats")
        if valeur_soin > 0.75:
            self.vie = self.vie + 4
            print(self.nom + " S'est soigné de 4 dégats")
            
    def magie(self,J2):
        sort_lancable = ["poison","explosion","regeneration","pacte"]
        print("")
        print("poison: met poison à votre adversaire (coût: 5) ")
        print("")
        print("explosion: inflige 7 degats (coût: 5)")
        print("")
        print("regeneration: vous retire votre status (coût: 4)")
        print("")
        print("pacte: vous redonne 1 point de mana (coût: 2pv)")
        print("")
        sort = input("Quel sort voullez vous lancer ? ")
        while sort not in sort_lancable:
            sort = input("Quel sort voullez vous lancer ? ")
        if sort == "poison":
            J2.effet = "poison"
            print(J2.nom + " est maintenant empoisoné")
            self.p_magie = self.p_magie - 5
        if sort == "explosion":
            J2.vie = J2.vie - 7
            self.p_magie = self.p_magie - 5
            print(J2.nom + " à reçu 7 dégats de l'explosion")
        if sort == "regeneration":
            self.effet = ""
            print(self.nom + " n'a plus d'effet de statut")
            self.p_magie = self.p_magie - 4
        if sort == "pacte":
            self.p_magie += 1
            self.vie -= 2
            print("vous avez effectué le pacte ")
                         
bilbo = Personnage("Bilbo",25,25,1.5,"",10)
gollum = Personnage("Gollum",17,17,1.7,"",10)
frodon = Personnage("Frodon",20,20,1.5,"",10)
araignee = Personnage("Araignée",6,6,1.1,"",10)
sauron = Personnage("Sauron",25,25,1.2,"",10)
goblin = Personnage("Goblin",6,6,1.1,"",10)
test1 = Personnage("test1",200,200,1.1,"",1)
test2 = Personnage("test2",200,200,1.1,"",1)


def game(combattant1,combattant2):
    while combattant1.vie > 0 and combattant2.vie > 0:
        if combattant1.p_magie < 4:
            print("vous n'avez pas assez de mana pour lancer un sort, utilisez l'une des deux autres options ")
            print("")
        choix_action = (input(combattant1.nom + " vous avez " + str(combattant1.vie) + " point(s) de vie, que voullez vous faire? 1 attaquer, 2 vous soigner,3 lancer un sort "))
        print("")
        while choix_action not in allowed_values:
            choix_action = (input("action non autorisé " + combattant1.nom + " vous avez " + str(combattant1.vie) + " point(s) de vie, que voullez vous faire? 1 attaquer, 2 vous soigner, 3 lancer un sort "))
        if choix_action == "1" :
            combattant2.perd_vie()
        if choix_action == "2" :
            combattant1.soin()
            combattant1.set_hp()
            print("vous avez " + str(combattant1.vie) + " points de vie")
        if choix_action == "3" :
            combattant1.magie(combattant2)
            print("Il reste à " + combattant1.nom + " " + str(combattant1.p_magie) + " points de magie ")
            if combattant2.p_magie < 4:
                print("vous n'avez pas assez de mana pour lancer un sort, utilisez l'une des deux autres options")
                print("")
        choix_action = (input(combattant2.nom + " vous avez " + str(combattant2.vie) + " point(s) de vie, que voullez vous faire? 1 attaquer, 2 vous soigner, 3 lancer un sort "))
        print("")
        while choix_action not in allowed_values:
            choix_action = (input("action non autorisé " + combattant2.nom + " vous avez " + str(combattant2.vie) + " point(s) de vie, que voullez vous faire? 1 attaquer, 2 vous soigner, 3 lancer un sort "))
        if choix_action == "1" :
            combattant1.perd_vie()
        if choix_action == "2" :
            combattant2.soin()
            combattant2.set_hp()
            print("vous avez " + str(combattant2.vie) + " points de vie")
        if choix_action == "3":
            combattant2.magie(combattant1)
            print("Il reste à " + combattant2.nom + " " + str(combattant2.p_magie) + " points de magie ")
        print(combattant1.nom + " et " + combattant2.nom + " on régénéré 1 point de mana")
        print("")
        combattant1.p_magie += 1
        combattant2.p_magie += 2
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points alors que " + combattant2.nom + " est mort"
    return msg

def gamealea(combattant1,combattant2):
    while combattant1.vie > 0 and combattant2.vie > 0:
        choix_action = random.random()
        print("")    
        if choix_action <= 0.6 :
            combattant2.perd_vie()
        if choix_action >= 0.6 :
            combattant1.soin()
            combattant1.set_hp()
            print("vous avez " + str(combattant1.vie) + " points de vie")
        choix_action = random.random() 
        print("")
        if choix_action <= 0.6:
            combattant1.perd_vie()
        if choix_action >= 0.6 :
            combattant2.soin()
            combattant2.set_hp()
            print("vous avez " + str(combattant2.vie) + " points de vie")
    
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points alors que " + combattant2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"
    return msg