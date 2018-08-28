# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other. 
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
from collections import defaultdict
import time
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


def size_of_largest_construction():
    biggest = 0
    for i in range(dim):
        j1 = 0
        while j1 < dim:
            if not grid[i][j1]:
                j1 += 1
                continue
            for j2 in range(j1, dim):
                if not grid[i][j2]:
                    break
                con = construction_size(i, j1, j2)
                if con > biggest:
                    biggest = con
            j1 = j2
            j1 += 1
    return biggest
    # Replace pass above with your code


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.

dict_size = defaultdict(lambda: 0)


def construction_size(i, j1, j2):
    local = dict_size[(i, j2, j2)] = dict_size[(i - 1, j2, j2)] + 1
    if j1 == j2:
        size_construction = local
    else:
        size_construction = dict_size[(i, j1, j2)] = dict_size[(i, j1, j2-1)] + local
    return size_construction

try:
    # for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed, n = 0, 4
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
time1 = time.time()
size = size_of_largest_construction()
time2 = time.time()
if not size:
    print(f'The largest block construction has no block.')  
elif size == 1:
    print(f'The largest block construction has 1 block.')  
else:
    print(f'The largest block construction has {size_of_largest_construction()} blocks.')  
print(time2 - time1)