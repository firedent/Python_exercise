# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys
from queue import Queue


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def visit_point(start_point, chess_set):
    i, j = start_point[0], start_point[1]
    a, b = 1, 2
    visited = []
    for _ in range(2):
        a, b = b, a
        for _ in range(2):
            a = a*-1
            for _ in range(2):
                b = b*-1
                v_i, v_j = i+a, j+b
                if (v_i, v_j) in chess_set:
                    if grid[v_i][v_j] == 1:
                        visited.append((v_i, v_j))
    return visited


def explore_board():
    chess = 0
    chess_set = set()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                chess += 1
                chess_set.add((i, j))

    print(f'chess:{chess}')
    num = 0
    while len(chess_set) != 0:
        q = set()
        q.add(chess_set.pop())
        while len(q) != 0:
            going_visit = q.pop()
            visited = visit_point(going_visit, chess_set)
            for i in visited:
                chess_set.remove(i)
                q.add(i)
        num += 1
    return num


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    # for_seed, n = 0, -6
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
# grid = [[0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 1, 0, 0]]
# print(grid)
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')

