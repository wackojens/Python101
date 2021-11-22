def getFloat( prompt ):
    while True:
        try:
            num = float( input( prompt ) )
        except ValueError:
            print( "That is not a number -- please try again" )
            continue
        return num

def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num

def getString( prompt ):
    line = input( prompt )
    return line.strip()

def getLetter( prompt ):
    while True:
        line = input( prompt )
        line = line.strip()
        line = line.upper()
        if len( line ) != 1:
            print( "Please enter exactly one character" )
            continue
        if line < 'A' or line > 'Z':
            print( "Please enter a letter from the alphabet" )
            continue
        return line

def vraagInput(vraag):
    totaal = 0
    while True:
        try:
            totaal =int(input(vraag))
            break
        except ValueError:
            print('verkeerde input. Geef aantal opnieuw in')
    return totaal

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

def dishAmount(dish):
    number = getInteger('Geef aantal keer', dish, 'in: ')
    return number