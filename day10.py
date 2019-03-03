#!/usr/bin/python
#
#
#
#

# parse values
# parsing into two arrays [ (x0, y0).. ], [ (vx0, vy0)..]
positions = []
velocities = []
with open('day10-input.txt', 'r') as f:
    for l in f:
        positions.append((int(l[10:16]), int(l[18:24])))
        velocities.append((int(l[36:38]), int(l[40:42])))

# (debug-print)
#print(positions)
#print(velocities)

def plot(pos_xs, pos_ys):
    min_y = min(pos_ys)
    min_x = min(pos_xs)
    pos = [ (pos_xs[i], pos_ys[i]) for i in range(len(pos_ys)) ]
    # corr.: this i don't need actually, but should work as well
    #pos_y_norm = [ y - min_y for y in pos_ys ]
    #pos_x_norm = [ x - min_x for x in pos_xs ]
    for y in range(min_y, min_y+10):
        l = ""
        for x in range(min_x, min_x+80):
            if (x, y) in pos:
                l += "#"
            else:
                l += "."
        print(l)

pos_ys = [ p[1] for p in positions ]
pos_xs = [ p[0] for p in positions ]
l = len(positions)
step = 1
while True:
    # corr.: must use + here, it's moving forward in time
    pos_ys = [ pos_ys[i] + velocities[i][1] for i in range(l) ]
    #pos_xs = [ pos_xs[i] + velocities[i][0] * step for i in range(l) ]
    dy = max(pos_ys) - min(pos_ys)
    #dx = max(pos_xs) - min(pos_xs)

    if dy < 10:
        print("step: {} dy: {} dx: {}".format(step, dy, "None"))
        # putting this here instead saves about 1s
        pos_xs = [ pos_xs[i] + velocities[i][0] * step for i in range(l) ]
        plot(pos_xs, pos_ys)
        break

    dy0 = dy
    step += 1
