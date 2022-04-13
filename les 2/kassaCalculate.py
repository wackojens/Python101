import pcinput

def getTotalDiscount(dishAmount, prices):
    total = 0
    discount = 0
    for amount, price in zip(dishAmount, prices):
        total = total + amount * price
    if dishAmount[0] >= 2:
        if total >= 150:
            discount = 20
        elif total >= 100:
            discount = 10
        elif total >= 50:
            discount = 5
    totalWithDiscount = total - discount    
    return total, discount, totalWithDiscount

def getChangeNotes(coins, change):
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

def endRegister(worker, registerContent):
    end = pcinput.getLetter('Wil je stoppen? (Y/N): ')
    if end != 'Y' and end != 'N':
        print('Verkeerde input. Geef keuze opnieuw in.')
    elif end == 'Y':
        print()
        print('Bediende:', worker)
        print('De kassa heeft nu ', round(registerContent, 2), 'EUR', ' inhoud', sep='')
        print()
        exit()
    else:
        print()
        return

def getOrderAmount(dishes,dishAmount):
    dishAmount.clear()
    for dish in dishes:
        print('Geef het aantal keer', dish, 'in: ', end='')
        amount = pcinput.getInteger('')
        dishAmount.append(amount)

def getChange(total, received):
    change = received - total
    while True:
        if change < 0:
            print('Te weinig betaald. Controleer ontvagen bedrag')
            received = pcinput.getFloat('Geef ontvangen bedrag in: ')
            change = received - total
            return change
        else:
            return change