for x in range(1,21):
    for y in range(1,11):
        print((f"{x:>2} x{y:>2} ={x * y:>3}"), end='  ')
    print()

# 2 keer hetzelfde resultaat

for x in range(1,21):
    for y in range(1,11):
        print(("{:>2} x{:>2} ={:>3}").format(x,y,x*y), end='  ')
    print()