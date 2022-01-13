class Punt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

puntenLijst = []

for i in range(4):
    for j in range(4):
        p = Punt(i,j)
        puntenLijst.append((p.x,p.y))

print(puntenLijst)