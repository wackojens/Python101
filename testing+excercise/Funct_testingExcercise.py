import pcinput

def getOrder(dishes, orders):
    for dish in dishes:
        orderDict = {}
        num = pcinput.getInteger(f"Aantal {dish['gerecht']}: ")
        orderDict = {"gerecht": dish["gerecht"], "prijs": dish["prijs"], "aantal": num}
        orders.append(orderDict)
    return orders