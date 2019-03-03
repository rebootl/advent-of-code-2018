#!/usr/bin/python
#
import re

with open('day3-input.txt', 'r') as f:
    input_list = list(f)
#input_list = '''#1 @ 1,3: 4x4
##2 @ 3,1: 4x4
##3 @ 5,5: 2x2'''.splitlines()

f_x = [ 0 for n in range(1, 1000) ]
fabric = [ f_x.copy() for n in range(1, 1000) ]

r = re.compile('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')

for line in input_list:
    id, x, y, width, height = [ int(v) for v in r.findall(line)[0] ]
    for h in range(height):
        for w in range(width):
            fabric[y+h][x+w] += 1

# p1
count = 0
for line in fabric:
    for char in line:
        if char >= 2:
            count += 1
print(count)

# p2
for line in input_list:
    id, x, y, width, height = [ int(v) for v in r.findall(line)[0] ]
    check = True
    for h in range(height):
        for w in range(width):
            if fabric[y+h][x+w] > 1:
                check = False
    if check == True:
        print(id)
        break
