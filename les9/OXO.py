import OXO_Function

player = 'X'
gameBoard = [['-','-','-'],['-','-','-'],['-','-','-']]

OXO_Function.showBoard(gameBoard)

while True:

    gameBoard = OXO_Function.getChoice(gameBoard, player)
    OXO_Function.showBoard(gameBoard)
    player = OXO_Function.getWinner(gameBoard, player)