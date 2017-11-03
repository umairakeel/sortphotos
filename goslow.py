from __future__ import print_function
import os


print (" Starting a scan")

total = 0
d = 0
f = 0

folder = "/Users/umairakeel/Desktop/ul/OLD PICTURES"
for root, dirs, files in os.walk(folder):
    d = d+1
    print ( 'R -> ' +  root )
    print ( 'D -> ')
    print ( dirs )
    print ( files )
    total += len(files)
    f = f+len(files)

print ( "Total " + str(total))
print ( "Directories " + str ( d ) ) 
print ( " Done " )
