text='appel,peer,banaan,kers,appel,kers,kers,mango,appel,appel,kers,tomaat,banaan,appel,appel,appel,appel,kers,banaan,appel,banaan,kers,tomaat,mango'
text2='appel,peer,banaan,kers,appel,kers,kers,mango,appel,appel,kers,tomaat,banaan,appel,appel,appel,appel,kers,banaan,appel,banaan,kers,tomaat,mango'
dictionary = {}

text = text.split(',')
text2 = text2.split(',')
text2 = list(set(text2))
# text2.sort() is mogelijk maar sorteren voor het maken van de dictionary kan problemen geven bij grotere programma's.

for fruit in text2:
    dictionary[fruit] = text.count(fruit)

keyList = list(dictionary.keys())
keyList.sort()

for fruit in keyList:
    print(f"{fruit:<12}{':':>1}{dictionary[fruit]:>3}")

'''
indien je de input niet 'dubbel' wilt hebben of niet met een set wil werken:

for fruit in text:

OPTIE 1:    dictionary[fruit] = text.count(fruit)

OPTIE 2:    if dictionary.get(fruit):
                dictionary[fruit] += 1
            else:
                dictionary[fruit] = 1

Optie 1  gaat steeds opnieuw het fruit tellen en toevoegen aan de dictionary. Als het fruit er al in zit gaat het steeds overwritten worden. 
Vanwege de count() functie is optie 1 trager omdat er steeds opnieuw gelooped wordt over de hele lijst.

Optie 2 gaat kijken in de dictionary of de key(fruit) al bestaat en deze toevoegen, of de value met 1 verhogen telkens hij opnieuw in de tekst voorkomt.

# keyList = list(dictionary.keys())
# keyList.sort()
# keys in een lijst steken en sorteren als je al een ongesorteerde dictionary hebt. Daarna over de gesorteerde lijst loopen ipv de dictionary.
for fruit in dictionary: 
    print(f"{fruit:<12}{':':>1}{dictionary[fruit]:>3}")
'''