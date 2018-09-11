# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def visit_point(start_point):
    i, j = start_point[0], start_point[1]
    visited = []
    if not 0<= i<len(grid) or not 0<=j<len(grid):
        return visited
    if grid[i][j] == 0:
        return visited
    grid[i][j] = 0
    visited = [(i, j)]
    a, b = 1, 2
    for _ in range(2):
        a, b = b, a
        for _ in range(2):
            a = a*-1
            for _ in range(2):
                b = b*-1
                v_i, v_j = i+a, j+b
                for v in visit_point((v_i, v_j)):
                    visited.append(v)
    return visited


def explore_board():
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if len(visit_point((i, j))) != 0:
                num += 1
    return num


try:
#    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    for_seed, n = 0, 3
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
# grid = [[True for _ in range(dim)] for _ in range(dim)]

print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')
