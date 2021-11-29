import datetime

now = datetime.datetime.now()

def printTicket(worker, dishes, dishAmount, prices, total, discount, totalWithDiscount, received, change):
    print(f"{'Kassaticket':^60}")
    print('*'*60)

    print(f"{'U werd geholpen door:':<30}{worker:>30}")
    print(f"{now.strftime('%Y-%m-%d'):<30}{now.strftime('%H:%M:%S'):>30}")
    print('*'*60)

    print(f"{'Besteld':<28}{'Aantal':<16}{'Bedrag':>16}")
    printOrderedDishes(dishes, dishAmount, prices)
    print('='*60)

    print(f"{'Totaal te betalen:':<50}{total:>9.2f}{'€':>1}")

    if discount > 0:
        print(f"{'Korting:':<50}{'-':>3}{discount:>6.2f}{'€':>1}")
        print(f"{'Totaal met korting:':<50}{totalWithDiscount:>9.2f}{'€':>1}")
    print('-'*60)

    print(f"{'Betaald:':<50}{received:>9.2f}{'€':>1}")
    print(f"{'Wisselgeld:':<50}{change:>9.2f}{'€':>1}")
    print('*'*60)

    if dishAmount[0] == 0 and dishAmount[1] == 0 and dishAmount[2] == 0:
        print(f"{'Gezondheid !!!':^60}")
    else:
        print(f"{'Smakelijk eten !!!':^60}")
        print('*'*60)


def printOrderedDishes(dishes, dishAmount, prices):
    for dish, amount, price in zip(dishes, dishAmount, prices):
        if amount > 0:
            print(f"{'-':<1}{dish:<29}{amount:<15}{amount * price:>14.2f}{'€':>1}")