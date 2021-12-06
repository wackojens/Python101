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
oxList = []
oxBinary = readInput.readLinesDay3()

for j in range(len(oxBinary[0])):
    count0 = 0
    count1 = 0
    for i in range(len(oxBinary)):
        if oxBinary[i][j] == '1':
            count1 += 1
        else:
            count0 += 1
    if count1 > count0:
        for k in oxBinary:
            if k[j] != '0':
                oxList.append(k)
    elif count0 > count1:
        for k in oxBinary:
            if k[j] != '1':
                oxList.append(k)
    else:
        for k in oxBinary:
            if k[j] != '0':
                oxList.append(k)

    oxBinary.clear()
    oxBinary = oxBinary + oxList
    oxList.clear()
    if len(oxBinary) == 1:
        break



coBinary = readInput.readLinesDay3()
coList = []

for j in range(len(coBinary[0])):
    count0 = 0
    count1 = 0
    for i in range(len(coBinary)):
        if coBinary[i][j] == '1':
            count1 += 1
        else:
            count0 += 1
    if count1 > count0:
        for k in coBinary:
            if k[j] != '1':
                coList.append(k)
    elif count0 > count1:
        for k in coBinary:
            if k[j] != '0':
                coList.append(k)
    elif count0 == count1:
        for k in coBinary:
            if k[j] != '1':
                coList.append(k)
    
    coBinary.clear()
    coBinary = coBinary + coList
    coList.clear()
    if(len(coBinary)) == 1:
        break



oxBinary = str(oxBinary)
oxBinary = oxBinary.replace('[','').replace("'",'').replace(']', '')
oxBinary = int(oxBinary, 2)

coBinary = str(coBinary)
coBinary = coBinary.replace('[','').replace("'",'').replace(']', '')
coBinary = int(coBinary, 2)

print(oxBinary * coBinary)