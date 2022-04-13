import reisbureauFunction

#Vaste gegevens
kortingKinderen = 50
hotelZeezicht = 30
hotelDuinenzicht = 25
supplementZeezicht = 10
supplementBalkon = 20
supplementSuite = 40
geenMaaltijd = 0
ontbijt = 10
halfPension = 30
volPension = 40
prijsVliegtuig = 200
prijsAutocar = 50
prijsZelf = 0
kortingNachten1 = 7
kortingNachten2 = 10

#Input keuzes
print()
volwassenen, kinderen= reisbureauFunction.getPeopleAmountAge('Geef het aantal volwassenen: ', 'Geef het aantal kinderen: ')
aantalNachten = reisbureauFunction.getNightsAmount('Geef het aantal nachten in: ')
prijsHotel, hotel = reisbureauFunction.getAccomodation('Geef keuze hotel in.(zeezicht of duinenzicht): ', hotelZeezicht, hotelDuinenzicht)
zeezicht, balkon, suite = reisbureauFunction.getRoomType('Kamer met zeezicht?(Y/N) ', 'Kamer met balkon?(Y/N) ', 'Luxe suite?(Y/N) ')
prijsMaaltijd, maaltijd = reisbureauFunction.getMeal('Geef keuze maaltijd in.(Geen, Ontbijt, Half of Vol) ', geenMaaltijd, ontbijt, halfPension, volPension)
prijsVervoer, vervoer = reisbureauFunction.getTransport('Geef het type transport in.(vliegtuig, autocar of zelf): ', prijsVliegtuig, prijsAutocar, prijsZelf)

#berekeningen prijzen etc
totaalPersonen = volwassenen + kinderen
totaalNachten, gratisNachten = reisbureauFunction.getNightsDiscount(aantalNachten, kortingNachten1, kortingNachten2)
totaalPerNacht = reisbureauFunction.getOneNightPrice(prijsHotel, prijsMaaltijd, zeezicht, balkon, suite, supplementZeezicht, supplementBalkon, supplementSuite)
hotelVolwassenen = totaalPerNacht * totaalNachten * volwassenen
hotelKinderen = totaalPerNacht * totaalNachten * kinderen * (kortingKinderen / 100)
totaalHotel = hotelVolwassenen + hotelKinderen
totaalVervoer = prijsVervoer * 2 * totaalPersonen
totaalPrijs = totaalVervoer + totaalHotel

#printen
print()
print('Uw aantal personen is', totaalPersonen, 'met', volwassenen, 'volwassenen en', kinderen, 'kinderen')
print('U gaat', aantalNachten, 'nachten op vakantie en moet', totaalNachten, 'nachten betalen. U heeft dus', gratisNachten, 'nacht(en) gratis')
print('Uw hotelkeuze is', hotel, 'en kost', prijsHotel, 'euro per nacht.')
print('Uw gekozen supplementen zijn "zeezicht?"', zeezicht, '"balkon?"', balkon, '"luxe suite?"', suite)
print('Uw maaltijdkeuze is', maaltijd, 'en kost', prijsMaaltijd, 'per nacht.')
print('Uw vervoerskeuze is:', vervoer, 'en kost', totaalVervoer, 'euro')
print('Het hotel kost', totaalPerNacht, 'euro per nacht')
print('Het hotel kost', round(hotelVolwassenen,2), 'voor de volwassenen en', round(hotelKinderen,2), 'voor de kinderen. Het totaal is', round(totaalHotel,2))
print('De totale prijs is: ', totaalPrijs)