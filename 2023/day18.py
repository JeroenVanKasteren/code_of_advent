import numpy as np

with open('day18', 'r') as f:
    file = f.read().split('\n')

plan = [line.split(' ')[:2] for line in file]

x_min, y_min, x_max, y_max = 0, 0, 0, 0
x, y = 0, 0
cycle = {(x, y): [plan[0][0], 0]}  # start will be overwritten
order_cycle = {0: (x, y)}  # start will be overwritten

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

for d, i in plan:
    for dig in range(int(i)):
        x, y = x + dirs[d][0], y + dirs[d][1]
        cycle[(x, y)] = [d, len(cycle)]
        order_cycle[len(order_cycle)] = (x, y)
        x_min, x_max = min(x, x_min), max(x, x_max)
        y_min, y_max = min(y, y_min), max(y, y_max)


def get_dir(x, y):
    cur_d, cur_n = cycle[(x, y)]
    if cur_d in ['U', 'D']:
        return cur_d
    else:
        prev_dir = cycle[order_cycle[(cur_n - 1) % (len(cycle) + 1)]][0]
        if prev_dir in ['U', 'D']:
            return prev_dir
        next_dir = cycle[order_cycle[(cur_n + 1) % (len(cycle) + 1)]][0]
        if next_dir in ['U', 'D']:
            return next_dir


inside = set()

for x in range(x_min, x_max + 1):
    inside_sign = -1
    on_cycle = False
    dir_cycle = '0'
    for y in range(y_min, y_max + 1):
        if (x, y) in cycle:
            if not on_cycle:
                on_cycle = True
                dir_cycle = get_dir(x, y)
        else:
            if on_cycle and dir_cycle == get_dir(x, y - 1):
                inside_sign = -inside_sign
            on_cycle = False
            if inside_sign == 1:
                inside.add((x, y))
print(len(cycle) + len(inside))

map = [['.' for _ in range(y_max - y_min + 1)]
       for _ in range(x_max - x_min + 1)]
for x, y in cycle:
    map[x - x_min][y - y_min] = cycle[(x, y)][0]
for x, y in inside:
    map[x - x_min][y - y_min] = '+'
for line in map:
    print(''.join(line))

# Part 2

dirs_code = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
plan = [line.split(' ') for line in file]
corners = []
x, y = 0, 0
x_values = [x]

for _, i, hex_str in plan:
    d = dirs_code[hex_str[-2]]
    dist = sum([int(x, 16) * 16 ** (5 - j - 1)
                for j, x in enumerate(hex_str[2:-2])])
    x_n, y_n = x + dirs[d][0]*dist, y + dirs[d][1]*dist
    if d in ['D', 'U']:
        corners.append((min(x, x_n), y, max(x, x_n), y_n))
    x, y = x_n, y_n
    x_values.append(x)

corners = np.array(corners)
res = 0
x_values = sorted(list(set(x_values)))
x = x_values.pop(0)
while len(x_values) > 0:
    ys = []
    for corner in corners:
        if corner[0] <= x <= corner[1]:
            ys.append(y)
    x_next = x_values.pop(0)
    for i in range(0, len(ys), 2):
        res += (ys[i+1] - ys[i]) * (x_next - x)
    x = x_next
print(res)
