import random
teller = 0
percentage = 0
questionAmount = 5
solutions = []

while teller != questionAmount:
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result = num1 + num2
    solutions.append(result)
    print( num1, '+', num2, '=', end=' ')
    answer = int(input( ))
    if num1 + num2 == answer:
        percentage = percentage + (100 / questionAmount)
    teller += 1

print('')
print(percentage, '%')
if percentage >= 50:
    print('Geslaagd!')
else:
    print('Niet geslaagd')

print('')
print('Oplossingen:')
for solution in solutions:
    print(solution)