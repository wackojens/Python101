import inputValidation

########## X en Y enkel nodig voor tweede methode ########
ondernemingsnummer, x, y = inputValidation.getValidInput()

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
import inputValidation

####### X enkel nodig voor eerste methode #########
x, getal, controleNummer = inputValidation.getValidInput()

check = 97 - (int(getal) % 97)

if int(controleNummer) == check:
    print('Geldig nummer')
else:
    print('Ongeldig nummer')
####################################################################################################