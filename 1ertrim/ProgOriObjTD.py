from math import sqrt
#Ex 1
class Eleve:
    def __init__(self,nomeleve,classeeleve,noteeleve):
        self.nom = nomeleve
        self.classe = classeeleve
        self.note = noteeleve
        
vincent = Eleve("Vincent","TG",12.70)
yoni = Eleve("Yoni","TG",12.69)
sofiane = Eleve("Sofiane","TG",12.70)
elevetoujoursabs = Eleve("Il est toujours absent","TG",0)

def compare(eleve1,eleve2):
    if eleve1.note > eleve2.note:
        return eleve1.note
    if eleve2.note > eleve1.note:
        return eleve2.note
    if eleve1.note == eleve2.note :
        return (eleve1.nom , eleve2.nom)
    
print(compare(vincent,yoni))
print(compare(vincent,sofiane))
print(compare(yoni,sofiane))

def a_la_moyenne(eleve1,eleve2,eleve3,eleve4):
    moyenne = (eleve1.note + eleve2.note + eleve3.note + eleve4.note) / 4
    if eleve1.note > moyenne:
        return True
    else:
        return False
print(a_la_moyenne(vincent,yoni,sofiane,elevetoujoursabs))
print(a_la_moyenne(yoni,sofiane,elevetoujoursabs,vincent))
print(a_la_moyenne(sofiane,elevetoujoursabs,vincent,yoni))
print(a_la_moyenne(elevetoujoursabs,vincent,yoni,sofiane))

#Ex 2
class TriangleRectangle:
    def __init__ (self,cote1,cote2,hypo):
        self.longeur = cote1
        self.largeur = cote2
        self.hypothenus = hypo
constructeur = TriangleRectangle(4,5,sqrt((4**2)+5**2))