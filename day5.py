#!/usr/bin/python
#

with open('day5-input.txt', 'r') as f:
    in_str = f.read().strip("\n")

# example str.
#in_str = "dabAcCaCBAcCcaDA"
# result: 10

loop = True
while loop == True:
    for i, c in enumerate(in_str):
        #print(len(in_str))
        if i+1 == len(in_str):
            loop = False
            break
        if c == in_str[i+1].swapcase():
            in_str = in_str[:i] + in_str[i+2:]
            break

print(len(in_str))
