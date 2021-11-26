#Imports
import pcinput
import kassaCalculate
import datetime

muntstukken = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
now = datetime.datetime.now()
prijsMosselen = 20
prijsKoninginnenhapje = 10
prijsIJs = 3
prijsDrank = 2

#Bediende en staat kassa vragen
print()
bediende = pcinput.getString('Geef de naam van de bediende in: ')
inhoudKassa = pcinput.getFloat('Geef de inhoud van de kassa in: ')
print()

#Start loop
while True:

    #Bestelling ingeven + controle op foutieve bestelling
    aantalMosselen = pcinput.getInteger('Geef het aantal porties mosselen in: ')
    aantalKoninginnenhapje = pcinput.getInteger('Geef het aantal porties koninginnenhapje in: ')
    aantalIJs = pcinput.getInteger('Geef het aantal ijsjes in: ')
    aantalDrank = pcinput.getInteger('Geef het aantal drankjes in: ')

    while aantalMosselen == 0 and aantalKoninginnenhapje == 0 and aantalIJs == 0 and aantalDrank == 0:
        print('Geen bestelling geplaatst. Begin opnieuw of stop het programma.')
        end = pcinput.getLetter('Wil je stoppen? (Y/N): ')

        if end != 'Y' and end != 'N':
            print('verkeerde input. Geef keuze opnieuw in')
        elif end == 'N':
            aantalMosselen = pcinput.getInteger('Geef het aantal porties mosselen in: ')
            aantalKoninginnenhapje = pcinput.getInteger('Geef het aantal porties koninginnenhapje in: ')
            aantalIJs = pcinput.getInteger('Geef het aantal ijsjes in: ')
            aantalDrank = pcinput.getInteger('Geef het aantal drankjes in: ')
        else:
            print()
            print('Bediende:', bediende)
            print('De kassa heeft nu ', inhoudKassa, 'EUR', ' inhoud', sep='')
            print()
            exit()

    print()

    #Totaal zonder korting berekenen
    totaal =(prijsMosselen * aantalMosselen) + (prijsKoninginnenhapje * aantalKoninginnenhapje) + (prijsIJs * aantalIJs) + (prijsDrank * aantalDrank)

    #Korting berekenen en totaal met korting weergeven
    korting = 0
    korting = kassaCalculate.kortingCalculate(aantalMosselen, totaal)
    totaalMetKorting = totaal - korting

    print('Er moet ', float(totaalMetKorting), 'EUR betaald worden.', sep='')
    print()

    #Ontvangen bedrag ingeven + controle
    while True:
        try:
            ontvangen = pcinput.getFloat('Geef ontvangen bedrag in: ')
            break
        except ValueError:
            print('verkeerde input. Geef bedrag opnieuw in')

    #Wisselgeld berekenen + controle ontvangst
    wisselgeld = ontvangen - totaalMetKorting

    while True:
        if wisselgeld < 0:
            print('Te weinig betaald. Controleer ontvagen bedrag')
            ontvangen = pcinput.getFloat('Geef ontvangen bedrag in: ')
            wisselgeld = ontvangen - totaalMetKorting
        else:
            break

    #Ontvangen bedrag en wisselgeld weergeven
    print('Je hebt ', ontvangen, 'EUR ontvangen', sep='')
    print()
    print('Er moet ', wisselgeld, 'EUR teruggegeven worden', sep='')

    #Berekenen coupures wisselgeld en print
    kassaCalculate.changeNotes(muntstukken, wisselgeld)
    print()

    #Inhoud kassa berekenen
    inhoudKassa = inhoudKassa + ontvangen - wisselgeld

    #Ticket printen(Y/N) + controle
    while True:
        afdrukken = pcinput.getLetter('Moet er een kassaticket afgedrukt worden? Y/N ')
        print()
        if afdrukken != 'Y' and afdrukken != 'N':
            print('Verkeerde input. Geef keuze opnieuw in.')
        elif afdrukken == 'N':
            break
        else:

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

            if korting > 0:
                print(f"{'Korting:':<50}{'-':>3}{korting:>6.2f}{'€':>1}")
                print(f"{'Totaal met korting:':<50}{totaalMetKorting:>9.2f}{'€':>1}")
            print('-'*60)

            #Hoeveelheid betaald en wisselgeld
            print(f"{'Betaald:':<50}{ontvangen:>9.2f}{'€':>1}")
            print(f"{'Wisselgeld:':<50}{wisselgeld:>9.2f}{'€':>1}")
            print('*'*60)

            #Smakelijk of gezondheid
            if aantalMosselen == 0 and aantalKoninginnenhapje == 0 and aantalIJs == 0:
                print(f"{'Gezondheid !!!':^60}")
            else:
                print(f"{'Smakelijk eten !!!':^60}")
                print('*'*60)

            break

    #Volgende bestelling of stoppen + controle
    while True:
        print()
        end = pcinput.getLetter('Wil je stoppen? (Y/N): ')
        if end != 'Y' and end != 'N':
            print('Verkeerde input. Geef keuze opnieuw in.')
        elif end == 'Y':
            print()
            print('Bediende:', bediende)
            print('De kassa heeft nu ', inhoudKassa, 'EUR', ' inhoud', sep='')
            print()
            exit()
        else:
            print()
            break