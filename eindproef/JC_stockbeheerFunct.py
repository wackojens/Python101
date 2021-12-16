def getProducts(orders, stock, lijst1, lijst2, lijst3):

    for order in orders:
        product = stock.get(order[0])

####### Lijst 3 maken
        if product[0] < order[1]:
            if product[0] >= 0:
                lijst3.append([order[0], product[0], product[5], order[1] - product[0], order[2]])
            else:
                lijst3.append([order[0], 0, product[5], order[1] - 0, order[2]])

####### Lijst 1 maken
        if product[0] >= order[1]:
            lijst1.append([order[0], order[1], order[2]])
        elif product[0] < order[1] and product[0] > 0:
            lijst1.append([order[0], product[0], order[2]])

        product[0] = product[0] - order[1]

####### Lijst 2 maken
        if product[0] < product[1] and product[3] != 1:
            lijst2.append([order[0], product[2], product[4], product[5]])
            product[3] = 1
        if product[0] < (0 - product[2]) + product[1]:
            for i in range(len(lijst2)):
                if order[0] in lijst2[i]:
                    lijst2[i][1] = lijst2[i][1] + product[2]



def printList1(lijst1):

    print()
    print(f"{'KLAARZETTEN':^60}")
    print('*' * 60)
    print(f"{'Product':<14}{'|'}{'Aantal':>15}{'|':>15}{'Klant':>15}")
    print(f"{'=' * 14}{'|'}{'=' * 29}{'|'}{'=' * 15}")

    for order in lijst1:
        print(f"{order[0]:<14}{'|'}{order[1]:>15}{'|':>15}{order[2]:>15}")

    print('*' * 60)
    print()



def printList2(lijst2):

    print()
    print(f"{'STOCK AANVULLEN':^60}")
    print('*' * 60)
    print(f"{'Product':<10}{'|'}{'Aantal':>10}{'|':>5}{'Leverancier':>15}{'|':>5}{'Levertijd':>14}")
    print(f"{'=' * 10}{'|'}{'=' * 14}{'|'}{'=' * 19}{'|'}{'=' * 14}")

    for order in lijst2:
        print(f"{order[0]:<10}{'|'}{order[1]:>10}{'|':>5}{order[2]:>15}{'|':>5}{order[3]:>14}")

    print('*' * 60)
    print()



def printList3(lijst3):

    print()
    print(f"{'ONVOLLEDIGE LEVERINGEN':^80}")
    print('*' * 80)
    print(f"{'Product':<10}{'|'}{'Aantal geleverd':^17}{'|':>3}{'Aantal nog leveren':^20}{'|':>3}{'Levertijd':>10}{'|':>5}{'Klant':>11}")
    print(f"{'=' * 10}{'|'}{'=' * 19}{'|'}{'=' * 22}{'|'}{'=' * 14}{'|'}{'=' * 11}")

    for order in lijst3:
        print(f"{order[0]:<10}{'|'}{order[1]:^17}{'|':>3}{order[3]:>9}{'|':>14}{order[2]:>10}{'|':>5}{order[4]:>11}")

    print('*' * 80)
    print()