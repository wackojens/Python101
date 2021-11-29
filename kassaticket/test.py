import kassaCalculate

gerechten = ['mosselen', 'koninginnenhapje', 'ijs', 'drank']
aantalGerechten = []
bediende = 'Jens'
inhoudKassa = 50

while True:
    kassaCalculate.getOrderAmount(gerechten, aantalGerechten)
    print()

    if kassaCalculate.getValidOrder(aantalGerechten, bediende, inhoudKassa):
        continue
    else:
        print('test2')
        break