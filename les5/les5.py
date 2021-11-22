for x in range(1,21):
    for y in range(1,11):
        print(("{:>2} x{:>2}={:>3}").format(x,y,x*y), end='  ')
    print()