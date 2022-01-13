import pcinput, datetime

def getOrder(products, order):
    order.clear()
    for product in products:
        num = pcinput.getInteger(f"Aantal {product['naam']}: ")
        order.append([product['naam'], num])
        product["aantal"] = product.get("aantal", 0) + num



def printOrderTXT(teller, order):
    now = datetime.datetime.now()
    teller += 1
    with open("bestellingen.txt", "a") as file:
        file.writelines(f"Bestelling {teller}\n")
        file.writelines(f"{now.strftime('%d-%m-%Y  %H:%M:%S')}\n")
        file.writelines(f"{'-' * 20}\n")
        for product in order:
            file.writelines(f"{product[0]}: {product[1]}\n")
        file.writelines(f"{'=' * 20}\n")
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



def printTotals(products, ingredients):
    for product in products:
        print(f"{product['naam']:<14}: {product['aantal']:>3}")
    print()
    for ingredient in ingredients:
        if 'noten' in ingredient:
            print(f"{ingredient:<11}: {ingredients[ingredient]:>6}el")
        elif 'water' in ingredient:
            print(f"{ingredient:<11}: {ingredients[ingredient]:>6}ml")
        else:
            print(f"{ingredient:<11}: {ingredients[ingredient]:>6}gr")
    print()



def getStock(stock, ingredients):
    resupply = []
    for key in stock:
        stock[key][0] -= ingredients[key]
        print(f"{key:<11}:", stock[key])
    print()
    for key in stock:
        if stock[key][0] < stock[key][1]:
            resupply.append(key)
            print(f"{key} bijbestellen")




def getIngredients(products):
    totalIngr = {}
    for product in products:
        recept = product.get("recept")
        for ingr in recept:
            totalIngr[ingr] = totalIngr.get(ingr, 0) + product['aantal'] * recept[ingr][0] 
    return totalIngr