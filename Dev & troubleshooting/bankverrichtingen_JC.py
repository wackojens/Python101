from pcinput import getFloat

class Persoon:

    def __init__(self, voornaam:str, achternaam:str, rijksregisternummer:str):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.rijksregisternummer = rijksregisternummer

    def __repr__(self):
        return f'{self.voornaam} {self.achternaam}'



class Rekening:

    def __init__(self, rekeningnummer:str, persoon):
        self.rekeningnummer = rekeningnummer
        if self.controle() == False:
            print("Geen geldig rekeningnummer aangemaakt!")
            exit()
        self.persoon = persoon
        self.voornaam = persoon.voornaam
        self.achternaam = persoon.achternaam
        self.rijksregisternummer = persoon.rijksregisternummer
        self.geld = 0

    def __repr__(self):
        return f'Rekening van {self.voornaam} {self.achternaam}'

    def controle(self):
        if self.rekeningnummer[3] != '-' or self.rekeningnummer[11] != '-':
            print(f'Het nummer: {self.rekeningnummer} is niet correct ingevoerd. Geef een nummer in zoals volgend voorbeeld: 123-1234567-12')
            exit()
        testNummer = self.rekeningnummer.replace('-', '')
        if len(testNummer) != 12:
            print('Te weinig of te veel cijfers ingegeven.')
            exit()
        try:
            testNummer = int(testNummer)
        except ValueError:
            print('Je rekeningnummer mag geen letters of tekens bevatten! Geef je nummer enkel in zoals volgend voorbeeld: 123-1234567-12')
            exit()
        controlenummer = testNummer % 100
        getal = int((testNummer - controlenummer) / 100)
        check = getal % 97
        if check == 0:
            controlenummer = 0
        return controlenummer == check

    def rekeningOverzicht(self):
        return (f'{self.voornaam} {self.achternaam}, er staat {self.geld}EUR op je rekening.')

    def overschrijven(self, other):
        return NotImplemented



class Zichtrekening(Rekening):

    def overschrijven(self, other):
        if isinstance(other, Rekening):
            if other.controle() and ((isinstance(other, Zichtrekening)) or (isinstance(other, Spaarrekening) and self.persoon == other.persoon)):
                while True:
                    bedrag = getFloat(f"Welk bedrag wilt u overschrijven naar rekening {other.rekeningnummer}? ")
                    if bedrag < 0:
                        print("Het bedrag kan niet negatief zijn!")
                        continue
                    else:
                        self.geld -= bedrag
                        other.geld += bedrag
                        print(f"Bedrag is overgeschreven naar rekening {other.rekeningnummer} van {other.persoon}")
                        break
            else:
                print(f"Overchrijving naar {other.rekeningnummer} niet mogelijk. Het rekeningnummer van de ontvanger is niet geldig / Je kan geen overschrijvingen doen naar spaarrekeningen van andere personen.")
        else:
            return NotImplemented

    def storten(self):
        bedrag = getFloat(f"Welk bedrag wilt u storten op rekening {self.rekeningnummer}? ")
        self.geld += bedrag
        print("Bedrag gestort")

    def opvragen(self):
        bedrag = getFloat("Welk bedrag wilt u opvragen? ")
        self.geld -= bedrag
        print("Vergeet je geld niet uit de lade te nemen")



class Spaarrekening(Rekening):
    
    def overschrijven(self, other):
        if isinstance(other, Zichtrekening):
            if self.persoon == other.persoon and other.controle():
                while True:
                    bedrag = getFloat(f"Welk bedrag wilt u overschrijven naar rekening {other.rekeningnummer}? ")
                    if bedrag > self.geld or bedrag < 0:
                        print('Het bedrag mag niet negatief zijn en mag ook niet hoger zijn dan je saldo!')
                        continue
                    else:
                        self.geld -= bedrag
                        other.geld += bedrag
                        print(f"Bedrag is overgeschreven naar rekening {other.rekeningnummer} van {other.persoon}")
                        break
            else:
                print(f'Overschrijving naar rekening {other.rekeningnummer} niet gelukt. Vanaf je spaarrekening kan je enkel overschrijvingen naar je eigen rekeningen uitvoeren.')
        else:
            return NotImplemented




# Onderstaande input kan gebruikt worden om het programma te testen


ik = Persoon('Jens', 'Coomans', '56465464')
pers = Persoon('J', 'C', '45454545')

test1 = Zichtrekening('000-0000097-97', ik)
test2 = Spaarrekening('000-0000100-03', ik)
test3 = Spaarrekening('091-0122401-16', pers)

print(test1)
print(test2)
print(test3)
print()

print(test1.controle())
print(test2.controle())
print(test3.controle())
print()

print(test1.rekeningOverzicht())
print(test2.rekeningOverzicht())
print(test3.rekeningOverzicht())
print()

test1.storten()
test1.opvragen()
print()

test1.overschrijven(test2)
print()
test1.overschrijven(test3)
print()
test2.overschrijven(test1)
print()
test3.overschrijven(test1)
print()

print(test1.rekeningOverzicht())
print(test2.rekeningOverzicht())
print(test3.rekeningOverzicht())