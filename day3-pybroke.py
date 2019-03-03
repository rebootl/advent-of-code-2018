#!/usr/bin/python
#

f_x = [ 0 for n in range(1, 10) ]
fabric = [ f_x.copy() for n in range(1, 10) ]

for l in fabric:
    print(l)

print("---")

fabric[5][4] = 1

for l in fabric:
    print(l)
