from pcinput import getInteger, getString, getLetter
from kassaticket_classes_JC import Product, Bestelling, Ticket



mosselen = Product('mosselen', 20)
videe = Product('videe', 10)
drank = Product('drank', 2)
ijs = Product('ijs', 3)



naamBediende = getString('Kassabediende, geef je naam! : ')
kassaBegin = getInteger(naamBediende + ', geef je kassabegin! : ')
while True:
    bestelling = Bestelling(mosselen, videe, drank, ijs)
    inkomsten = bestelling.berekenBedrag()
    print('Bedrag', inkomsten)
    print('Wisselgeld', bestelling.getChange())
    kassaBegin += inkomsten
    if getLetter('Ticket? J/N: ') == 'J':
        Ticket(naamBediende, bestelling)
    if getLetter('Stoppen? J/N:') == 'J':
        print('Bediende: ', naamBediende)
        print('Inhoud kassa: ', kassaBegin)
        break