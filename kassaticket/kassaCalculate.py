import pcinput

def getValidOrder(dishes,dishAmount, worker, registerContent):
    while True:
        teller = 0
        dishAmount.clear()
        for dish in dishes:
            print('Geef het aantal keer', dish, 'in: ', end='')
            amount = pcinput.getInteger('')
            dishAmount.append(amount)
        for amount in dishAmount:
            if amount == 0:
                teller = teller + 1
        if teller == len(dishAmount):
            print()
            print('Geen bestelling geplaatst. Begin opnieuw of stop het programma.')
            endRegister(worker, registerContent)
        else:
            print()
            break


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
    print('Er moet ', float(totalWithDiscount), 'EUR betaald worden.', sep='')
    print()  
    return total, discount, totalWithDiscount


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
    print()


def endRegister(worker, registerContent):
    while True:
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