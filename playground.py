# coding=utf-8
# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def leftmost_longest_path_from_top_left_corner():
    path = []
    new_directions = {'': ['s', 'e'], 'n': ['e', 'n', 'w'], 'e': ['s', 'e', 'n'], 's': ['w', 's', 'e'],
                      'w': ['n', 'w', 's']}
    distance_dirt = {'n': (0, -1), 'e': (1, 0), 's': (0, 1), 'w': (-1, 0)}
    if grid[0][0] != 0:
        paths_quene = Queue()
        paths_quene.enqueue(([(0, 0)], ['s', 'e']))
        while not paths_quene.is_empty():
            node = paths_quene.dequeue()
            path = node[0]
            destinaton = path[-1]
            for direction in node[1]:
                distance = distance_dirt.get(direction)

                new_destinaton = (destinaton[0] + distance[1], destinaton[1] + distance[0])

                directions = new_directions.get(direction)

                if (new_destinaton[0] not in range(10)) | (new_destinaton[1] not in range(10)):
                    continue
                print(new_destinaton[0], new_destinaton[1])
                if grid[new_destinaton[0]][new_destinaton[1]] == 0:
                    continue
                if new_destinaton in path:
                    continue

                new_path = path.copy()
                new_path.append(new_destinaton)
                new_node = (new_path, directions)
                paths_quene.enqueue(new_node)

    return path


provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')

