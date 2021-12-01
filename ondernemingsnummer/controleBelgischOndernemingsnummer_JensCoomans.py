import inputValidation

ondernemingsnummer = inputValidation.getValidInput()

controleNummer = ondernemingsnummer % 100
getal = int((ondernemingsnummer - controleNummer) / 100)
check = 97 - (getal % 97)

if controleNummer != check:
    print('Ongeldig nummer')
else:
    print('Geldig nummer')