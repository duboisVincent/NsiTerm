import random
class Personnage:
    def __init__(self,nom_du_combatant,points_de_vie,valeurmaxpv,evite,status):
        self.nom = nom_du_combatant
        self.vie = points_de_vie
        self.maxpv = valeurmaxpv
        self.esquive = evite
        self.effet = status
        
    def perd_vie(self):
        chance_desquive = random.random()
        proba_critique_effet = random.random()
        if chance_desquive * 10 < self.esquive:
            print(self.nom + " à esquivé l'attaque!")
        if chance_desquive * 10 > self.esquive:
            if random.random() < 0.5:
                nbPoint = 1
                if proba_critique_effet > 0.9:
                    nbPoint = nbPoint * 5
                    self.vie = self.vie - nbPoint
                    print("Attaque critique! " + self.nom + " à reçu " +str(nbPoint) + " dégat!")
                    if proba_critique_effet > 0.8:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
                else:
                    self.vie = self.vie - nbPoint
                    print(self.nom + " à reçu " +str(nbPoint)+ " dégats!")
                    if proba_critique_effet > 0.8:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
            else:
                nbPoint = 2
                if proba_critique_effet > 0.9:
                    nbPoint = nbPoint * 5
                    self.vie = self.vie - nbPoint
                    print("Attaque critique! " + self.nom + " à reçu " +str(nbPoint)+ " dégats!")
                    if proba_critique_effet > 0.8:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
                else:
                    self.vie = self.vie - nbPoint
                    print(self.nom + " à reçu " +str(nbPoint)+ " dégats!")
                    if proba_critique_effet > 0.8:
                        self.effet = "saigné"
                        print("Oh non! "+ self.nom +" saigne abondament")
                    
    def set_hp(self):
        if self.vie > self.maxpv:
            while self.vie > self.maxpv:
                self.vie = self.vie - 1 
            
    def soin(self):
        valeur_soin = random.random()
        if valeur_soin > 0 and valeur_soin <=0.25:
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
        
bilbo = Personnage("Bilbo",12,12,1.5,"")
gollum = Personnage("Gollum",17,17,1.7,"")
frodon = Personnage("Frodon",20,20,1.5,"")
araignee = Personnage("Araignée",6,6,1.1,"")
sauron = Personnage("Sauron",25,25,1.2,"")
goblin = Personnage("Goblin",6,6,1.1,"")
test1 = Personnage("test1",200,200,1.1,"")
test2 = Personnage("test2",200,200,1.1,"")


def game(combattant1,combattant2):    
    while combattant1.vie > 0 and combattant2.vie > 0:
        if combattant1.effet == "saigné":
            combattant1.vie = combattant1.vie - 1
            print(combattant1.nom + " à perdu 1 point de vie à cause de de la perte de sang")
        if combattant2.effet == "saigné":
            combattant2.vie = combattant1.vie - 1
            print(combattant2.nom + " à perdu 1 point de vie à cause de de la perte de sang")
        choix_action = int(input(combattant1.nom + " vous avez " + str(combattant1.vie) + " point(s) de vie, que voullez vous faire? 1 attaquer , 2 vous soigner "))
        print("")    
        if choix_action == 1 :
            combattant2.perd_vie()
        if choix_action == 2 :
            combattant1.soin()
            combattant1.set_hp()
            print("vous avez " + str(combattant1.vie) + " points de vie")
        choix_action = int(input(combattant2.nom + " vous avez " + str(combattant2.vie) + " point(s) de vie, que voullez vous faire? 1 attaquer , 2 vous soigner "))
        print("")
        if choix_action == 1 :
            combattant1.perd_vie()
        if choix_action == 2 :
            combattant2.soin()
            combattant2.set_hp()
            print("vous avez " + str(combattant2.vie) + " points de vie")
       
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points alors que " + combattant2.nom + " est mort"
    return msg

def gamealéa(combattant1,combattant2):
    while combattant1.vie > 0 and combattant2.vie > 0:
        choix_action = random.random()
        print("")    
        if choix_action <= 0.5 :
            combattant2.perd_vie()
        if choix_action >= 0.5 :
            combattant1.soin()
            combattant1.set_hp()
            print("vous avez " + str(combattant1.vie) + " points de vie")
        choix_action = random.random() 
        print("")
        if choix_action <= 0.5:
            combattant1.perd_vie()
        if choix_action >= 0.5 :
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