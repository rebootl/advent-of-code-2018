#!/usr/bin/python
#
# improved version, basically from:
# - https://github.com/bengosney/Advent-Of-Code-2018/blob/master/AdventOfCode_2018_day_8.ipynb

# read the input from file
with open('day8.txt', 'r') as f:
    tree_str = f.read()
# use example input
#tree_str = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# (result: 66)

tree = [ int(i) for i in tree_str.split(" ") ]

def traverse(tree):
    n_child_nodes, n_meta_entr = tree[:2]
    value = 0
    child_values = []

    tree = tree[2:]
    for n in range(n_child_nodes):
        child_value, tree = traverse(tree)
        child_values.append(child_value)

    if n_child_nodes == 0:
        value += sum(tree[:n_meta_entr])
    else:
        for i in tree[:n_meta_entr]:
            if i > 0 and i <= len(child_values):
                value += child_values[i-1]

    return value, tree[n_meta_entr:]

value, _ = traverse(tree)
print("value:", value)
