from shootergame.class_point import Point

class Character():
    def __init__(self, point: Point, width: int, height: int, health: int, firepower: int, speed: int):
        pass

class Player(Character):
    def __init__(self, point: Point, width: int, height: int, health: int, firepower: int, speed: int, armour: bool):
        self.armourBool = armour
        super().__init__(point, width, height, health, firepower, speed)
        pass

class Enemy(Character):
    def __init__(self, point: Point, width: int, height: int, health: int, firepower: int, speed: int):
        super().__init__(point, width, height, health, firepower, speed)
        pass