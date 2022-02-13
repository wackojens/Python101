class Persoon():
    def __init__(self, voornaam:str, achternaam:str, rijksregisternummer:str):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.rijksregisternummer = rijksregisternummer
        self.controle()

    def controle(self):
        if not isinstance(self.voornaam, str) or not isinstance(self.achternaam, str) or not isinstance(self.rijksregisternummer, str):
            raise TypeError('Please provide string arguments')
        if len(self.rijksregisternummer) != 15:
            raise ValueError('Use correct format for rijksregisternummer: ##.##.##-###.##')
        if self.rijksregisternummer[2] != '.' or self.rijksregisternummer[5] != '.' or self.rijksregisternummer[8] != '-' or self.rijksregisternummer[12] != '.':
            raise ValueError('Use correct format for rijksregisternummer: ##.##.##-###.##')
        check = self.rijksregisternummer.replace('.','').replace('-','')
        try:
            check = int(check)
        except:
            raise ValueError('Use correct format for rijksregisternummer: ##.##.##-###.##')