import bakkerijFunct

tijd = 0
teller = 0
bestelling = []

producten = [
    { 
        "naam": "noten brood",
        "gewicht": (800,"gr"), 
        "recept": {
            "suiker": (10,"gr"),
            "meel": (600, "gr"),
            "water": (300, "ml"),
            "zout": (5, "gr"),
            "gist": (2, "gr"),
            "noten": (5, "el")
        }
    },
    { 
        "naam": "bruin brood",
        "gewicht": (800,"gr"), 
        "recept": {
            "suiker": (10,"gr"),
            "donker_meel": (600, "gr"),
            "water": (300, "ml"),
            "zout": (5, "gr"),
            "gist": (2, "gr"),
            "noten": (5, "el")
        }
    },
    { 
        "naam": "wit brood",
        "gewicht": (600,"gr"), 
        "recept": {
            "suiker": (10,"gr"),
            "meel": (500, "gr"),
            "water": (200, "ml"),
            "zout": (5, "gr"),
            "gist": (2, "gr")
        }
    },
    { 
        "naam": "sandwich",
        "gewicht": (50,"gr"), 
        "recept": {
            "suiker": (5,"gr"),
            "meel": (40, "gr"),
            "water": (5, "ml"),
            "gist": (0.5, "gr"),
        }
    },
    { 
        "naam": "noten sandwich",
        "gewicht": (50,"gr"), 
        "recept": {
            "suiker": (5,"gr"),
            "meel": (40, "gr"),
            "water": (5, "ml"),
            "gist": (0.5, "gr"),
            "noten": (1, "el")
        }
    }
]

voorraad = {
    "suiker": [5000, 1000, "gr"],
    "meel": [100000, 10000, "gr"], 
    "donker_meel": [100000, 10000, "gr"],          
    "gist": [5000, 1000, "gr"],
    "zout": [5000, 1000, "gr"],
    "noten": [50, 20, "el"],    
}

while tijd != 10:
    bakkerijFunct.getOrder(producten, bestelling)
    teller = bakkerijFunct.printOrderTXT(teller, bestelling)
    tijd = bakkerijFunct.getTime()
print('=' * 100)

ingredienten = bakkerijFunct.getAmounts(producten)
bakkerijFunct.printTotals(producten, ingredienten)
bakkerijFunct.getStock(voorraad, ingredienten)

# vraag de bestellingen

# bereken de totalen van de bestelde producten en print

# bereken de totalen per ingredient en druk af

# print de nieuwe stock af