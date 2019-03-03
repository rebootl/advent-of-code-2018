#!/usr/bin/python
#
#



with open('day2-input.txt', 'r') as f:
    lines = [ l.strip() for l in list(f) ]
#
#lines = '''abcdef
#bababc
#abbcde
#abcccd
#aabcdd
#abcdee
#ababab'''
#lines = lines.splitlines()
# example res.: 12
lines_ = '''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz'''
lines_ = lines_.splitlines()
# example res.: fgij
#print(lines)

n_two_letters = 0
n_three_letters = 0

for line in lines:
    strcheck = {}
    for c in line:
        if c not in strcheck.keys():
            strcheck[c] = 1
        else:
            strcheck[c] += 1
    match_two = False
    match_three = False
    #print(line)
    for v in strcheck.values():
        if not match_two and v == 2:
            print("match two")
            n_two_letters += 1
            match_two = True
        if not match_three and v == 3:
            print("match three")
            n_three_letters += 1
            match_three = True
        if match_two and match_three:
            break

print("res:", n_two_letters*n_three_letters)

lines_match = []
found = False
for line in lines:
    for line_ in lines:
        if line != line_:
            diff_c = 0
            for i, c in enumerate(line):
                #print("comp {} {}".format(c, line_[i]))
                if c != line_[i]:
                    diff_c += 1
                if diff_c > 1: break
            #print(diff_c)
            if diff_c == 1:
                lines_match.append(line)
                lines_match.append(line_)
                found = True
                break
    if found: break
print(lines_match)
for n, c in enumerate(lines_match[0]):
    if c != lines_match[1][n]:
        x = n
        print(x)
        break
res = lines_match[0][:x] + lines_match[0][x+1:]
print("res2:", res)
