#!/usr/bin/python
#

# read in map
with open('day13-input.txt', 'r') as f:
    map_rawdata = f.read()
###
# result: 8,9
# example input
#map_rawdata = r'''/->-\
#|   |  /----\
#| /-+--+-\  |
#| | |  | v  |
#\-+-/  \-+--/
#  \------/   '''
###
# result: 7,3
#map_rawdata = r'''/>-<\
#|   |
#| /<+-\
#| | | v
#\>+</ |
#  |   ^
#  \<->/'''
###
# result: 6,4

map_data = map_rawdata.split("\n")

class Cart:
    def __init__(self, x, y, o_in):
        # position
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        # orientation
        # 0 ">", 1 "v", 2 "<", 3 "^"
        if o_in == ">":
            self.orientation = 0
        elif o_in == "v":
            self.orientation = 1
        elif o_in == "<":
            self.orientation = 2
        elif o_in == "^":
            self.orientation = 3
        else:
            print("init orient. err.")
        # steering position
        # 0 left, 1 straight, 2 right
        self.steer_pos = 0
        self.collided = False
    def move(self):
        # move 1 step in the curr. orient.
        if self.orientation == 0:
            self.x += 1
        elif self.orientation == 1:
            self.y += 1
        elif self.orientation == 2:
            self.x -= 1
        elif self.orientation == 3:
            self.y -= 1
        self.pos = (self.x, self.y)
        # get the new map input
        map_input = map_data[self.y][self.x]
        #print(map_input)
        # update the orientation acc. to the map inp
        if map_input == "\\":
            if self.orientation == 0:
                self.orientation = 1
            elif self.orientation == 2:
                self.orientation = 3
            elif self.orientation == 1:
                self.orientation = 0
            elif self.orientation == 3:
                self.orientation = 2
        elif map_input == "/":
            if self.orientation == 0:
                self.orientation = 3
            elif self.orientation == 2:
                self.orientation = 1
            elif self.orientation == 1:
                self.orientation = 2
            elif self.orientation == 3:
                self.orientation = 0
        elif map_input == "+":
            if self.steer_pos == 0:
                self.orientation -= 1
            elif self.steer_pos == 2:
                self.orientation += 1
            if self.orientation < 0:
                self.orientation = 3
            elif self.orientation > 3:
                self.orientation = 0
            self.steer_pos += 1
            if self.steer_pos > 2:
                self.steer_pos = 0
    def get_res(self):
        return "{},{}".format(self.x, self.y)
    def __str__(self):
        return "cart object pos: {} orient: {} steer_pos: {} coll: {}".format(
            self.pos, self.orientation, self.steer_pos, self.collided
        )

def init_carts():
    '''creates the carts'''
    global carts
    carts = []
    for l_num, l in enumerate(map_data):
        for c_num, c in enumerate(l):
            if c == ">" or c == "<" or c == "^" or c == "v":
                cart = Cart(c_num, l_num, c)
                carts.append(cart)

def run():
    init_carts()
    while True:
        positions = []
        for cart in carts:
            cart.move()
            if cart.pos in positions:
                return cart.get_res()
            positions.append(cart.pos)

def run_p2():
    init_carts()
    global carts
    while True:
        carts = sorted(carts, key=lambda x: x.pos)
        for cart in carts:
            cart.move()
            #print(cart)
            for cart_ in carts:
                if cart.pos == cart_.pos and not cart_.collided and \
                    cart != cart_:
                    cart.collided = True
                    cart_.collided = True
                    break
            #print(cart)
        carts_new = []
        for cart in carts:
            if cart.collided == False:
                carts_new.append(cart)
        print(len(carts_new))
        if len(carts_new) < 2:
            return carts_new[0].get_res()
        carts = carts_new

print(run())
print(run_p2())
