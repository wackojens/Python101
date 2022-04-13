from pcinput import getInteger,getString, getLetter
import pickle

class Bestelling:
    def __init__(self):
        self.PRIJSMOSSELEN = 20
        self.PRIJSVIDEE = 10
        self.PRIJSDRANK = 2
        self.PRIJSIJS = 3
        self.aantalMosselen = self.getAantal("Geef het aantal mosselen: ")
        self.aantalVidee = self.getAantal("Geef het aantal videe: ")
        self.aantalDrank = self.getAantal("Geef het aantal drank: ")
        self.aantalIjs = self.getAantal("Geef het aantal ijs: ")
        self.bedrag = self.berekenBedrag()


    def getAantal(self,strPrompt):
        aantal = getInteger(strPrompt)
        return aantal

    def berekenBedrag(self):
        self.bedragMosselen = self.aantalMosselen * self.PRIJSMOSSELEN
        self.bedragVidee = self.aantalVidee * self.PRIJSVIDEE
        self.bedragDrank = self.aantalDrank * self.PRIJSDRANK
        self.bedragIjs = self.aantalIjs * self.PRIJSIJS
        return self.bedragMosselen + self.bedragVidee + self.bedragDrank + self.bedragIjs

naamBediende = getString('Kassabediende, geef je naam! : ')
kassaBegin = getInteger(naamBediende + ', geef je kassabegin! : ')
while True:
    bestelling = Bestelling()
    print('Bedrag', bestelling.bedrag)

    try:
        inputbestand = open('bestelling.nr', 'rb')  # rb is read binary
        bestelnummer = pickle.load(inputbestand)
        inputbestand.close()
    except:
        bestelnummer = 1

    # schrijven bestelling


    bestelnummer += 1
    outputbestand = open('bestelling.nr','wb')     #wb is write binair
    pickle.dump(bestelnummer, outputbestand )
    outputbestand.close()


    if getLetter('Stoppen? J/N:') == 'J':
        break

