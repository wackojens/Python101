import readInput

#####################   PART 1
answerGamma = []
answerEpsilon = []
binary = readInput.readLinesDay3()

for j in range(len(binary[0])):
    count0 = 0
    count1 = 0
    for i in range(len(binary)):
        if binary[i][j] == '1':
            count1 += 1
        else:
            count0 += 1
    if count1 > count0:
        answerGamma.append('1')
    else:
        answerGamma.append('0')

for i in answerGamma:
    if i == '1':
        answerEpsilon.append('0')
    else:
        answerEpsilon.append('1')

answerGamma = ''.join(answerGamma)
answerEpsilon = ''.join(answerEpsilon)

answerGamma = int(answerGamma, 2)
answerEpsilon = int(answerEpsilon, 2)

print(answerGamma * answerEpsilon)

####################    PART 2
newList = []

for j in range(len(binary[0])):
    count0 = 0
    count1 = 0
    for i in range(len(binary)):
        if binary[i][j] == '1':
            count1 += 1
        else:
            count0 += 1
    if count1 > count0:
        for k in binary:
            if k[j] != '0':
                newList.append(k)
    elif count0 > count1:
        for k in binary:
            if k[j] != '1':
                newList.append(k)
    else:
        for k in binary:
            if k[j] != '0':
                newList.append(k)

    binary.clear()
    binary = newList
    newList.clear()

print(binary)

exit()
binaryTest = readInput.readLinesDay3()
newList = []

for j in range(len(binaryTest[0])):
    count0 = 0
    count1 = 0
    for i in range(len(binaryTest)):
        if binary[i][j] == '1':
            count1 += 1
        else:
            count0 += 1
    if count1 > count0:
        for k in binaryTest:
            if k[j] != '1':
                newList.append(k)
    elif count0 > count1:
        for k in binaryTest:
            if k[j] != '0':
                newList.append(k)
    else:
        for k in binaryTest:
            if k[j] != '1':
                newList.append(k)

    binaryTest.clear()
    binaryTest = binaryTest + newList
    newList.clear()

print(binaryTest)