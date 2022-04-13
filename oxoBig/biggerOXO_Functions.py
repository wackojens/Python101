import pcinput

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



def getChoice(gBoard, player, n):

    print("It's player ", player, "'s turn", sep='')

    while True:

        row = pcinput.getInteger('Choose the row that you want to use: ')
        row -= 1
        if row < 0 or row > (n - 1):
            print('The row can only be between 1 and', n)
            continue

        col = pcinput.getLetter('Choose the column you want to use: ')
        col = ord(col) - 65
        if col < 0 or col > (n - 1):
            print('The column can only be between A and', chr(65 + (n - 1)))
            continue

        if gBoard[row][col] != '-':
            print('Space is occupied. Choose another space.')
            continue

        gBoard[row][col] = player
        return gBoard



def getWinner(gBoard, player, n, win):

# Check horizontal and vertical
    for row in range(n):
        counterHor = 0
        counterVert = 0
        for col in range(n):
            if player in (gBoard[row][col]):
                counterHor += 1
            else:
                counterHor = 0
            if counterHor == win:
                print('Player', player, 'wins. Congratulations!')
                exit()
            if player in (gBoard[col][row]):
                counterVert += 1
            else:
                counterVert = 0
            if counterVert == win:
                print('Player', player, 'wins. Congratulations!')
                exit()

# Check diagonal
    counterUpDown = 0
    counterDownUp = 0
    row = n - 1
    for col in range(n):
        if player in (gBoard[col][col]):
            counterUpDown += 1
        else:
            counterUpDown = 0
        if counterUpDown == win:
            print('Player', player, 'wins. Congratulations!')
            exit()
        if player in (gBoard[row - col][col]):
            counterDownUp += 1
        else:
            counterDownUp = 0
        if counterDownUp == win:
            print('Player', player, 'wins. Congratulations!')
            exit()

# Check if playing field is full and swap player if not
    for row in range(n):
        for col in range(n):
            if gBoard[row][col] == '-':
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                return player
                
    print('Draw')
    exit()