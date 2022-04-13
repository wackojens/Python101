import datetime

class Student:
    def __init__(self, voorNaam: str = '', achterNaam: str = '', geboortedatum: tuple = (0,0,0), administratienummer: int = 0) -> None:
        self.vNaam = voorNaam
        self.aNaam = achterNaam
        self.gbdat = geboortedatum
        self.adNum = administratienummer
        self.leeftijd = self.getAge()
        self.curs = []

    def showCursussen(self):
        print(self.vNaam, self.aNaam)
        if len(self.curs) > 0:
            for curs in self.curs:
                print(curs.naam)
            print()
        else:
            print('Niet ingeschreven\n')
    
    def getAge(self):
        today = datetime.date.today()
        self.dag = self.gbdat[0]
        self.maand = self.gbdat[1]
        self.jaar = self.gbdat[2]
        return today.year - self.jaar - ((today.month, today.day) < (self.maand, self.dag))

    def addCursus(self, *args):
        for newCursus in args:
            if newCursus not in self.curs:
                self.curs.append(newCursus)           
                newCursus.addStudent(self)



class Cursus:
    def __init__(self, naam: str = '', nummer: int = 0) -> None:
        self.naam = naam
        self.num = nummer
        self.studs = []

    def addStudent(self, *args):
        for newStudent in args:
            if newStudent not in self.studs:
                self.studs.append(newStudent)
                newStudent.addCursus(self)

    def showStudents(self):
        print(self.naam)
        if len(self.studs) > 0:
            for stud in self.studs:
                print(f'Voornaam: {stud.vNaam}\nAchternaam: {stud.aNaam}\n'
                f'Leeftijd: {stud.leeftijd}\nID: {stud.adNum}\n')
        else:
            print('Geen studenten ingeschreven\n')



stud1 = Student('Jens','Coomans', (19,1,1990), 1)
stud2 = Student('Dario', 'Van Hasselt', (1,1,2000), 2)
stud3 = Student('Glenn', 'Silkens', (2,2,2000), 3)

curs1 = Cursus('Python', 1)
curs2 = Cursus('.Net', 2)
curs3 = Cursus('Wiskunde', 3)

stud1.addCursus(curs1, curs2, curs3)
curs2.addStudent(stud1, stud2, stud3)
stud3.addCursus(curs1)

stud1.showCursussen()
stud2.showCursussen()
stud3.showCursussen()

curs1.showStudents()
curs2.showStudents()
curs3.showStudents()