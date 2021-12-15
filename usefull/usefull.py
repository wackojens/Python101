# print ascii in een tabel vorm startend vanaf positie 32
'''teller = 32

for x in range(16):
    for y in range(6):

        print(f"{'|':<5}{teller:^3}{chr(teller):^3}", end='')
        teller = teller + 16

    print('|')
    teller = teller - 95


start = 32

for row in range(16):
    for column in range(6):
        
        value = start + row + column * 16

        print(f"{'|':<5}{value:^3}{chr(value):^3}", end='')

    print('|')'''
# beide methodes bereiken hetzelfde resultaat


# bepaalde type letters zoeken in een string(in dit geval de klinkers)
'''tekst= '\
Update je gaming setup met de \
AMD Advanced Upgrade Kit met Ryzen 7 3700X. \
Deze kit bestaat uit een processor, \
een moederbord, intern geheugen en koelpasta.'

tekst = tekst.lower()

teller = 0
for letter in tekst:
    if letter in 'aeuio':
        teller += 1
print(teller)'''


# volgende maakt een lijst van 'n-aantal' lijsten met 'n-aantal' keer "-". Handig om een tabel te maken van 'n' op 'n' gevuld met "-".
'''
for number in range(n)
    gameBoard.append(["-" for x in range(n)])
'''


# volgt op het vorige. Functie om een tabel af te printen van 'n' op 'n' gevuld met de inhoud van gBoard(in dit geval is gBoard een lijst gevuld met lijsten gevuld met "-")
'''
def showBoard(gBoard, n):

    print('  ', end=' ')
    for i in range(n):
        print(chr(65 + i), end=' ')
    print()

    for row in range(n):
        print(f"{row + 1:>2}", end=' ')
        for col in range(n):
            print(gBoard[row][col], end=' ')
        print()
'''

# les 8 sortTuple voor subTuples te sorten
# les 8 les8_oef oefeningen met sorts

#print een tabel met de tafels
'''
for x in range(1,21):
    for y in range(1,11):
        print((f"{x:>2} x{y:>2} ={x * y:>3}"), end='  ')
    print()

# 2 keer hetzelfde resultaat

for x in range(1,21):
    for y in range(1,11):
        print(("{:>2} x{:>2} ={:>3}").format(x,y,x*y), end='  ')
    print()
'''