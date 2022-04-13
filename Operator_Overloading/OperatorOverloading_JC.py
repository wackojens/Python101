class Rechthoek:
    def __init__(self, startPunt, breedte, hoogte):
        self.sPunt = startPunt
        self.breedte = abs(breedte)
        self.hoogte = abs(hoogte)
    
    def getSurface(self):
        return self.breedte * self.hoogte

    def __eq__(self, otherRhoek):
        if isinstance(otherRhoek, Rechthoek):
            return self.breedte == otherRhoek.breedte and self.hoogte == otherRhoek.hoogte
        return NotImplemented

    def __gt__(self, otherRhoek):
        if isinstance(otherRhoek, Rechthoek):
            return self.getSurface() > otherRhoek.getSurface()
        return NotImplemented

    def __lt__(self, otherRhoek):
        if isinstance(otherRhoek, Rechthoek):
            return self.getSurface() < otherRhoek.getSurface()
        return NotImplemented



class Punt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mul__(self, other):
        if isinstance(other, Punt):
            return self.x * other.y, self.y * other.x
        elif isinstance(other, int):
            return self.x * other, self.y * other
        return NotImplemented



p1 = Punt(1,1)
p2 = Punt(5,5)
p3 = Punt(10,10)

r1 = Rechthoek(p1, 10, 10)
r2 = Rechthoek(p2, 10, 10)
r3 = Rechthoek(p3, 9, 9)
r4 = Rechthoek(p1, 11, 11)

# True rechthoek operatoren
print(r1 == r2)
print(r1 > r3)
print(r1 < r4)
print(r3 < r4)
print()

# False rechthoek operatoren
print(r1 == r3)
print(r1 > r4)
print(r1 < r3)
print(r2 == r4)
print()

# vermenigvuldigen punten
print(p1 * p2)
print(p1 * 5)
print(p1 * p3)
print(p2 * p3)