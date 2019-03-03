#!/usr/bin/python
#

with open('day1-input.txt', 'r') as f:
    changelist = [ int(i.strip()) for i in list(f) ]

# remark: list(f) is equal to f.readlines()

# (debug print)
#print(changelist)

freq = 0
for c in changelist:
    freq += c

print("res. freq:", freq)
