import pcinput

diagonal = 0
matrix = []

size = pcinput.getInteger('Input the size of the matrix: ')

# waarden per veld vragen en de som van de diagonaal berekenen 
for i in range(size):
    matrix.append([pcinput.getInteger('Input the field value that u would like to use: ') for j in range(size)])
    diagonal += matrix[i][i]

# matrix weergeven en som van de diagonaal afprinten
print()
for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=' ')
    print()
print()
print('Sum of matrix primary diagonal: ', diagonal)