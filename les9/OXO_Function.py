import pcinput

def toon_bord(bord):
    print('  A B C')
    for rij in range(3):
        print(rij + 1, end=' ')
        for kol in range(3):
            print(bord[rij][kol], end=' ')
        print()

def getChoice(bord, player):
    print('Speler', player, 'is aan de beurt')
    while True:
        rij = pcinput.getInteger('Geef de rij in waar je iets wilt plaatsen(1, 2 of 3): ')
        if rij < 1 or rij > 3:
            print('De rij kan enkel 1, 2 of 3 zijn.')
            continue
        rij -= 1
        kol = pcinput.getLetter('Geef de kolom in waar je iets wilt plaatsen(A, B of C): ')
        kol = kol.upper()
        if kol < 'A' or kol > 'C':
            print('De kolom kan enkel A, B of C zijn.')
            continue
        if kol == 'A':
            kol = 0
        elif kol == 'B':
            kol = 1
        else:
            kol = 2
        if bord[rij][kol] != '-':
            print('Plaats is al bezet. Kies opnieuw')
            continue
        bord[rij][kol] = player
        return bord

def getWinner(bord, player):
    for rij in range(3):
        if (bord[rij][0] == bord[rij][1] == bord[rij][2]) and bord[rij][0] != '-':
            print('Speler', player, 'heeft gewonnen. Proficiat!')
            exit()
    for kol in range(3):
        if (bord[0][kol] == bord[1][kol] == bord[2][kol]) and bord[0][kol] != '-':
            print('Speler', player, 'heeft gewonnen. Proficiat!')
            exit()
    middle = bord[1][1]
    if ((middle == bord[0][0] == bord[2][2]) or (middle == bord[0][2] == bord[2][0])) and middle != '-':
        print('Speler', player, 'heeft gewonnen. Proficiat!')
        exit()
    for rij in range(3):
        for kol in range(3):
            if bord[rij][kol] == '-':
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                return player
    print('Gelijkspel')
    exit()



























'''def getWinnerTest(bord, player):
    for rij in range(3):
        for kol in range(3):
            if ((bord[rij][kol] == bord[rij][kol + 1 - kol] and bord[rij][kol] == bord[rij][kol + 2 - kol]) 
            or (bord[rij][kol] == bord[rij + 1 - rij][kol] and bord[rij][kol] == bord[rij + 2 - rij][kol])) and bord[rij][kol] != '-':
                print('Speler', player, 'heeft gewonnen. Proficiat!')
                exit()
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player'''