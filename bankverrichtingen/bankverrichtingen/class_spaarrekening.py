from bankverrichtingen.class_rekening import Rekening


class Spaarrekening(Rekening):
    def __init__(self) -> None:
        super().__init__()  
    
    def overschrijven(self):
        pass

    def onderNul(self):
        pass