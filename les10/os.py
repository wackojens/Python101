import os

from os import listdir
flist = listdir( "." )
print(type(flist))
flist.sort(key=lambda naam: (str(naam)))
for naam in flist:
        print( naam )
