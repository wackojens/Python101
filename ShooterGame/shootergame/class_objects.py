from shootergame.class_point import Point

class Objects():
    def __init__(self, point: Point, height: int, width: int):
        self.point = point
        self.height = height
        self.width = width
        self.checkTypeValues()
        self.x = point.x
        self.y = point.y
        self.size = self.width * self.height

    def checkTypeValues(self):
        if not isinstance(self.point, Point) or not isinstance(self.height, int) or not isinstance(self.width, int):
            raise TypeError("Height and width need to be integers. Point needs to be an instance of the Point class")





class Rock(Objects):
    def __init__(self, point: Point, height: int, width: int):
        super().__init__(point, height, width)
        self.checkSize()

    def checkSize(self):
        if self.height < 4 or self.height > 20 or self.width < 4 or self.width > 20:
            raise ValueError("Both Rock Height and width need to be between 4 and 20")





class Damageable(Objects):
    def __init__(self, point: Point, height: int, width: int, health: int):
        self.health = health
        super().__init__(point, height, width)
        self.checkTypeHealth

    def checkTypeHealth(self):
        if not isinstance(self.health, int):
            raise TypeError("Health needs to be an integer")





class Building(Damageable):
    def __init__(self, point: Point, height: int, width: int, health: int):
        super().__init__(point, height, width, health)
        self.checkSize()
        self.checkHealth()

    def checkSize(self):
        if self.height < 10 or self.height > 40 or self.width < 10 or self.width > 40:
            raise ValueError("Both Building Height and width need to be between 10 and 40")

    def checkHealth(self):
        if self.health < 150 or self.health > 300:
            raise ValueError("Building health has to be between 150 and 300")





class Crate(Damageable):
    def __init__(self, point: Point, height: int, width: int, health: int, armour: bool):
        self.armourBool = armour
        super().__init__(point, height, width, health)
        self.checkTypeArmour()
        self.checkSize()
        self.checkHealth()
        self.checkArmour()

    def checkTypeArmour(self):
        if not isinstance(self.armourBool, bool):
            raise TypeError("Armour needs to be passed as a boolean (True or False)")

    def checkSize(self):
        if self.height != 10 or self.height != self.width:
            raise ValueError("Crate's height and width need to be 10")

    def checkHealth(self):
        if self.health < 40 or self.health > 50:
            raise ValueError("Crate health needs to be between 40 and 50")

    def checkArmour(self):
        if self.armourBool:
            self.armourValue = self.health * 0.2
        else:
            self.armourValue = 0