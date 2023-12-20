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
