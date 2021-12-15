fruitlist = ["appel", "banaan", "kers"]

try:
    num = input( "Geef een getal: " )
    if "." in num:
        num = float(num)
    else:      
        num = int(num)
    print(fruitlist[num])

except ValueError:
    print('Geen getal gegeven')

except TypeError:
    print('indices moeten integers of slices zijn.')

except IndexError:
    print('Index is te groot/klein')

except Exception as e:
    print( "Er ging iets fout" )
    print(e.args)







numlist = [100, 101, 0, "103", 104]

while True:

    try:
        i1 = int(input("Give an index: "))
        print("100 /", numlist[i1], "=", 100 / numlist[i1])
        break

    except ValueError:
        print('No round number given.')

    except IndexError:
        print('Index is too big/small.')

    except TypeError:
        print('Item in list is not an integer/float.')

    except ZeroDivisionError:
        print("You can't divide by 0. (Idiot!)")

    except Exception as e:
        print( "Something went wrong." )
        print(e.args)