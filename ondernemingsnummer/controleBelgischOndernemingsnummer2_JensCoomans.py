import inputValidation2

########## X en Y enkel nodig voor tweede methode ########
ondernemingsnummer, x, y = inputValidation2.getValidInput()

controleNummer = ondernemingsnummer % 100
getal = int((ondernemingsnummer - controleNummer) / 100)
check = 97 - (getal % 97)

if controleNummer != check:
    print('Ongeldig nummer')
else:
    print('Geldig nummer')

# Methode 2 
# Aangezien deze oefening over de les 'strings' gaat, is de volgende methode mss meer van toepassing.
####################################################################################################
import inputValidation2

####### X enkel nodig voor eerste methode #########
x, getal, controleNummer = inputValidation2.getValidInput()

check = 97 - (getal % 97)

if controleNummer == check:
    print('Geldig nummer')
else:
    print('Ongeldig nummer')
####################################################################################################