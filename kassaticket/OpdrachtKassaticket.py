import pcinput
import kassaCalculate
import printTicket

muntstukken = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
gerechten = ['mosselen', 'koninginnenhapje', 'ijs', 'drank']
prijzen = [20, 10, 3, 2]
aantalGerechten = []
korting = 0

print()
bediende = pcinput.getString('Geef de naam van de bediende in: ')
inhoudKassa = pcinput.getFloat('Geef de inhoud van de kassa in: ')
print()

while True:

    kassaCalculate.getValidOrder(gerechten, aantalGerechten, bediende, inhoudKassa)
    print()

    totaal, korting, totaalMetKorting = kassaCalculate.getTotalDiscount(aantalGerechten, prijzen)
    print('Er moet ', float(totaalMetKorting), 'EUR betaald worden.', sep='')
    print()

    ontvangen = pcinput.getFloat('Geef ontvangen bedrag in: ')
    wisselgeld = kassaCalculate.getChange(totaalMetKorting, ontvangen)
    print('Je hebt ', ontvangen, 'EUR ontvangen', sep='')
    print()
    print('Er moet ', round(wisselgeld, 2), 'EUR teruggegeven worden', sep='')

    kassaCalculate.getChangeNotes(muntstukken, wisselgeld)
    print()

    inhoudKassa = inhoudKassa + ontvangen - wisselgeld

    while True:
        afdrukken = pcinput.getLetter('Moet er een kassaticket afgedrukt worden? Y/N ')
        print()
        if afdrukken != 'Y' and afdrukken != 'N':
            print('Verkeerde input. Geef keuze opnieuw in.')
        elif afdrukken == 'N':
            break
        else:
            printTicket.printTicket(bediende, gerechten, aantalGerechten, prijzen, totaal, korting, totaalMetKorting, ontvangen, wisselgeld)
            break

    while True:
        print()
        kassaCalculate.endRegister(bediende, inhoudKassa)
        break