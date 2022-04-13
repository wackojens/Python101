class Point():
    def __init__(self, x:int = 0, y:int = 0):
        self.x = x
        self.y = y
        self.checkValues()
    
    def checkValues(self):
        if not isinstance(self.x, int) or not isinstance(self.y, int):
            raise TypeError("Point coordinates have to be integers")
        if self.x < 0 or self.y < 0:
            raise ValueError("Point coordinates have to be positive")
    
    def translation(self, deltaX: int = 10, deltaY: int = 10, speed: int = 1):
        if not isinstance(deltaX, int) or not isinstance(deltaY, int) or not isinstance(speed, int):
            raise TypeError("Point translation values and speed need to be integers")
        if deltaX > 10 or deltaX < -10 or deltaY > 10 or deltaY < -10 or speed < 1 or speed > 5:
            raise ValueError("Point translation values need to be between -10 and 10 and speed needs to be between 1 and 5")
        deltaX *= speed
        deltaY *= speed
        self.x += deltaX
        self.y += deltaY