import pcinput

def showBoard(gBoard):

    print('  A B C')

    for row in range(3):
        print(row + 1, end=' ')
        for col in range(3):
            print(gBoard[row][col], end=' ')
        print()



def getChoice(gBoard, player):

    print("It's player ", player, "'s turn", sep='')

    while True:

        row = pcinput.getInteger('Choose the row that you want to use.(1, 2 or 3): ')
        row -= 1
        if row < 0 or row > 2:
            print('The row can only be 1, 2 or 3.')
            continue

        col = pcinput.getLetter('Choose the column you want to use.(A, B or C): ')
        col = ord(col) - 65
        if col < 0 or col > 2:
            print('The column can only be "A", "B" or "C".')
            continue

        if gBoard[row][col] != '-':
            print('Space is occupied. Choose another space.')
            continue

        gBoard[row][col] = player
        return gBoard



def getWinner(gBoard, player):

# Check horizontal and vertical
    for row in range(3):
        counterHor = 0
        counterVert = 0
        for col in range(3):
            if player in (gBoard[row][col]):
                counterHor += 1
                if counterHor == 3:
                    print('Player', player, 'wins. Congratulations!')
                    exit()
            if player in (gBoard[col][row]):
                counterVert += 1
                if counterVert == 3:
                    print('Player', player, 'wins. Congratulations!')
                    exit()

# Check diagonal
    counterUpDown = 0
    counterDownUp = 0
    row = 2
    for col in range(3):
        if player in (gBoard[col][col]):
            counterUpDown += 1
            if counterUpDown == 3:
                print('Player', player, 'wins. Congratulations!')
                exit()
        if player in (gBoard[row - col][col]):
            counterDownUp += 1
            if counterDownUp == 3:
                print('Player', player, 'wins. Congratulations!')
                exit()

# Check if playing field is full and swap player if not
    for row in range(3):
        for col in range(3):
            if gBoard[row][col] == '-':
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                return player
                
    print('Draw')
    exit()