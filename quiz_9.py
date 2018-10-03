# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from queue_adt import *


def display_grid():
    for row in grid:
        print('    ', *row)


def get_children(grid, point):
    """
    >>> grid = [['NW', 'SW', 'NE', 'NW', 'SE', 'NE', 'NE'],\
                ['NE', 'SW', 'NW', 'SE', 'NW', 'NE', 'SE'],\
                ['NE', 'SE', 'NW', 'SW', 'SE', 'NW', 'SE'],\
                ['NE', 'SE', 'NW', 'SE', 'SE', 'NE', 'NE'],\
                ['SE', 'SE', 'SE', 'SE', 'SW', 'SW', 'SE'],\
                ['SE', 'SE', 'SE', 'NW', 'SW', 'NE', 'SW'],\
                ['SW', 'SE', 'SE', 'SW', 'NE', 'SW', 'SE']]
    >>> get_children(grid, (3, 3))
    [(4, 4), (4, 3), (3, 4)]
    >>> get_children(grid, (0, 0))
    [(-1, -1), (-1, 0), (0, -1)]
    >>> get_children(grid, (0, 6))
    [(-1, 7), (-1, 6), (0, 7)]
    >>> get_children(grid, (6, 0))
    [(7, -1), (7, 0), (6, -1)]
    >>> get_children(grid, (6, 6))
    [(7, 7), (7, 6), (6, 7)]
    """
    operators = {
        'N': lambda p: (p[0], p[1] - 1),
        'S': lambda p: (p[0], p[1] + 1),
        'W': lambda p: (p[0] - 1, p[1]),
        'E': lambda p: (p[0] + 1, p[1]),
    }
    x, y = point[0], point[1]
    direction = grid[y][x]
    return [operators[direction[1]](operators[direction[0]](point)), operators[direction[1]](point), operators[direction[0]](point)]


def shortest_path_in_dijkstra(grid, destination):
    """
    >>> grid = [['SW', 'SW', 'NE', 'NW', 'SE', 'NE', 'SE'],\
                ['NE', 'SW', 'NW', 'SE', 'NW', 'NE', 'SE'],\
                ['NE', 'SE', 'NW', 'SW', 'SE', 'NW', 'SE'],\
                ['NE', 'SE', 'NW', 'SE', 'SE', 'NE', 'NE'],\
                ['SE', 'SE', 'SE', 'SE', 'SW', 'SW', 'SE'],\
                ['SE', 'SE', 'SE', 'NW', 'SW', 'NE', 'SW'],\
                ['NW', 'SE', 'SE', 'SW', 'NE', 'SW', 'SW']]
    >>> shortest_path_in_dijkstra(grid, (0, 0))
    [(3, 3), (4, 3), (5, 3), (5, 2), (4, 1), (3, 1), (3, 2), (2, 2), (1, 1), (0, 1), (0, 0)]
    >>> shortest_path_in_dijkstra(grid, (6, 0))
    [(3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (6, 0)]
    >>> shortest_path_in_dijkstra(grid, (6, 6))
    [(3, 3), (4, 3), (5, 4), (5, 5), (6, 5), (6, 6)]
    >>> shortest_path_in_dijkstra(grid, (0, 6))
    []
    """
    centre = (3, 3)
    q = Queue()
    visited_point = set()
    pre_point = dict()
    path = []

    q.enqueue(centre)
    visited_point.add(centre)
    while not q.is_empty():
        p = q.dequeue()
        children = get_children(grid, p)
        if destination in children:
            pre_point[destination] = p
            break
        for i in children:
            if 0 <= i[0] <= len(grid)-1 and 0 <= i[1] <= len(grid)-1:
                if i not in visited_point and i not in corners:
                    q.enqueue(i)
                    pre_point[i] = p
                    visited_point.add(i)

    if pre_point.get(destination) is None:
        return path

    path.append(destination)
    pre = destination
    while True:
        pre = pre_point.get(pre)
        path.append(pre)
        if pre == centre:
            break

    return path[::-1]


def preferred_paths_to_corners():
    paths = dict()
    for i in corners:
        path = shortest_path_in_dijkstra(grid, i)
        if len(path)>0:
            paths[i] = path
    return paths


try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
