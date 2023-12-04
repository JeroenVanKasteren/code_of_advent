import numpy as np

with open('day9', 'r') as f:
    file = f.read()

# file = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

# file = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

commands = np.array([row.split(' ') for row in file.split('\n')])

directions = {'U': np.array([0., 1.]),
              'R': np.array([1., 0.]),
              'D': np.array([0., -1.]),
              'L': np.array([-1., 0.])}

H = np.array([0., 0.])
T = np.array([0., 0.])
positions = {tuple(T)}  # dict{tuple(T):1}

for direction, moves in commands:
    for move in range(int(moves)):
        H += directions[direction]
        diff = np.array([H[0] - T[0], H[1] - T[1]])
        if abs(diff[0]) == 2 or abs(diff[1]) == 2:
            T = T + np.sign(diff)
        positions.add(tuple(T))
print(len(positions))

knots = np.array([0., 0.]*10).reshape(-1, 2)
positions = {tuple(knots[9])}  # dict{tuple(T):1}

for direction, moves in commands:
    for move in range(int(moves)):
        knots[0] += directions[direction]
        for i in range(1, 10):
            diff = np.array([knots[i-1, 0] - knots[i, 0], knots[i-1, 1] - knots[i, 1]])
            if abs(diff[0]) == 2 or abs(diff[1]) == 2:
                knots[i] = knots[i] + np.sign(diff)
            if i == 9:
                positions.add(tuple(knots[9]))
print(len(positions))
