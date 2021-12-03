import biggerOXO_Functions

n = 9
player = 'X'
bord = [['-'] * n] * n
print(bord)

biggerOXO_Functions.toon_bord(bord)

while True:

    bord = biggerOXO_Functions.getChoice(bord, player)
    biggerOXO_Functions.toon_bord(bord)
    player = biggerOXO_Functions.getWinner(bord, player)