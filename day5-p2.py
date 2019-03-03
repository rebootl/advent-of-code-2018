#!/usr/bin/python
#

with open('day5-input.txt', 'r') as f:
    in_str = f.read().strip("\n")

# example str.
#in_str = "dabAcCaCBAcCcaDA"
# result: 10

def react(p):
    loop = True
    ptr = 0
    remaining_length = len(p)
    while loop == True:
        for i in range(remaining_length):
            #print(i, ptr)
            if p[ptr] == p[ptr+1].swapcase():
                #print(in_str)
                p = p[:ptr] + p[ptr+2:]
                #print(in_str)
                if ptr > 2:
                    ptr -= 2
                    break
                else: ptr = 0
                break
            ptr += 1
            remaining_length = len(p) - ptr
            if remaining_length == 1:
                loop = False
                return len(p)

print(len(in_str))
print(react(in_str))
#print(in_str)

results = []
for c in range(ord("a"), ord("z")+1):
    # remove lowercase
    polymer = in_str.replace(chr(c), '')
    # remove uppercase
    polymer = polymer.replace(chr(c).upper(), '')
    # react polymer
    #print("removed:", chr(c))
    #print(polymer)
    #print("-----")
    n = react(polymer)
    results.append(n)

print(min(results))
