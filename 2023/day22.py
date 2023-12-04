import numpy as np
import re

np.set_printoptions(linewidth=150)

with open('day22', 'r') as f:
    file = f.read()

grid, instructions = file.split('\n\n')
grid = [list(row) for row in grid.split('\n')]
column_len = max([len(row) for row in grid])
instructions = re.split(r'(R|L)', instructions)

x_ranges = []
walls = set()
for r in range(len(grid)):
    if len(grid[r]) < column_len:
        grid[r].extend([' ']*(column_len - len(grid[r])))
    row = np.array(grid[r])
    x_ranges.append([np.where(row != ' ')[0][0],
                     np.where(row != ' ')[0][-1]])
    walls.update([(i, r) for i, wall in enumerate(row) if wall == '#'])

grid = np.array(grid)
y_ranges = []
for c, column in enumerate(grid.T):
    y_ranges.append([np.where(column != ' ')[0][0],
                     np.where(column != ' ')[0][-1]])

# y_ranges = [[] for c in range(column_len)]
# for c, column in enumerate(grid.T):
#     start = 0
#     while start < column_len:
#         if all(column[start:] == ' '):
#             break
#         start = (np.where(column[start:] != ' ')[0] + start)[0]
#         if not any(column[start:] == ' '):
#             y_ranges[c].append([start, column_len - 1])
#             break
#         end = (np.where(column[start:] == ' ')[0] + start)[0]
#         y_ranges[c].append([start, end - 1])
#         start = end
# check_grid = np.array(y_ranges[position[0]]) - position[1]
# y_range = y_ranges[position[0]][np.where(check_grid[:, 0] * check_grid[:, 1] <= 0)[0][0]]
# if position[1] < y_range[0] and (position[0], position[1]) not in walls:
#     position[1] = y_range[1]

position = np.array([x_ranges[0][0], 0])
# [x, y], top left is (0,0)
# orientations = {'N': 0, 'W': 90, 'S': 180, 'E': 270}
orientations = {0: np.array([0, -1]), 90: np.array([1, 0]), 180: np.array([0, 1]), 270: np.array([-1, 0])}
orientation = 90

for instruction in instructions:
    if instruction == 'R':
        orientation = (orientation + 90) % 360
    elif instruction == 'L':
        orientation = (orientation - 90) % 360
    else:
        for step in range(int(instruction)):
            next_pos = position + orientations[orientation]
            if orientation == 0:
                if next_pos[1] < y_ranges[position[0]][0]:
                    next_pos[1] = y_ranges[position[0]][1]
            elif orientation == 90:
                if next_pos[0] > x_ranges[position[1]][1]:
                    next_pos[0] = x_ranges[position[1]][0]
            elif orientation == 180:
                if next_pos[1] > y_ranges[position[0]][1]:
                    next_pos[1] = y_ranges[position[0]][0]
            else:  # orientation == 270:
                if next_pos[0] < x_ranges[position[1]][0]:
                    next_pos[0] = x_ranges[position[1]][1]
            if (next_pos[0], next_pos[1]) not in walls:
                position = next_pos
            else:
                break

points = {0: 3, 90: 0, 180: 1, 270: 2}
print(1000*(position[1]+1) + 4*(position[0]+1) + points[orientation])
