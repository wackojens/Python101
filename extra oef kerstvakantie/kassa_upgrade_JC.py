import pcinput, kassa_upgrade_JC_Funct

bediende = pcinput.getString('Geef de naam van de bediende in: ')
inhoudKassa = pcinput.getFloat('Geef de inhoud van de kassa in: ')
gerechten = kassa_upgrade_JC_Funct.getProducts()

while True:
    kassa_upgrade_JC_Funct.printProducts(gerechten)
    bestelling, gerechten = kassa_upgrade_JC_Funct.getOrder(gerechten)
    totaal = kassa_upgrade_JC_Funct.printOrder(bestelling)
    wisselgeld, ontvangen = kassa_upgrade_JC_Funct.getChange(totaal)
    inhoudKassa += (ontvangen - wisselgeld)
    kassa_upgrade_JC_Funct.getChangeNotes(wisselgeld)
    kassa_upgrade_JC_Funct.printTicket(bestelling, totaal, ontvangen, wisselgeld)
    kassa_upgrade_JC_Funct.endRegister(bediende, inhoudKassa, gerechten)