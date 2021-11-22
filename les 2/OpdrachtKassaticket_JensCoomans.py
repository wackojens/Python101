#Imports
import pcinput
import datetime

#Datum en prijzen per eenheid
now = datetime.datetime.now()
prijsMosselen = 20
prijsKoninginnenhapje = 10
prijsIJs = 3
prijsDrank = 2
dishes = ['Mosselen', 'Koninginnenhapje', 'IJs', 'Drank']

#Bediende en staat kassa vragen
bediende = pcinput.getString('Geef de naam van de bediende in: ')
inhoudKassa = pcinput.getFloat('Geef de inhoud van de kassa in: ')

#Start loop
end = 'N'
while end == 'N':

    #test
    for dish in dishes:
        dish = pcinput.dishAmount
    
    print(dishes)
    exit()

    #Bestelling ingeven + controle op foutieve bestelling
    aantalMosselen = pcinput.getInteger('Geef het aantal porties mosselen in: ')
    aantalKoninginnenhapje = pcinput.getInteger('Geef het aantal porties koninginnenhapje in: ')
    aantalIJs = pcinput.getInteger('Geef het aantal ijsjes in: ')
    aantalDrank = pcinput.getInteger('Geef het aantal drankjes in: ')

    while aantalMosselen==0 and aantalKoninginnenhapje==0 and aantalIJs==0 and aantalDrank==0:
        print('Geen bestelling geplaatst. Begin opnieuw of stop het programma.')
        end = pcinput.getLetter('Wil je stoppen? (Y/N): ')
        if end == 'N':
            aantalMosselen = pcinput.getInteger('Geef het aantal porties mosselen in: ')
            aantalKoninginnenhapje = pcinput.getInteger('Geef het aantal porties koninginnenhapje in: ')
            aantalIJs = pcinput.getInteger('Geef het aantal ijsjes in: ')
            aantalDrank = pcinput.getInteger('Geef het aantal drankjes in: ')
        else:
            print('Bediende:', bediende)
            print('De kassa heeft nu ', inhoudKassa, 'EUR', ' inhoud', sep='')
            exit()

    #Totaal zonder korting berekenen
    totaal =(prijsMosselen * aantalMosselen) + (prijsKoninginnenhapje * aantalKoninginnenhapje) + (prijsIJs * aantalIJs) + (prijsDrank * aantalDrank)

    #Korting berekenen en totaal met korting weergeven
    korting = 0
    korting = pcinput.kortingCalculate(aantalMosselen, totaal)
    totaalMetKorting = totaal - korting

    print('Er moet ', totaalMetKorting, 'EUR betaald worden.', sep='')

    #Ontvangen bedrag ingeven
    while True:
        try:
            ontvangen = pcinput.getFloat('Geef ontvangen bedrag in: ')
            break
        except ValueError:
            print('verkeerde input. Geef bedrag opnieuw in')

    #Hoeveelheid wisselgeld en controle ontvangst
    wisselgeld = ontvangen - totaalMetKorting

    while True:
        if wisselgeld<0:
            print('Te weinig betaald. Controleer ontvagen bedrag')
            ontvangen = pcinput.getFloat('Geef ontvangen bedrag in: ')
            wisselgeld = ontvangen - totaalMetKorting
        else:
            break
    
    #Inhoud kassa berekenen
    inhoudKassa = inhoudKassa + ontvangen - wisselgeld

    #Berekenen coupures wisselgeld
    totaal500, rest = pcinput.berekenMuntstukken(wisselgeld, 500)
    totaal200, rest = pcinput.berekenMuntstukken(rest, 200)
    totaal100, rest = pcinput.berekenMuntstukken(rest, 100)
    totaal50, rest = pcinput.berekenMuntstukken(rest, 50)
    totaal20, rest = pcinput.berekenMuntstukken(rest, 20)
    totaal10, rest = pcinput.berekenMuntstukken(rest, 10)
    totaal5, rest = pcinput.berekenMuntstukken(rest, 5)
    totaal2, rest = pcinput.berekenMuntstukken(rest, 2)
    totaal1, rest = pcinput.berekenMuntstukken(rest, 1)
    totaal50C, rest = pcinput.berekenMuntstukken(rest, 0.50)
    totaal20C, rest = pcinput.berekenMuntstukken(rest, 0.20)
    totaal10C, rest = pcinput.berekenMuntstukken(rest, 0.10)
    totaal5C, rest = pcinput.berekenMuntstukken(rest, 0.05)
    totaal2C, rest = pcinput.berekenMuntstukken(rest, 0.02)
    totaal1C, rest = pcinput.berekenMuntstukken(rest, 0.01)

    #Ticket printen
    afdrukken = pcinput.getLetter('Moet er een kassaticket afgedrukt worden? Y/N ')

    if afdrukken=='N':
        continue

