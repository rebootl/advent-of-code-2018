#!/usr/bin/python
#

with open('day6-input.txt', 'r') as f:
    in_str = f.read().strip("\n")

# example
#in_str = '''1, 1
#1, 6
#8, 3
#3, 4
#5, 5
#8, 9'''
# result: 17

#print(in_str)

coordinates = []
coords_x = []
coords_y = []
for l in in_str.splitlines():
    x, y = l.split(",")
    coordinates.append((int(x), int(y)))
    coords_x.append(int(x))
    coords_y.append(int(y))

max_x = max(coords_x)
max_y = max(coords_y)

# (x1, y1) => A
# (x2, y1) => B
# (x3, y1) => B

def manhat_dist(l, c):
    d_x = abs(c[0] - l[0])
    d_y = abs(c[1] - l[1])
    return d_x + d_y

locations = {}
for x in range(0, max_x+1):
    for y in range(0, max_y+1):
        min_dist = 1000000
        for idx, c in enumerate(coordinates):
            #dist = manhat_dist((x, y), c)
            dist = abs(c[0] - x) + abs(c[1] - y)
            if dist < min_dist:
                min_dist = dist
                nearest_idx = idx
            elif dist == min_dist:
                nearest_idx = "."
                #break # don't, there could be smaller values (thx maja)
        locations[(x,y)] = nearest_idx

#print(coordinates)
#print(max_x)
#print(max_y)
#print(manhat_dist((2,5), coordinates[4]))
#print(locations)

# print picture
#for y in range(0, max_y+1):
#    str_x = ""
#    for x in range(0, max_x+1):
#        str_x += str(locations[(x,y)])
#    print(str_x)

# find largest area that is not infinite
infinites = set()
areas = {}
for l in locations:
    if locations[l] in infinites:
        continue
    if l[0] == 0 or l[0] == max_x or l[1] == 0 or l[1] == max_y:
        infinites.add(locations[l])
        continue
    if locations[l] in areas:
        areas[locations[l]] += 1
    else:
        areas[locations[l]] = 1
#print(areas)
max_area = 0
for a in areas.values():
    if a > max_area:
        max_area = a
print(max_area)
