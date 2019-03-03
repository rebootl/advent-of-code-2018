#!/usr/bin/python
#

freq = 0

with open('day1-input.txt', 'r') as f:
    for l in f:
        freq += int(l.strip())

print("res. freq:", freq)
