text='appel,peer,banaan,kers,appel,kers,kers,mango,appel,appel,kers,tomaat,banaan,appel,appel,appel,appel,kers,banaan,appel,banaan,kers,tomaat,mango'
dictionary = {}

text = text.split(',')
text.sort()

for fruit in text:
#   dictionary[fruit] = text.count(fruit)
    if dictionary.get(fruit):
        dictionary[fruit] += 1
    else:
        dictionary[fruit] = 1
# methode buiten comment gaat kijken in de dictionary of de key(fruit) al bestaat en deze toevoegen, of de value met 1 verhogen telkens hij opnieuw in de tekst voorkomt.
# methode in comment gaat steeds opnieuw het fruit tellen en toevoegen aan de dictionary. Als het fruit er al in zit gaat het steeds overwritten worden. 
# Vanwege de count() functie is de methode in de comment trager omdat er steeds opnieuw gelooped wordt over de hele lijst.
    
# keyList = list(dictionary.keys())
# keyList.sort()
# keys in een lijst steken en sorteren als je al een ongesorteerde dictionary hebt. Daarna over de gesorteerde lijst loopen ipv de dictionary.

for fruit in dictionary:    # Gesorteerde lijst gebruiken ipv dictionary indien de sort functie gebruikt wordt na het maken van de functie.
    print(f"{fruit:<12}{':':>1}{dictionary[fruit]:>3}")