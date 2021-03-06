import biggerOXO_Functions, copy

# 'n' is the variable to scale the size of the game. The game currently supports a max value of 26 for 'n'. Anything higher will not allow you to make some of the inputs.
# 'win' is the variable to change the win condition(the amount of same pieces needed in a row). 'win' needs to be lower or equal to n. It's adviced to use a minimum of 3 for 'win'.
n = 3
win = 3
player = 'X'
emptyField = '-'
rowWidth = []
gameBoard = []

if n > 26 or win > n:
    exit()

###### Dit:
'''
for number in range(n):
    rowWidth.append(emptyField)
for number in range(n):
    gameBoard.append(copy.deepcopy(rowWidth))
'''
# kan vervangen worden door:
'''
for number in range(n)
    gameBoard.append(["-" for x in range(n)])
'''
# copy moet niet meer imported worden en de variabelen "emptyField" en "rowWidth" zijn niet meer nodig in het 2de voorbeeld.


biggerOXO_Functions.showBoard(gameBoard, n)

while True:

    gameBoard = biggerOXO_Functions.getChoice(gameBoard, player, n)
    biggerOXO_Functions.showBoard(gameBoard, n)
    player = biggerOXO_Functions.getWinner(gameBoard, player, n, win)