'''Een klant boekt bij een reisorganisatie een reis met keuze uit verschillende opties: bereken de
totale kostprijs voor deze klant met volgende gegevens:

• Vervoer : enkele reis vliegtuig=200€, enkele reis per autocar=50€, zelf met de auto = 0€.
• Hotel: standaardkamer prijs in hotel Zeezicht=30€/nacht/persoon, hotel
Duinenzicht=25€/nacht/persoon.
• Type kamer: zeezicht = supplement van 10%, balkon=+20€/nacht/persoon, luxe suite=+40€/nacht/persoon.
• Aantal nachten: hoeveelheidskorting: 7 +1 nacht gratis, 10+2 nachten gratis. (7=7, 8=7, 9=8,
10=9, 11=10, 12=10, 13=11, ….).
• Aantal personen: aantal volwassenen, kinderen (50% korting op kamerprijs en kamertype
supplement).
• Eten: geen ontbijt, met ontbijt (10€/nacht/persoon), half pension(30€/nacht/persoon), vol pension (40€/nacht/persoon)'''

def getRoomType(prompt1, prompt2, prompt3):
    while True:
        line1 = input(prompt1)
        line1 = line1.strip()
        line1 = line1.lower()

        line2 = input(prompt2)
        line2 = line2.strip()
        line2 = line2.lower()

        line3 = input(prompt3)
        line3 = line3.strip()
        line3 = line3.lower()

        if line1 != 'y' and line1 != 'n' and line2 != 'y' and line2 != 'n' and line3 != 'y' and line3 != 'n':
            print('Geef aub "Y" of "N" in.')
            continue
        else:
            return line1, line2, line3

def getNightsAmount(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('Ongeldige waarde. Geef een cijfer in')
            continue
        return num

def getMeal(prompt, priceMeal1, priceMeal2, priceMeal3, priceMeal4):
    while True:
        line = input(prompt)
        line = line.strip()
        line = line.lower()
        if line != 'geen' and line != 'ontbijt' and line != 'half' and line != 'vol':
            print('ongeldige keuze. Geef type maaltijd opnieuw in.')
            continue
        if line == 'ontbijt':
            return priceMeal2, 'ontbijt'
        elif line == 'half':
            return priceMeal3, 'half pension'
        elif line == 'vol':
            return priceMeal4, 'vol pension'
        else:
            return priceMeal1, 'geen ontbijt'

def getTransport(prompt, vehicle1, vehicle2, vehicle3):
    while True:
        line = input(prompt)
        line = line.strip()
        line = line.lower()
        if line != 'vliegtuig' and line != 'autocar' and line != 'zelf':
            print('Ongeldige keuze. Geef vervoer opnieuw in.')
            continue
        if line == 'vliegtuig':
            return vehicle1, 'vliegtuig'
        elif line == 'autocar':
            return vehicle2, 'autocar'
        else:
            return vehicle3, 'zelf'

def getAccomodation(prompt, priceHotel1, priceHotel2):
    while True:
        line = input(prompt)
        line = line.strip()
        line = line.lower()
        if line != 'zeezicht' and line != 'duinenzicht':
            print('Ongeldige keuze. Geef accomodatie opnieuw in.')
            continue
        if line == 'zeezicht':
            return priceHotel1, 'zeezicht'
        else:
            return priceHotel2, 'duinenzicht'

def getPeopleAmountAge(prompt1, prompt2):
    while True:
        try:
            num1 = int(input(prompt1))
            num2 = int(input(prompt2))
        except ValueError:
            print('Ongeldige waarde. Geef een cijfer in')
            continue
        return num1, num2

def getNightsDiscount(nightAmount, singleNightDiscount, doubleNightDiscount):
    if nightAmount > singleNightDiscount and nightAmount < (doubleNightDiscount + 2):
        discount = 1
        nightAmount -= discount
        return nightAmount, discount
    elif nightAmount >= (doubleNightDiscount + 2):
        discount = 2
        nightAmount -= discount
        return nightAmount, discount
    else:
        discount = 0
        return nightAmount, discount

def getOneNightPrice(hotelPrice, mealPrice, sup1, sup2, sup3, sup1Price, sup2Price, sup3Price):
    if sup1 == 'n':
        sup1Price = 0
    if sup2 == 'n':
        sup2Price = 0
    if sup3 == 'n':
        sup3Price = 0
    oneNight = (hotelPrice + mealPrice + sup2Price + sup3Price) * (1 + sup1Price / 100)
    return oneNight