#!/usr/bin/python
#
# improved version, basically from:
# - https://github.com/bengosney/Advent-Of-Code-2018/blob/master/AdventOfCode_2018_day_8.ipynb

# read the input from file
#with open('day8.txt', 'r') as f:
#    tree_str = f.read()
# use example input
tree_str = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# (result: 138)

tree = [ int(i) for i in tree_str.split(" ") ]

def traverse(tree):
    n_child_nodes, n_meta_entr = tree[:2]
    meta_sum = 0
    tree = tree[2:]
    for n in range(n_child_nodes):
        child_sum, tree = traverse(tree)
        meta_sum += child_sum

    meta_sum += sum(tree[:n_meta_entr])

    return meta_sum, tree[n_meta_entr:]

meta_sum, _ = traverse(tree)
print("metadata sum:", meta_sum)
