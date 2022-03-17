from mysql.connector import Error, connect
from dotenv import dotenv_values

config = dotenv_values(".env")





class ClassicModels():
    def __init__(self):
        self.openClassicModels()

    def openClassicModels(self):
        try:
            self.conn = connect(**config)
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
        except Error as e:
            print("Error connectie met MySQL", e)

    def sluitClassicModels(self):
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
        except Error as e:
            print("Error connectie met MySQL", e)





class Klant(ClassicModels):
    def __init__(self, klant_nr=0):
        super().__init__()
        self.nr = klant_nr
        self.naam = ''
        self.anaam = ''
        self.vnaam = ''
        self.tel = ''
        self.adres1 = ''
        self.adres2 = ''
        self.gemeente = ''
        self.staat = ''
        self.postcode = ''
        self.land = ''
        self.verkopernr = ''
        self.creditLimiet = ''
        if self.nr > 0:
            self.getKlant(self.nr)
        super().sluitClassicModels()

    def __repr__(self):
        return f'(<Klant> ' \
            f'\n\tklantnr: {self.nr}, ' \
            f'\n\tklantfirmanaam: {self.naam}, ' \
            f'\n\tklantachternaam: {self.anaam},' \
            f'\n\tklantvoornaam: {self.vnaam},' \
            f'\n\tklanttel: {self.tel}, ' \
            f'\n\tklantadres1: {self.adres1}, ' \
            f'\n\tklantadres2: {self.adres2}, ' \
            f'\n\tklantgemeente: {self.gemeente}, ' \
            f'\n\tklantstaat: {self.staat}, ' \
            f'\n\tklantpostcode: {self.postcode}, ' \
            f'\n\tklantland: {self.land}, ' \
            f'\n\tklantverkopernr: {self.verkopernr}, ' \
            f'\n\tklantcreditlimiet: {self.creditLimiet})'

    def getKlant(self,klantnr)  :
        super().openClassicModels()
        strSQL = "select * from  customers where customerNumber = %(klantnr)s"
        self.cursor.execute(strSQL,{'klantnr':klantnr})
        self.record = self.cursor.fetchone()
        if self.cursor.rowcount > 0: 
            self.matchKlantrecord(self.record)
        super().sluitClassicModels()

    def matchKlantrecord(self,record):
        self.nr = record[0]
        self.naam = record[1]
        self.anaam = record[2]
        self.vnaam = record[3]
        self.tel = record[4]
        self.adres1 = record[5]
        self.adres2 = record[6]
        self.gemeente = record[7]
        self.staat = record[8]
        self.postcode = record[9]
        self.land = record[10]
        self.verkopernr = record[11]
        self.creditLimiet = record[12]

    def setKlant(self):
        pass




if __name__ == "__main__":
    klant1 = Klant()
    klant1.getKlant(121)
    print(klant1)
    print('klantfirmanaam:',klant1.naam)
    
    klant2 = Klant(276)
    print(klant2)
    
    klant3 = Klant(455000)
    print(klant3)
