class Map():
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.checkTypeValues()
        self.checkSize()
        self.size = self.width * self.height
    
    def checkTypeValues(self):
        if not isinstance(self.height, int) or not isinstance(self.width, int):
            raise TypeError("Height and width need to be of type integer")

    def checkSize(self):
        if self.height < 1000 or self.height > 5000 or self.width < 1000 or self.width > 5000:
            raise ValueError("The height and width of the map need to be between 1000 and 5000")
