from random import choice

class Dobbelsteen:
    def __init__(self):
        self.waarden = []
    def __repr__(self):
        return 'Dobbelsteen interface class'
    def rol(self):
        return NotImplemented

class D6 (Dobbelsteen):
    def __init__(self):
        self.waarden = [1,2,3,4,5,6]
    def __repr__(self):
        return '6 zijdige dobbelsteen'
    def rol(self):
        return choice(self.waarden)

class D10(Dobbelsteen):
    def __init__(self):
        self.waarden = [1,2,3,4,5,6,7,8,9,10]
    def __repr__(self):
        return '10 zijdeige dobbelsteen'
    def rol(self):
        return choice(self.waarden)

class D6special(Dobbelsteen):
    def __init__(self):
        self.waarden = [u'\u2691',u'\u2692',u'\u2693',u'\u235E',u'\u233E', u'\u2694'] 
    def __repr__(self):
        return 'speciale 6 zijdige dobbelsteen'
    def rol(self):
        return choice(self.waarden)

#    if __name__ == '__main__':
#        d = Dobbelsteen()
#        print(d)
#        print(d.rol())  # NotImplemented levert geen RunTimeError bij een print
#        d6 = D6()
#        print(d6)
#        for i in range(10):
#            print('rol',i, d6.rol())

if __name__ == '__main__':
    d10 = D10()
    for i in range(10):
        print('rol ', i, d10.rol())
    print()
    d6 = D6special()
    for i in range(10):
        print('rol ', i, d6.rol())