import OXO_Function

player = 'X'
bord = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

OXO_Function.toon_bord(bord)

while True:

    bord = OXO_Function.getChoice(bord, player)
    OXO_Function.toon_bord(bord)
    player = OXO_Function.getWinner(bord, player)