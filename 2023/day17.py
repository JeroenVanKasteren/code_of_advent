import numpy as np

with open('day17', 'r') as f:
    file = f.read()

map = np.array([list(row) for row in file.split('\n')], dtype=int)
# {'right':(0, 1),'down':(1, 0), 'left':(0, -1), 'up':(-1, 0)}
dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
turn = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

# state: (x, y, d)
v = np.array([[[np.inf for d in range(len(dirs))]
               for y in range(len(map[0]))] for x in range(len(map))])
dirs_set = set(dirs.keys())

# for d in range(len(dirs)):
v[-1, -1, :] = 0


def invalid(r, c):
    return r < 0 or r >= len(map) or c < 0 or c >= len(map[0])


N = 1e3
n = 0
min_steps = 4
max_steps = 10
while n < N:
    v_t = v.copy()
    for r in range(len(map)):
        for c in range(len(map[0])):
            if r == len(map) - 1 and c == len(map[0]) - 1:
                continue
            v_minis = np.ones(len(dirs)) * np.inf
            for d, step in dirs.items():
                heat = 0
                for i in range(1, min_steps):
                    r_i, c_i = r + step[0] * i, c + step[1] * i
                    if invalid(r_i, c_i):
                        break
                    heat += map[r_i, c_i]
                for i in range(min_steps, max_steps + 1):
                    r_i, c_i = r + step[0] * i, c + step[1] * i
                    if invalid(r_i, c_i):
                        break
                    heat += map[r_i, c_i]
                    v_minis[d] = min(v_minis[d], heat + v_t[r_i, c_i, d])
            for d_previous in dirs.keys():
                v[r, c, d_previous] = min(v_minis[turn[d_previous]])
    n += 1
    if min(v[0, 0]) < np.inf or n % 10 == 0:
        print(n, min(v[0, 0]))
    if (v_t == v).all():
        break
print(n, min(v[0, 0]))
# v_min = np.zeros((len(map), len(map[0])))
# for r in range(len(map)):
#     for c in range(len(map[0])):
#         v_min[r, c] = min(v[r, c, :])
# print(v_min)

arrows = ['>', '|', '<', '^']
policy = np.chararray((len(map), len(map[0])), 2, unicode=True)
policy[:] = '..'
r, c = 0, 0
d_previous = 1
while r < len(map) - 1 or c < len(map[0]) - 1:
    for d in turn[d_previous]:
        heat = v[r, c, d_previous]
        for i in range(1, min_steps):
            r_i, c_i = r + dirs[d][0] * i, c + dirs[d][1] * i
            if invalid(r_i, c_i):
                break
            heat -= map[r_i, c_i]
        for i in range(min_steps, max_steps + 1):
            r_i, c_i = r + dirs[d][0] * i, c + dirs[d][1] * i
            if invalid(r_i, c_i):
                break
            heat -= map[r_i, c_i]
            if heat == v[r_i, c_i, d]:
                break
        if (not invalid(r_i, c_i)) and heat == v[r_i, c_i, d]:
            break
    print(v[r_i, c_i, d])
    policy[r, c] = arrows[d] + str(i)
    r, c, d_previous = r_i, c_i, d
    print(arrows[d] + str(i), (r, c))
print(policy)
