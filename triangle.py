import math

"""class TriangleRectangle:
    def __init__(self,cote1,cote2):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hypothenus = math.sqrt(cote2**2 + cote1**2)
        
    def get_cote1(self):
       return self.cote1
    def get_cote2(self):
        return self.cote2
    
    def set_cote1(self,nb,cote2):
        self.cote1 = nb
        self.hypothenuse = math.sqrt(cote2**2 + cote1**2)
        
    def set_cote2(self,nb,cote1):
        self.cote2 = nb
        self.hypothenuse = math.sqrt(cote2**2 + cote1**2)
        
triangle = TriangleRectangle(14,6)
print(triangle.cote1)
print(triangle.cote2)
print(triangle.hypothenus)"""

"""class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")" 
        
    def distance(self):
        print("la distance entre le point et l'origine est de " + math.sqrt((self.x**2)+self.y**2))
        
a = Point(-2,5)
b = Point(5,5)
c = Point(-2,-2)
d = Point(5,-2)
"""


class Fraction:
    def __init__(self,numerateur,denominateur):
        self.num = numerateur
        self. denom = denominateur
        
    def __repr__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return str(self.num) + " / " + str(self.denom)
        
    def __eq__(self,equa2):
        if self.num / self. denom == equa2.num / equa2.denom:
            return True
        else:
            return False
        
    def __lt__(self,equa2):
        if self.num / self.denom < equa2.num / equa2.denom:
            return True
        else:
            return False
        
    def __add__(self,equa2):
        if self.denom == equa2.denom:
            return (self.num + equa2.num ) / self.denom
        else:
            return (self.num * equa2.denom + equa2.num * self.denom)/self.denom * equa2.denom
        
    def __mul__(self,equa2):
        return (self.num * equa2.num ) / (self.denom * equa2.denom )

def pgcd(a,b):
    if b == 0:
        return a
    else:
        return pgcd(b,b%a)
    
pgcd(17000, 14)
    
a = Fraction(12,35)
b = Fraction(78,35)
c = Fraction(1,2)
