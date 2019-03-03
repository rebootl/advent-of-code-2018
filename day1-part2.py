#!/usr/bin/python
#

with open('day1-input.txt', 'r') as f:
    changelist = [ int(i.strip()) for i in list(f) ]

# remark: list(f) is equal to f.readlines()

# (debug print)
#print(changelist)

freq = 0
frequencies = { freq }
lcount = 0
reloop = True
while reloop:
    lcount += 1
    print(lcount)
    for c in changelist:
        freq += c
        if freq in frequencies:
            reloop = False
            break
        frequencies.add(freq)

print("res. freq:", freq)
