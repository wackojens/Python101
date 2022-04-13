# Code in comments op lines: 5-6, 9-15, 37-38, 43 nodig om zeer grote bestellingen correct te laten verlopen. Line 39 wordt vervangen door line 37 en moet dus uitgeschakeld worden.

def getProducts(orders, stock, lijst1, lijst2, lijst3):

#   tellerForProduct = []
#   teller = 1

    for order in orders:
#       for i in range(len(tellerForProduct)):
#           if order[0] in tellerForProduct[i]:
#               teller = tellerForProduct[i][1]
#               tellerForProduct.remove(tellerForProduct[i])
#               break
#           else:
#               teller = 1
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
#       while product[0] < (0 - product[2]) * teller + product[1]:
#           teller += 1
        if product[0] < (0 - product[2]) + product[1]:
            for i in range(len(lijst2)):
                if order[0] in lijst2[i]:
                    lijst2[i][1] = lijst2[i][1] + product[2]
#       tellerForProduct.append([order[0], teller])



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