from os import read
import readInput

######################  PART 1 
counterFo = 0
counterDo = 0
counterUp = 0
directions = readInput.readLinesDay2()

lst=[]

for i in directions:
    command, value = i.split()
    if command == 'forward':
        counterFo = counterFo + int(value)
    if command == 'down':
        counterDo = counterDo + int(value)
    if command == 'up':
        counterUp = counterUp + int(value)

print(counterFo * (counterDo - counterUp))

###################### PART 2
counterFor = 0
counterDep = 0
counterAim = 0
lst = []

for i in directions:
    command, value = i.split()
    if command == 'forward':
        counterFor = counterFor + int(value)
        counterDep = counterDep + (counterAim * int(value))
    if command == 'down':
        counterAim = counterAim + int(value)
    if command == 'up':
        counterAim = counterAim - int(value)

print(counterFor * counterDep)