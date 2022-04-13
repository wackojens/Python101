import pcinput

def getProducts():
    dishes = []
    teller = 65
    while True:
        print('Geef een nieuw product in (x bij naam om te stoppen):')
        name = pcinput.getString('naam: ')
        name = name.lower()
        if name == 'x':
            return dishes
        price = pcinput.getFloat('prijs: ')
        stock = pcinput.getInteger('stock: ')
        code = chr(teller)
        teller += 1
        dishes.append({ 'naam' : name, 'prijs' : price, 'stock' : stock, 'code' : code})

def printProducts(dishes):
    print('*' * 60)
    print(f"*{'product':>12}{'* stock':>30}{'* prijs':^14}  *")
    print('*' * 60)
    for dish in dishes:
        print(f"* {dish['code']} | {dish['naam']:<30}* {dish['stock']:>3}{'* ':>7}{dish['prijs']:>5} euro *")
    print('*' * 60)

def getOrder(dishes):
    order = []
    while True:
        item = pcinput.getString('Geef nieuw item in (x om bestelling af te ronden): ')
        if item == 'x' or item == 'X':
            return order, dishes
        for dish in dishes:
            if dish['naam'] == item or dish['code'] == item:
                print(f"{dish['naam']} {dish['stock']} in stock aan {dish['prijs']}euro.")
                amount = pcinput.getInteger('aantal: ')
                while amount > dish['stock']:
                    amount = pcinput.getInteger('onvoldoende stock. Geef nieuw aantal in: ')
                dish['stock'] -= amount
                order.append({ 'naam' : dish['naam'], 'aantal' : amount, 'prijs' : dish['prijs'], 'totaal' : (amount * dish['prijs'])})
        printProducts(dishes)

def printOrder(order):
    orderTotal = 0
    for item in order:
        orderTotal += item['totaal']
        print(f"-{item['naam']}, {item['aantal']} keer besteld aan {item['prijs']}euro. Totaal: {item['totaal']}euro.")
    print('Er moet', orderTotal, 'euro betaald worden')
    return orderTotal

def getChange(total):
    while True:
        received = pcinput.getFloat('Geef ontvangen bedrag in: ')
        change = received - total
        if change < 0:
            print('Te weinig betaald. Controleer ontvagen bedrag')
            continue
        else:
            print('Je hebt ', received, 'EUR ontvangen', sep='')
            print('Er moet ', round(change, 2), 'EUR teruggegeven worden', sep='')
            return change, received

def getChangeNotes(change):
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    for coin in coins:
        if change == 0:
            return
        amount = 0
        amount = change // coin
        change = change % coin
        change = round(change, 2)
        if amount > 0:
            print(int(amount), end=' ')
            if coin >= 5:
                print('Briefje(s) van ', coin, 'EUR', sep='')
            else:
                print('munt(en) van ', coin, 'EUR', sep='')

def printTicket(order, total, received, change):
    ticket = pcinput.getLetter('Druk op P om een ticket af te drukken of een andere toets om verder te gaan: ')
    if ticket != 'P':
        return
    change = round(change, 2)
    print('*' * 60)
    print(f"* {'product':<}{'* aantal':>21}{'* prijs':^14}{'* totaal':^12}   *")
    print('*' * 60)
    for item in order:
        print(f"* {item['naam']:<20}* {item['aantal']:>4}{'* ':>7}{item['prijs']:>5}euro  * {item['totaal']:>6}euro *")
    print('*' * 60)
    print(f"* Totaal:{total:>45}euro *")
    print(f"* Ontvangen:{received:>42}euro *")
    print(f"* Teruggave:{change:>42}euro *")
    print('*' * 60)

def endRegister(worker, registerContent, dishes):
    while True:
        end = pcinput.getLetter('Wil je stoppen? (Y/N): ')
        if end != 'Y' and end != 'N':
            print('Verkeerde input. Geef keuze opnieuw in.')
        elif end == 'Y':
            print('Bediende:', worker)
            print('De kassa heeft nu ', round(registerContent, 2), 'EUR', ' inhoud', sep='')
            printProducts(dishes)
            with open("stock.txt", "w") as file:
                for dish in dishes:
                    file.writelines(dish)
            file.close()
            exit()
        else:
            return

def readStock():
    dishes = []
