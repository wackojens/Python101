import pcinput, kassaCalculate, printTicket

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

    totaal, korting, totaalMetKorting = kassaCalculate.getTotalDiscount(aantalGerechten, prijzen)
    wisselgeld, ontvangen = kassaCalculate.getChange(totaalMetKorting)

    kassaCalculate.getChangeNotes(muntstukken, wisselgeld)

    inhoudKassa = inhoudKassa + ontvangen - wisselgeld

    printTicket.askTicket(bediende, gerechten, aantalGerechten, prijzen, totaal, korting, totaalMetKorting, ontvangen, wisselgeld)

    kassaCalculate.endRegister(bediende, inhoudKassa)