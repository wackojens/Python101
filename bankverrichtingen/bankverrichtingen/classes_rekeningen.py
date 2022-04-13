from bankverrichtingen.class_persoon import Persoon



class InvalidRekeningnummer(Exception):
    pass



class Rekening():
    def __init__(self, rekeningnummer: str, persoon: Persoon):
        self.rekeningnummer = rekeningnummer
        self.persoon = persoon
        self.controleInput()
        self.controleRekeningnummer()
        self.geld = 0

    def rekeningOverzicht(self):
        return (f'{self.persoon.voornaam} {self.persoon.achternaam}, er staat {self.geld}EUR op je rekening.')

    def controleInput(self):
        if not isinstance(self.persoon, Persoon):
            raise TypeError('Please provide Persoon object for persoon')
        if not isinstance(self.rekeningnummer, str):
            raise TypeError('Please provide string argument for rekeningnummer')
        if len(self.rekeningnummer) != 14:
            raise ValueError('Use correct format for rekeningnummer: ###-#######-##')
        if self.rekeningnummer[3] != '-' or self.rekeningnummer[11] != '-':
            raise ValueError('Use correct format for rekeningnummer: ###-#######-##')
        self.testNummer = self.rekeningnummer.replace('-', '')
        try:
            self.testNummer = int(self.testNummer)
        except:
            raise ValueError('Use correct format for rekeningnummer: ###-#######-##')

    def controleRekeningnummer(self):
        controlenummer = self.testNummer % 100
        getal = int((self.testNummer - controlenummer) / 100)
        check = getal % 97
        if check == 0:
            check = 97
        if controlenummer != check:
            raise InvalidRekeningnummer("Rekeningnummer isn't valid")

    def overschrijven(self, other):
        return NotImplemented



class Zichtrekening(Rekening):
    def overschrijven(self, other: Rekening, bedrag):
        if not isinstance(other, Rekening):
            raise TypeError("Overschrijvingen have to be to other rekeningen.")
        if not isinstance(bedrag, int) and not isinstance(bedrag, float):
            raise TypeError("Bedrag has to be a numerical value (int or float)")
        if bedrag <= 0:
            raise ValueError("Bedrag has to be a positive number")
        if (not isinstance(other, Zichtrekening)) and (not (isinstance(other, Spaarrekening) and self.persoon == other.persoon)):
            raise ValueError("Overschrijvingen have to be to other zichtrekeningen or your own spaarrekening")
        if isinstance(other, Zichtrekening) and self.rekeningnummer == other.rekeningnummer:
            raise ValueError("Overschrijven isn't possible to the same rekening")
        self.geld -= bedrag
        other.geld += bedrag

    def opvragen(self, bedrag):
        if not isinstance(bedrag, int) and not isinstance(bedrag, float):
            raise TypeError("Bedrag has to be a numerical value (int or float)")
        if bedrag <= 0:
            raise ValueError("Bedrag has to be a positive number")
        self.geld -= bedrag

    def storten(self, bedrag):
        if not isinstance(bedrag, int) and not isinstance(bedrag, float):
            raise TypeError("Bedrag has to be a numerical value (int or float)")
        if bedrag <= 0:
            raise ValueError("Bedrag has to be a positive number")
        self.geld += bedrag



class Spaarrekening(Rekening):
    def overschrijven(self, other: Zichtrekening, bedrag):
        if not isinstance(other, Zichtrekening):
            raise TypeError("Overschrijven has te be done to your zichtrekening")
        if self.persoon != other.persoon:
            raise ValueError("Overschrijven can only be done to your own zichtrekeningen")
        if not isinstance(bedrag, int) and not isinstance(bedrag, float):
            raise TypeError("Bedrag has to be a numerical value (int or float)")
        if bedrag <= 0:
            raise ValueError("Bedrag has to be a positive number")
        if bedrag > self.geld:
            raise ValueError("Spaarrekening can't go below 0")
        self.geld -= bedrag
        other.geld += bedrag