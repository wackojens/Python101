class Punt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y



class Rechthoek:
    def __init__(self, startPunt, breedte, hoogte):
        self.sPunt = startPunt
        self.breedte = abs(breedte)
        self.hoogte = abs(hoogte)
    
    def __repr__(self):
        return f'Links boven: {self.sPunt.x,self.sPunt.y}, B: {self.breedte}, H: {self.hoogte}'

    def getRightLowerCorner(self):
        self.rechtsOnderX = self.sPunt.x + self.breedte
        self.rechtsOnderY = self.sPunt.y + self.hoogte
        puntRO = Punt(self.rechtsOnderX, self.rechtsOnderY)
        return puntRO
    
    def getCircumference(self):
        return f'Omtrek = {(self.breedte + self.hoogte) * 2}'
    
    def getSurface(self):
        return f'Oppervlakte = {self.breedte * self.hoogte}'

    def getOverlay(self, other):
        self.lowX = self.sPunt.x
        self.highX = self.sPunt.x + self.breedte
        self.lowY = self.sPunt.y
        self.highY = self.sPunt.y + self.hoogte

        other.lowX = other.sPunt.x
        other.highX = other.sPunt.x + other.breedte
        other.lowY = other.sPunt.y
        other.highY = other.sPunt.y + other.hoogte

        if min(self.highX, other.highX) > max(self.lowX, other.lowX):

            overlayLB = (max(self.lowX, other.lowX), max(self.lowY, other.lowY))
            overlayRB = (min(self.highX, other.highX), max(self.lowY, other.lowY))
            overlayLO = (max(self.lowX, other.lowX), min(self.highY, other.highY))
            overlayRO = (min(self.highX, other.highX), min(self.highY, other.highY))

            overlayBreedte = (min(self.highX, other.highX) - max(self.lowX, other.lowX))
            overlayHoogte = (min(self.highY, other.highY) - max(self.lowY, other.lowY))

            overlayOmtrek = (overlayHoogte + overlayBreedte) * 2

            overlayOpp = overlayHoogte * overlayBreedte

            return (f'Hoekpunten overlappende zone = {overlayLB, overlayRB, overlayLO, overlayRO}\n'
                    f'Omtrek overlappende zone = {overlayOmtrek}\n'
                    f'Oppervlakte overlappende zone = {overlayOpp}')
        
        else:
            return 'Geen overlapping'



p1 = Punt(1,1)
p2 = Punt(0,0)

r1 = Rechthoek(p1, 9, 4)
r2 = Rechthoek(p2, 15, 9)

p3 = r1.getRightLowerCorner()

print(p3.x, p3.y)
print(r1.getCircumference())
print(r1.getSurface())
print(r1.getOverlay(r2))