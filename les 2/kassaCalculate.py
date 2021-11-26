def berekenMuntstukken(bedrag, muntstuk):
    aantal = 0
    aantal = bedrag // muntstuk
    bedrag = bedrag % muntstuk
    return int(aantal), round(bedrag, 2)

def muntenWisselgeld(aantal, muntstuk):
    if aantal >0:
        print(aantal, end=' ')
        if muntstuk>=5:
            print('Briefje(s) van', ' ', muntstuk, 'EUR', sep='')
        else:
            print('munt(en) van', ' ', muntstuk, 'EUR', sep='')

def kortingCalculate(aantalMosselen, kostprijs):
    discount = 0
    if aantalMosselen>=2 and kostprijs>=150:
        discount = 20
    elif aantalMosselen>=2 and kostprijs<150 and kostprijs>=100:
        discount = 10
    elif aantalMosselen>=2 and kostprijs<100 and kostprijs>=50:
        discount = 5
    return discount