import math

class Punt:
    def __init__(self, x=0, y=0, colour=(0,0,0)):
        self.x = x
        self.y = y
        self.colour = colour

    def __repr__(self):
        return (f'(<Punt> x:{self.x}, y:{self.y}, colour:{self.colour})')

    def __str__(self):
        return (f'(De class <Punt> ontvangt 3 argumenten x:({self.x}), y:({self.y}) en colour:({self.colour}) die de coördinaten\n'
        'van een punt op een oppervlakte en de kleur van het punt beschrijven)')

    def afstandTotOorsprong(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def translatie(self,deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY

    def spiegelOverX(self):
        self.y *= -1

    def spiegelOverY(self):
        self.x *= -1

    def spiegel(self):
        self.spiegelOverY()
        self.spiegelOverX()


'''
p = Punt(4,8,(100,255,150))

print(p)                        #Print de __str__ functie(method) indien deze gedefinieerd is. Print anders de __repr__ functie. Indien beide functies niet gedefinieerd zijn print het iets in de aard van: <__main__.Punt object at 0x0000027A1D113FD0>
print([p])                      #Print de __repr__ functie. Indien deze niet gedefineerd is print het iets in de aard van: <__main__.Punt object at 0x0000027A1D113FD0>
print(p.__repr__())             #Print de gevraagde method(functie)(in dit geval __repr__) 
print(p.x)                      #Print de waarde van het 'x' attribuut
print(p.y)                      #Print de waarde van het 'y' attribuut
print(p.colour)                 #Print de waarde van het 'colour' attribuut
print(p.afstandTotOorsprong())  #Print de afstand van de oorsprong (0,0) tot aan het punt(p). Stelling van pythagoras!
p.translatie(5,5)               #Verplaatst het punt met de gegeven values
print([p])
p.spiegelOverX()                #Spiegelt het punt over de x-as
print([p])
p.spiegelOverY()                #Spiegelt het punt over de y-as
print([p])
p.spiegel()                     #Spiegelt het punt over de x en y-as
print([p])
'''

'''
class Rechthoek:
    def __init__(self, startPunt, breedte, hoogte):
        self.xy = startPunt
        self.breedte = breedte
        self.hoogte = hoogte
    
    def __repr__(self):
        return f'Links boven: {self.xy.x,self.xy.y}, B: {self.breedte}, H: {self.hoogte}'

    def getCorners(self):
        self.LB = (self.sPunt.x, self.sPunt.y)
        self.LO = (self.sPunt.x, self.sPunt.y + self.hoogte)
        self.RB = (self.sPunt.x + self.breedte, self.sPunt.y)
        self.RO = (self.sPunt.x + self.breedte, self.sPunt.y + self.hoogte)
        return f'{self.LB}, {self.LO}, {self.RB}, {self.RO}'

p = Punt(4,4)
r = Rechthoek(p, 10, 3)
print(r)
print(r.hoekPunten())
'''



class Rechthoek:
    def __init__(self, puntLBH, puntROH):
        self.LBH = puntLBH
        self.ROH = puntROH

    def getSize(self):
        self.breedte = self.ROH.x - self.LBH.x
        self.hoogte = self.ROH.y - self.LBH.y
        return f'Breedte = {abs(self.breedte)}, Hoogte = {abs(self.hoogte)}'

    def translatie(self, deltaX, deltaY):
        self.LBH.translatie(deltaX, deltaY)
        self.ROH.translatie(deltaX, deltaY)

pLBH = Punt(0,0)
pROH = Punt(12,18)

r = Rechthoek(pLBH, pROH)

print(r.getSize())
print((r.LBH.x,r.LBH.y))
print((r.ROH.x,r.ROH.y))
r.translatie(5,5)
print((r.LBH.x,r.LBH.y))
print((r.ROH.x,r.ROH.y))