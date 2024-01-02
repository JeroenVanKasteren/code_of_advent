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
# for line in map:
#     print(''.join(line))

# Part 2

dirs_code = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
plan = [line.split(' ') for line in file]
corners = []
x, y = 0, 0
x_values = [x]

for d, i, _ in plan:
    x_n, y_n = x + int(i) * dirs[d][0], y + int(i) * dirs[d][1]
for _, i, hex_str in plan:
    d = dirs_code[hex_str[-2]]
    dist = sum([int(x, 16) * 16 ** (5 - j - 1)
                for j, x in enumerate(hex_str[2:-2])])
    x_n, y_n = x + dirs[d][0]*dist, y + dirs[d][1]*dist
    if d in ['D', 'U']:
        corner = (min(x, x_n), y, max(x, x_n), y_n)
        corners.append(tuple([np.int64(z) for z in corner]))
    x, y = x_n, y_n
    x_values.append(x)

corners = np.array(corners)
res = 0
x_values = sorted(list(set(x_values)))
x = x_values.pop(0)
while len(x_values) > 0:
    corners_on = []
    for corner in corners:
        if corner[0] <= x <= corner[2]:
            corners_on.append(corner)
    corners_on = sorted(corners_on, key=lambda x: x[1])
    x_next = x_values.pop(0)
    i = 0
    # if x == -201:
    #     pass
    # if j >= len(corners_on):
    #     pass
    while i < len(corners_on):
        # First, calculate the blocks between the corners on x level
        j = i + 1
        # if not both added or removed
        if not ((corners_on[i][0] == x and corners_on[j][0] == x)
                or (corners_on[i][2] == x and corners_on[j][2] == x)):
            # first added or removed (implies second removed or added)
            if corners_on[i][0] == x or corners_on[i][2] == x:
                j += 1
            while j + 1 < len(corners_on):
                if ((corners_on[j][0] == x and corners_on[j + 1][0] == x)
                        or (corners_on[j][2] == x and corners_on[j + 1][2] == x)):
                    j += 2  # two removed or two added
                elif corners_on[j][0] == x or corners_on[j][2] == x:
                    j += 1  # Added or removed (implies j+1 removed or added)
                    break
                else:
                    break
        res += (corners_on[j][1] - corners_on[i][1]) + 1
        i = j + 1
    # Second, calculate the blocks on x + 1 till x_next level, skip removed
    i = 0
    while i < len(corners_on):
        if corners_on[i][2] == x:  # till first is not removed
            i += 1
        else:
            j = i + 1
            while corners_on[j][2] == x:  # if more removed later
                j += 1
            if len(x_values) == 0:
                res += (corners_on[j][1] - corners_on[i][1] + 1) * \
                       np.int64(x_next - x)
            else:
                res += (corners_on[j][1] - corners_on[i][1] + 1) * \
                       np.int64(x_next - (x + 1))
            i = j + 1
    x = x_next
print(res)
