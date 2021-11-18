import random

class Personnage:
    def __init__(self,nom_du_combatant,points_de_vie,evite):
        self.nom = nom_du_combatant
        self.vie = points_de_vie
        self.esquive = evite
    def perd_vie(self):
        chance_desquive = random.random() 
        if chance_desquive * 10 < self.esquive:
            print(self.nom + " à esquivé l'attaque!")
        if chance_desquive * 10 > self.esquive:
            if random.random() < 0.5:
                nbPoint = 1
                self.vie = self.vie - nbPoint
                print(self.nom + " à reçu " +str(nbPoint) + " dégat!")
            else:
                nbPoint = 2
                self.vie = self.vie - nbPoint
                print(self.nom + " à reçu " +str(nbPoint)+ " dégats!")
        
bilbo = Personnage("Bilbo",20,1.5)
gollum = Personnage("Gollum",20,1.7)
frodon = Personnage("Frodon",20,1.5)
araignee = Personnage("Araignée",5,1.1)
sauron = Personnage("Sauron",50,1.2)

def game(combattant1,combattant2):    
    while combattant1.vie > 0 and combattant2.vie > 0:
        combattant1.perd_vie()
        combattant2.perd_vie()
       
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points alors que " + combattant2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"
    return msg


