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

        try:
            number = int(number)
        except ValueError:
            print('Het nummer is niet correct ingegeven. Er mogen geen letters tussen de cijfers staan.')
            continue

        return number