'''We hebben een tuple die (sub)tuples bevat.

tpl = (('a', 21),('b', 35),('c', 17), ('d',24))

Controleer of alle tweede items in de (sub)tuples verschillend zijn van elkaar. Indien zo, sorteer dan de tuple op deze waardes.

Voorzie commentaar waarom je voor een bepaalde manier van sortering gekozen hebt.'''
#################################################################################

def getSecond(element):
    return element[1]

tpl = (('a', 21),('b', 35),('c', 17), ('d',24))
aList = list(tpl)

aList.sort(key = getSecond)
tpl = tuple(aList)

aList.sort(key = getSecond, reverse = True)
aReversedList = aList
tpl1 = tuple(aReversedList)

print(tpl)
print(tpl1)

################################################################################

tpl = (('a', 21),('b', 35),('c', 17), ('d',24))
aList = list(tpl)

aList.sort(key = lambda element: element[1])
tpl = tuple(aList)

aList.sort(key = lambda element: element[1], reverse = True)
aReversedList = aList
tpl1 = tuple(aReversedList)

print(tpl)
print(tpl1)

################################################################################