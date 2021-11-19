from pcinput import getInteger
totaal = 0
num = getInteger('Geef een nummer (0 om te stoppen): ')
teller = 0
while num != 0:
    totaal += num
    num = getInteger('Geef een nummer (0 om te stoppen): ')
    teller += 1
print('Totaal is', totaal)
print('Gemiddelde is', round((totaal/teller), 2) )