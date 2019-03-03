#!/usr/bin/python
#

# read the input from file
#with open('day8.txt', 'r') as f:
#    tree_str = f.read()
# use example input
tree_str = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

# read the input into an array of integers
#tree = list(map(int, tree_str.split(" ")))
# --> use list compr. instead
tree = [ int(i) for i in tree_str.split(" ") ]

def traverse(tree):
    n_child_nodes = tree[0]
    n_meta_entr = tree[1]
    meta_sum = 0

    for n in range(n_child_nodes):
        c_sum = traverse(tree[2:])
        meta_sum += c_sum
    for n in range(n_meta_entr):
        meta_sum += tree[2:][n]

    return meta_sum

meta_sum = traverse(tree)
print("metadata sum:", meta_sum)
