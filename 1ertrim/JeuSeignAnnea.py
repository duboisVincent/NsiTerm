import random
class Personnage:

    def __init__(self,nom_du_combatant,points_de_vie):
        self.nom = nom_du_combatant
        self.vie = points_de_vie
        
    def perd_vie(self):
        if random.random() < 0.5:
            nbPoint = 1
            self.vie = self.vie - nbPoint
        else:
            nbPoint = 2
            self.vie = self.vie - nbPoint
            
bilbo = Personnage("Bilbo",20)
gollum = Personnage("Gollum",20)
frodon = Personnage("Frodon", 20)
araignee = Personnage("Araignée", 5)
sauron = Personnage("Sauron",50)
def game(combattant1,combattant2):    
    while combattant1.vie > 0 and combattant2.vie > 0:
        perte1 = combattant1.perd_vie()
        print(combattant1.nom + " perd " + str(perte1) + " point de vie")
        perte2 = combattant2.perd_vie()
        print(combattant2.nom + " perd " + str(perte2) + " point de vie")
        
    if combattant1.vie <= 0 and combattant2.vie > 0:
        msg = combattant2.nom + " est vainqueur, il lui reste encore " + str(combattant2.vie) + " points alors que " + combattant1.nom + " est mort"
    elif combattant2.vie <= 0 and combattant1.vie > 0:
        msg = combattant1.nom + " est vainqueur, il lui reste encore " + str(combattant1.vie) + " points alors que " + combattant2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"
    return msg

