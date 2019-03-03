#!/usr/bin/python
#
# idea from:
# - https://github.com/bengosney/Advent-Of-Code-2018/blob/master/AdventOfCode_2018_day_1.ipynb

with open('day1-input.txt', 'r') as f:
    freq = sum([ int(l) for l in list(f) ])

print("res. freq:", freq)
