try:
 bedrag =int(input("Enter your value: "))
 aantal100 =(bedrag // 100)
 rest =(bedrag % 100)
 aantal50 =(rest // 50)
 rest =(rest % 50)
 aantal20 =(rest // 20)
 rest =(rest % 20)
 aantal10 =(rest // 10)
 rest =(rest % 10)
 aantal5 =(rest // 5)
 rest =(rest % 5)
 aantal2 =(rest // 2)
 rest =(rest % 2)
 aantal1 =(rest // 1)
 rest =(rest % 1)
 print(bedrag, 'bestaat', 'uit:', end=' ')
 print(aantal100, 'x', '100,', aantal50, 'x', '50,', aantal20, 'x', '20,', aantal10, 'x', '10,', aantal5, 'x', '5,', aantal2, 'x', '2,', 'en', aantal1, 'x', '1.')
except:
 print('Geef een geheel getal')