import re

with open('day10', 'r') as f:
    file = f.read()

map = [row for row in file.split('\n')]

for i, row in enumerate(map):
    if 'S' in row:
        start = (i, re.search('S', row).span()[0])

directions = {'Right': (0, 1),
              'Down': (1, 0),
              'Left': (0, -1),
              'Up': (-1, 0)}

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.


def find_next(x, y, direction):
    if direction == 'Right':
        if map[x][y] == '-':
            return x, y + 1, 'Right'
        elif map[x][y] == 'J':
            return x - 1, y, 'Up'
        elif map[x][y] == '7':
            return x + 1, y, 'Down'
    elif direction == 'Down':
        if map[x][y] == '|':
            return x + 1, y, 'Down'
        elif map[x][y] == 'L':
            return x, y + 1, 'Right'
        elif map[x][y] == 'J':
            return x, y - 1, 'Left'
    elif direction == 'Left':
        if map[x][y] == '-':
            return x, y - 1, 'Left'
        elif map[x][y] == 'L':
            return x - 1, y, 'Up'
        elif map[x][y] == 'F':
            return x + 1, y, 'Down'
    elif direction == 'Up':
        if map[x][y] == '|':
            return x - 1, y, 'Up'
        elif map[x][y] == '7':
            return x, y - 1, 'Left'
        elif map[x][y] == 'F':
            return x, y + 1, 'Right'
    return None, None, None


def valid(x, y):
    if x is not None:
        return 0 <= x < len(map) and 0 <= y < len(map[0])
    return False


starts = []
for i, direction in enumerate(directions):
    starts.append((i, start[0], start[1], direction))

for i, x, y, direction in starts:
    loop = {(start[0], start[1]): direction}
    x, y = x + directions[direction][0], y + directions[direction][1]
    loop[(x, y)] = direction
    while valid(x, y) and map[x][y] != 'S':
        x, y, direction = find_next(x, y, direction)
        loop[(x, y)] = direction
        # print((x, y), loop[(x, y)])
    if x is not None:
        print(starts[i])
        print(x, y, direction)
        print(len(loop), len(loop)/2)
        s = list(map[start[0]])
        if starts[i][3] == 'Right':
            if direction == 'Down':
                s[start[1]] = 'L'
            elif direction == 'Right':
                s[y] = '-'
            elif direction == 'Up':
                s[y] = 'F'
        elif starts[i][3] == 'Down':
            if direction == 'Left':
                s[y] = 'F'
            elif direction == 'Down':
                s[y] = '|'
            elif direction == 'Right':
                s[y] = '7'
        elif starts[i][3] == 'Left':
            if direction == 'Up':
                s[y] = '7'
            elif direction == 'Left':
                s[y] = '-'
            elif direction == 'Down':
                s[y] = 'J'
        elif starts[i][3] == 'Up':
            if direction == 'Right':
                s[y] = 'J'
            elif direction == 'Up':
                s[y] = '|'
            elif direction == 'Left':
                s[y] = 'L'
        map[x] = ''.join(s)
        break


# for line in map:
#     print(line)
# print('\n')


def adding(items, some_set):
    for _x, _y in items:
        some_set.add((_x, _y))
    return [], some_set


direction = None
x, y = (0, -1)
investigated = []
outside = set()
inside = set()


while True:
    y = y + 1
    if y == len(map[0]):
        investigated, outside = adding(investigated, outside)
        x, y = x + 1, 0
        if x == len(map):
            break
    if (x, y) in loop:
        if direction is None:
            if loop[(x, y)] in ['Up', 'Right']:
                direction = 'Up'
            else:
                direction = 'Down'
        if len(investigated) > 0:
            if loop[(x, y)] == direction:
                investigated, outside = adding(investigated, outside)
            elif loop[(x, y)] == 'Left':
                _, _, next_dir = find_next(x, y, 'Left')
                if next_dir == direction:
                    investigated, outside = adding(investigated, outside)
                else:
                    print(investigated)
                    investigated, inside = adding(investigated, inside)
            elif (direction == 'Up' and loop[(x, y)] == 'Right'
                  and map[x][y] == 'F'):
                investigated, outside = adding(investigated, outside)
            elif (direction == 'Down' and loop[(x, y)] == 'Right'
                  and map[x][y] == 'L'):
                investigated, outside = adding(investigated, outside)
            else:
                print(investigated)
                investigated, inside = adding(investigated, inside)
    else:
        investigated.append((x, y))

print(f'outside: {len(outside)}, inside: {len(inside)}')
