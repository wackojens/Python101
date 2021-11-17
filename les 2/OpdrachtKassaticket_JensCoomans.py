import pcinput
import datetime
now = datetime.datetime.now()
prijsMosselen = 20
prijsKoninginnenhapje = 10
prijsIJs = 3
prijsDrank = 2
korting = 0
tempTotaal = 0
totaalMosselen = pcinput.getInteger('Geef het aantal porties mosselen in: ')
totaalKoninginnenhapje = pcinput.getInteger('Geef het aantal porties koninginnenhapje in: ')
totaalIJs = pcinput.getInteger('Geef het aantal ijsjes in: ')
totaalDrank = pcinput.getInteger('Geef het aantal drankjes in: ')
totaal =(prijsMosselen * totaalMosselen) + (prijsKoninginnenhapje * totaalKoninginnenhapje) + (prijsIJs * totaalIJs) + (prijsDrank * totaalDrank)

if totaalMosselen==0 and totaalKoninginnenhapje==0 and totaalIJs==0 and totaalDrank==0:
    exit()

while True:
    try:
        ontvangen = float(input('Geef ontvangen bedrag in: '))
        break
    except ValueError:
        print('verkeerde input. Geef bedrag opnieuw in')

korting = pcinput.kortingCalculate(totaalMosselen, totaal)
totaalMetKorting = totaal - korting
wisselgeld = ontvangen - totaalMetKorting

while True:
    if wisselgeld<0:
        print('Te weinig betaald. Controleer ontvagen bedrag')
        ontvangen = float(input('Geef ontvangen bedrag in: '))
        wisselgeld = ontvangen - totaalMetKorting
    else:
        break

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

afdrukken = input('Moet er een kassaticket afgedrukt worden? Y/N ')

if afdrukken=='N':
    exit()

print(f"{'Kassaticket':^60}")
print('*'*60)
print(f"{'U werd geholpen door:':<30}{'Jens':>30}")
print(f"{now.strftime('%Y-%m-%d'):<30}{now.strftime('%H:%M:%S'):>30}")
print('*'*60)
print(f"{'Besteld':<28}{'Aantal':<16}{'Bedrag':>16}")
print(f"{'-Mosselen':<30}{totaalMosselen:<15}{totaalMosselen * prijsMosselen:>14.2f}{'€':>1}")
print(f"{'-Koninginnenhapje':<30}{totaalKoninginnenhapje:<15}{totaalKoninginnenhapje * prijsKoninginnenhapje:>14.2f}{'€':>1}")
print(f"{'-IJs':<30}{totaalIJs:<15}{totaalIJs * prijsIJs:>14.2f}{'€':>1}")
print(f"{'-Drank':<30}{totaalDrank:<15}{totaalDrank * prijsDrank:>14.2f}{'€':>1}")
print('='*60)
print(f"{'Totaal te betalen:':<50}{totaal:>9.2f}{'€':>1}")
if korting>0:
    print(f"{'Korting:':<50}{'-':>3}{korting:>6.2f}{'€':>1}")
    print(f"{'Totaal met korting:':<50}{totaalMetKorting:>9.2f}{'€':>1}")
print('-'*60)
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
if totaalMosselen==0 and totaalKoninginnenhapje==0 and totaalIJs==0:
    print(f"{'Gezondheid !!!':^60}")
else:
    print(f"{'Smakelijk eten !!!':^60}")
print('*'*60)