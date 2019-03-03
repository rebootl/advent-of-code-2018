#!/usr/bin/python
#

with open('day5-input.txt', 'r') as f:
    in_str = f.read().strip("\n")

# example str.
#in_str = "dabAcCaCBAcCcaDA"
# result: 10

loop = True
ptr = 0
remaining_length = len(in_str)
while loop == True:
    for i in range(remaining_length):
        #print(i, ptr)
        if in_str[ptr] == in_str[ptr+1].swapcase():
            #print(in_str)
            in_str = in_str[:ptr] + in_str[ptr+2:]
            #print(in_str)
            if ptr > 2:
                ptr -= 2
                break
            else: ptr = 0
            break
        ptr += 1
        remaining_length = len(in_str) - ptr
        if remaining_length == 1:
            loop = False
            break

print(len(in_str))
print(in_str)