#Ticket afdrukken
    #Titel
    print(f"{'Kassaticket':^60}")
    print('*'*60)

    #Bediende en datum
    print(f"{'U werd geholpen door:':<30}{bediende:>30}")
    print(f"{now.strftime('%Y-%m-%d'):<30}{now.strftime('%H:%M:%S'):>30}")
    print('*'*60)

    #Bestelling
    print(f"{'Besteld':<28}{'Aantal':<16}{'Bedrag':>16}")
    print(f"{'-Mosselen':<30}{aantalMosselen:<15}{aantalMosselen * prijsMosselen:>14.2f}{'€':>1}")
    print(f"{'-Koninginnenhapje':<30}{aantalKoninginnenhapje:<15}{aantalKoninginnenhapje * prijsKoninginnenhapje:>14.2f}{'€':>1}")
    print(f"{'-IJs':<30}{aantalIJs:<15}{aantalIJs * prijsIJs:>14.2f}{'€':>1}")
    print(f"{'-Drank':<30}{aantalDrank:<15}{aantalDrank * prijsDrank:>14.2f}{'€':>1}")
    print('='*60)

    #Totaal en korting
    print(f"{'Totaal te betalen:':<50}{totaal:>9.2f}{'€':>1}")
    if korting>0:
        print(f"{'Korting:':<50}{'-':>3}{korting:>6.2f}{'€':>1}")
        print(f"{'Totaal met korting:':<50}{totaalMetKorting:>9.2f}{'€':>1}")
    print('-'*60)

    #Hoeveelheid betaald en wisselgeld
    print(f"{'Betaald:':<50}{ontvangen:>9.2f}{'€':>1}")
    print(f"{'Wisselgeld:':<50}{wisselgeld:>9.2f}{'€':>1}")
    pcinput.muntenWisselgeld(totaal500, 500)
    pcinput.muntenWisselgeld(totaal200, 200)
    pcinput.muntenWisselgeld(totaal100, 100)
    pcinput.muntenWisselgeld(totaal50, 50)
    pcinput.muntenWisselgeld(totaal20, 20)
    pcinput.muntenWisselgeld(totaal10, 10)
    pcinput.muntenWisselgeld(totaal5, 5)
    pcinput.muntenWisselgeld(totaal2, 2)
    pcinput.muntenWisselgeld(totaal1, 1)
    pcinput.muntenWisselgeld(totaal50C, 0.50)
    pcinput.muntenWisselgeld(totaal20C, 0.20)
    pcinput.muntenWisselgeld(totaal10C, 0.10)
    pcinput.muntenWisselgeld(totaal5C, 0.05)
    pcinput.muntenWisselgeld(totaal2C, 0.02)
    pcinput.muntenWisselgeld(totaal1C, 0.01)
    print('*'*60)

    #Smakelijk of gezondheid
    if aantalMosselen==0 and aantalKoninginnenhapje==0 and aantalIJs==0:
        print(f"{'Gezondheid !!!':^60}")
    else:
        print(f"{'Smakelijk eten !!!':^60}")
    print('*'*60)

    #Volgende bestelling of stoppen
    end = pcinput.getLetter('Wil je stoppen? (Y/N): ')
    if end == 'Y':
        print('Bediende:', bediende)
        print('De kassa heeft nu ', inhoudKassa, 'EUR', ' inhoud', sep='')