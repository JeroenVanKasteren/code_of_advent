import re
import numpy as np

with open('day11', 'r') as f:
    file = f.read().split('\n')

grid = []
for row in file:
    if re.search('#', row) is None:
        grid.append(row)
    grid.append(row)
file_t = [''.join(c) for c in list(zip(*grid))]
grid_t = []
for column in file_t:
    if re.search('#', column) is None:
        grid_t.append(column)
    grid_t.append(column)
grid = [''.join(r) for r in list(zip(*grid_t))]


def get_galaxies(grid):
    galaxies = set()
    for r, row in enumerate(grid):
        for item in list(re.finditer('#', row)):
            galaxies.add((r, item.span()[0]))
    return galaxies


galaxies = get_galaxies(grid)
res = 0
other_galaxies = galaxies.copy()
for galaxy in galaxies:
    other_galaxies.remove(galaxy)
    for other_galaxy in other_galaxies:
        res += (abs(galaxy[0] - other_galaxy[0]) +
                abs(galaxy[1] - other_galaxy[1]))
print(res)

# Part 2

expanded_rows = []
for r, row in enumerate(file):
    if re.search('#', row) is None:
        expanded_rows.append(r)
file_t = [''.join(c) for c in list(zip(*file))]
expanded_columns = []
for c, column in enumerate(file_t):
    if re.search('#', column) is None:
        expanded_columns.append(c)
galaxies = get_galaxies(file)


def count_inbetween(start, end, expanded):
    return len([j for j in expanded if (start < j < end) or
                (end < j < start)])


res = 0
distance = 1000000 - 1
other_galaxies = galaxies.copy()
for galaxy in galaxies:
    other_galaxies.remove(galaxy)
    for other_galaxy in other_galaxies:
        expansions = count_inbetween(galaxy[0], other_galaxy[0], expanded_rows)
        res += (abs(galaxy[0] - other_galaxy[0])
                + distance * expansions)
        expansions = count_inbetween(galaxy[1], other_galaxy[1], expanded_columns)
        res += (abs(galaxy[1] - other_galaxy[1])
                + distance * expansions)
print(res)
