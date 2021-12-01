def getValidInput():
    while True:
        number = str(input("Geef een ondernemingsnummer(type BE 0xxx.xxx.xxx) in of druk op 0 om te stoppen: "))

        if number == '0':
            exit()
        
        number = number.lower()

        if number[0:4] != 'be 0' or number[7] != '.' or number[11] != '.':
            print('Het nummer is niet correct ingegeven. Vergeet zeker de spatie na "BE" en de puntjes tussen de cijfers niet.')
            continue
        
        number = number.replace('be 0', '').replace('.', '')

        if len(number) != 9:
            print('Te weinig of te veel cijfers ingegeven.')
            continue
        
        # Enkel nodig voor methode 2 (om meer met de strings te werken en de les beter toe te passen.)
        #############################################################################################
        number1 = number[0:7]
        number2 = number[7:]
        #############################################################################################

        try:
            number = int(number)
        # Methode 2
        ###########################
            number1 = int(number1)
            number2 = int(number2)
        ###########################
        except ValueError:
            print('Het nummer is niet correct ingegeven. Er mogen geen letters of speciale tekens tussen de cijfers staan.')
            continue
        ############### number1 en number2 enkel nodig voor tweede methode
        return number, number1, number2