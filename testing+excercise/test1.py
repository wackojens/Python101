import pcinput, Funct_testingExcercise

menukaart = [
                {"gerecht" : "mosselen", "prijs" : 20},
                {"gerecht" : "koninginnenhapje", "prijs" : 10},
                {"gerecht" : "stoofvlees", "prijs" : 15},
                {"gerecht" : "ijs", "prijs" : 3},
                {"gerecht" : "taart", "prijs" : 3.5},
                {"gerecht" : "bier", "prijs" : 2.5},
                {"gerecht" : "frisdrank", "prijs" : 2},
                {"gerecht" : "wijn", "prijs" : 3}
        ]

bestelling = []

bestelling = list(Funct_testingExcercise.getOrder(menukaart, bestelling))

for gerecht in bestelling:
    print(gerecht)
    print(gerecht["aantal"] * gerecht["prijs"])