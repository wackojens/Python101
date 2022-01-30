import datetime
from pcinput import getFloat, getInteger



class Product:
    def __init__(self, naam: str, prijs: float):
        self.naam = naam
        self.prijs = prijs
    
    def print(self):
        print(f"{self.naam}    {self.prijs}")



class Bestelling:
    def __init__(self, *args):
        self.products = {}
        self.getAantal(args)
        self.bedrag = 0
        self.korting = 0
        self.totaal = 0
        self.ontvangen = 0
        self.wisselgeld = 0

    def getAantal(self, gerechten):
        while True:
            teller = 0
            for product in gerechten:
                aantal = getInteger(f'Geef het aantal {product.naam}: ')
                self.products[product.naam] = { 'product' : product, 'aantal' : aantal}
                if aantal == 0:
                    teller += 1
            if teller == len(self.products):
                print('Geen bestelling geplaatst, Probeer opnieuw.')
            else:
                break

    def berekenBedrag(self):
        for product in self.products:
            self.bedrag += self.products[product]['product'].prijs * self.products[product]['aantal']
        self.getKorting()
        return self.totaal

    def getKorting(self):
        if 'mosselen' in self.products and self.products['mosselen']['aantal'] >= 2:
            if self.bedrag >= 150:
                self.korting = 20
            elif self.bedrag >= 100:
                self.korting = 10
            elif self.bedrag >= 50:
                self.korting = 5
        self.totaal = round(self.bedrag - self.korting, 2)

    def getChange(self):
        while True:
            self.ontvangen = getFloat('Geef ontvangen bedrag: ')
            self.wisselgeld = round(self.ontvangen - self.totaal, 2)
            if self.wisselgeld < 0:
                print('Te weinig betaald. Controleer ontvangen bedrag.')
                continue
            else:
                print('Ontvangen: ', self.ontvangen)
                return self.wisselgeld

    def getTicket(self, bediende, bestelnum):
        besteld = []
        self.bediende = bediende
        self.bestelnum = bestelnum
        now = datetime.datetime.now()
        print(f"{'Kassaticket':^60}")
        print('*'*60)
        print(f'{self.bestelnum:^60}')
        print('-'*60)
        print(f"{'U werd geholpen door:':<30}{self.bediende:>30}")
        print(f"{now.strftime('%d-%m-%Y'):<30}{now.strftime('%H:%M:%S'):>30}")
        print('*'*60)
        print(f"{'Besteld':<28}{'Aantal':<16}{'Bedrag':>16}")
        for product in self.products:
            if self.products[product]['aantal'] > 0:
                besteld.append(self.products[product]['product'].naam)
                print(f"{'-':<1}{self.products[product]['product'].naam:<29}{self.products[product]['aantal']:<15}{self.products[product]['aantal'] * self.products[product]['product'].prijs:>14.2f}{'€':>1}")
        print('='*60)
        print(f"{'Totaal te betalen:':<50}{self.bedrag:>9.2f}{'€':>1}")
        if self.korting > 0:
            print(f"{'Korting:':<50}{'-':>3}{self.korting:>6.2f}{'€':>1}")
            print(f"{'Totaal met korting:':<50}{self.totaal:>9.2f}{'€':>1}")
        print('-'*60)
        print(f"{'Betaald:':<50}{self.ontvangen:>9.2f}{'€':>1}")
        print(f"{'Wisselgeld:':<50}{self.wisselgeld:>9.2f}{'€':>1}")
        print('*'*60)
        if 'drank' in besteld and len(besteld) == 1:
            print(f"{'Gezondheid !!!':^60}")
        else:
            print(f"{'Smakelijk eten !!!':^60}")
        print('*'*60)
        print()