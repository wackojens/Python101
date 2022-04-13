import readInput,copy

draw = 72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5

test = readInput.readLinesDay4Board()

####################### PART 1 #################################

som = 0
done = False
test1 = []
test6 = []
test7 = []

for k in range(0,2500, 25):
    for j in range(5):
        for i in range(5):
            test1.append(test[i+(5*j)+k])
        test6.append(copy.deepcopy(test1))
        test1.clear()
    test7.append(copy.deepcopy(test6))
    test6.clear()

for number in draw:
    for grid in range(100):
        for row in range(5):
            for col in range(5):
                if test7[grid][row][col] == str(number):
                    test7[grid][row][col] = 'X'
                    for bord in range(100):
                        for r in range(5):
                            counterHor = 0
                            counterVer = 0
                            nummer = number
                            for k in range(5):
                                if 'X' in test7[bord][r][k]:
                                    counterHor += 1
                                if counterHor == 5:
                                    print('Bingo! in veld', grid, 'met als laatste nummer', nummer)
                                    veld = grid
                                    done = True
                                    break
                                if 'X' in test7[bord][k][r]:
                                    counterVer += 1
                                if counterVer == 5:
                                    print('Bingo! in veld', grid, 'met als laatste nummer', nummer)
                                    veld = grid
                                    done = True
                                    break
                            if done:
                                break
                        if done:
                            break
                    if done:
                        break
                if done:
                    break
            if done:
                break
        if done:
            break
    if done:
        break

for rij in range(5):
    for kol in range(5):
        print(test7[veld][rij][kol],' ', end='')
        if test7[veld][rij][kol] != 'X':
            som = som + int(test7[veld][rij][kol])
    print()
answer = som * nummer
print(answer)


########################## PART 2  ##########################