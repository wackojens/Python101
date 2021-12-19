import pcinput

def getOrder(products, order):
    order.clear()
    for product in products:
        num = pcinput.getInteger(f"Aantal {product['naam']}: ")
        order.append([product['naam'], num])
        if 'aantal' not in product:
            product['aantal'] = 0
        product['aantal'] += num



def printOrderTXT(teller, order):
    teller += 1
    with open("bestellingen.txt", "a") as file:
        file.writelines(f"Bestelling {teller}\n")
        file.writelines(f"{'-' * 17}\n")
        for product in order:
            file.writelines(f"{product[0]}: {product[1]}\n")
        file.writelines(f"{'=' * 17}\n")
        file.writelines('\n')
        file.writelines('\n')
    file.close()
    return teller



def getTime():
    while True:
        print()
        time = pcinput.getInteger('Hoe laat is het nu?(1-12): ')
        if time < 1 or time > 12:
            print('Geef het uur in. Enkel waarden van 1 tot en met 12 aub.')
            continue
        print()
        return time



def getAmounts(products):
    totalIngredients = []
    suiker = 0
    meel = 0
    donker_meel = 0
    gist = 0
    zout = 0
    noten = 0

    for product in products:
        if 'suiker' in product['recept']:
            suiker += (product['recept']['suiker'][0] * product['aantal'])
        if 'meel' in product['recept']:
            meel += (product['recept']['meel'][0] * product['aantal'])
        if 'donker_meel' in product['recept']:
            donker_meel += (product['recept']['donker_meel'][0] * product['aantal'])
        if 'gist' in product['recept']:
            gist += (product['recept']['gist'][0] * product['aantal'])
        if 'zout' in product['recept']:
            zout += (product['recept']['zout'][0] * product['aantal'])
        if 'noten' in product['recept']:
            noten += (product['recept']['noten'][0] * product['aantal'])

    totalIngredients.append(['suiker', suiker])
    totalIngredients.append(['meel', meel])
    totalIngredients.append(['donker_meel', donker_meel])
    totalIngredients.append(['gist', gist])
    totalIngredients.append(['zout', zout])
    totalIngredients.append(['noten', noten])

    return totalIngredients



def printTotals(products, ingredients):
    for product in products:
        print(f"{product['naam']:<14}: {product['aantal']:>3}")
    print()
    for ingredient in ingredients:
        if 'noten' in ingredient:
            print(f"{ingredient[0]:<11}: {ingredient[1]:>6}el")
        else:
            print(f"{ingredient[0]:<11}: {ingredient[1]:>6}gr")
    print()



def getStock(stock, ingredients):
    counter = 0
    for key in stock:
        stock[key][0] -= ingredients[counter][1]
        counter += 1
        print(f"{key:<11}:", stock[key])