from pcinput import getInteger, getString, getLetter
from kassaticket_classes_JC import Product, Bestelling
import pickle



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



    if getLetter('Ticket? J/N: ') == 'J':
        bestelling.getTicket(naamBediende, bestelnummer)
    if getLetter('Stoppen? J/N:') == 'J':
        print('Bediende: ', naamBediende)
        print('Inhoud kassa: ', kassaBegin)
        break