import readInput

#########################   PART 1
counter = 0
depths = readInput.readLinesDay1()

for i in range(len(depths)):
    depths[i] = int(depths[i])

for i in range(len(depths) - 1):
    if depths[i] < depths[i+1]:
        counter += 1

print(counter)

########################    PART 2
counter = 0

for i in range(len(depths) - 3):
    if (depths[i] + depths[i+1] + depths[i+2]) < (depths[i+1] + depths[i+2] + depths[i+3]):
        counter += 1

print(counter)