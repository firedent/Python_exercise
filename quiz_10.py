# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree_adt import *

def _print_growing_up(tree, heigh, l):
    if heigh < 0:
        return
    if tree is None:
        tree = BinaryTree()
    _print_growing_up(tree.left_node, heigh - 1, l)
    v = tree.value
    if v is None:
        v = 'x'
    base = 2**heigh-1
    if l[heigh] == '':
        l[heigh] = ' '*base+str(v)
    else:
        l[heigh] = l[heigh]+' '*(base*2+1)+str(v)
    _print_growing_up(tree.right_node, heigh-1, l)


def print_growing_up(tree, heigh):
    l = ['']*(heigh+1)
    _print_growing_up(tree, heigh, l)
    for i in l:
        print(i.rstrip())


try:
    # seed_arg, nb_of_nodes = (int(x) for x in
    #                           input('Enter two integers, with the second one between 0 and 10: '
    #                                ).split()
    #                         )
    seed_arg, nb_of_nodes = 0, 10
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
print_growing_up(tree, tree.height())
