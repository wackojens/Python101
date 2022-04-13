set3 = set()
set7 = set()
set11 = set()
set3711 = set()
set37 = set()
setRest = set()

for i in range(1,1001):
    if i % 3 == 0:
        set3.add(i)
    if i % 7 == 0:
        set7.add(i)
    if i % 11 == 0:
        set11.add(i)
    if i % 3 == 0 and i % 7 == 0 and i % 11 == 0:
        set3711.add(i)
    if i % 3 == 0 and i % 7 == 0 and i % 11 != 0:
        set37.add(i)
    if i % 3 != 0 and i % 7 != 0 and i % 11 != 0:
        setRest.add(i)

print(set3)
print(set7)
print(set11)
print(set3711)
print(set37)
print(setRest)

setcompr3 = {i for i in range(1,1001) if i % 3 == 0}
setcompr7 = {i for i in range(1,1001) if i % 7 == 0}
setcompr11 = {i for i in range(1,1001) if i % 11 == 0}
setcompr3711 = {i for i in range(1,1001) if i % 3 == 0 and i % 7 == 0 and i % 11 == 0}
setcompr37 = {i for i in range(1,1001) if i % 3 == 0 and i % 7 == 0 and i % 11 != 0}
setcomprRest = {i for i in range(1,1001) if i % 3 != 0 and i % 7 != 0 and i % 11 != 0}
print(setcompr3)
print(setcompr7)
print(setcompr11)
print(setcompr3711)
print(setcompr37)
print(setcomprRest)