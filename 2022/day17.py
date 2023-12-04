import numpy as np

with open('day17', 'r') as f:
    file = f.read()

jet_pattern = [char for char in file]

top = np.array([0] * 7)

rocks = [[[2, 0], [3, 0], [4, 0], [5, 0]],
         [[3, 0], [2, 1], [3, 1], [4, 1], [3, 2]],
         [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]],
         [[2, 0], [2, 1], [2, 2], [2, 3]],
         [[2, 0], [3, 0], [2, 1], [3, 1]]]

mountain = set((x, 0) for x in range(7))

rocks_len = len(rocks)
jets_len = len(jet_pattern)
rock_i = 0
jet_i = 0
total_i = 0

while total_i < 2022:
    rock = rocks[rock_i]
    start_y = max(top) + 4
    rock_f = np.array(rock).copy()
    rock_f[:, 1] += start_y
    while True:
        if jet_pattern[jet_i] == '<':
            rock_f[:, 0] -= 1
            if np.any(rock_f[:, 0] == -1):
                rock_f[:, 0] += 1
            elif np.any([(x, y) in mountain for x, y in rock_f]):
                rock_f[:, 0] += 1
        else:  # '>'
            rock_f[:, 0] += 1
            if np.any(rock_f[:, 0] == 7):
                rock_f[:, 0] -= 1
            elif np.any([(x, y) in mountain for x, y in rock_f]):
                rock_f[:, 0] -= 1
        rock_f[:, 1] -= 1
        if np.any([(x, y) in mountain for x, y in rock_f]):
            rock_f[:, 1] += 1
            mountain.update([(x, y) for x, y in rock_f])
            xs = set(rock_f[:, 0])
            for x in xs:
                top[x] = max(top[x], max(rock_f[rock_f[:, 0] == x][:, 1]))
            rock_i = (rock_i + 1) % rocks_len
            jet_i = (jet_i + 1) % jets_len
            total_i += 1
            break
        jet_i = (jet_i + 1) % jets_len

print(max(top))
print(top)
print(mountain)

lcm = np.lcm(jets_len, rocks_len)
while total_i < lcm:
    rock = rocks[rock_i]
    start_y = max(top) + 4
    rock_f = np.array(rock).copy()
    rock_f[:, 1] += start_y
    while True:
        if jet_pattern[jet_i] == '<':
            rock_f[:, 0] -= 1
            if np.any(rock_f[:, 0] == -1):
                rock_f[:, 0] += 1
            elif np.any([(x, y) in mountain for x, y in rock_f]):
                rock_f[:, 0] += 1
        else:  # '>'
            rock_f[:, 0] += 1
            if np.any(rock_f[:, 0] == 7):
                rock_f[:, 0] -= 1
            elif np.any([(x, y) in mountain for x, y in rock_f]):
                rock_f[:, 0] -= 1
        rock_f[:, 1] -= 1
        if np.any([(x, y) in mountain for x, y in rock_f]):
            rock_f[:, 1] += 1
            mountain.update([(x, y) for x, y in rock_f])
            xs = set(rock_f[:, 0])
            for x in xs:
                top[x] = max(top[x], max(rock_f[rock_f[:, 0] == x][:, 1]))
            rock_i = (rock_i + 1) % rocks_len
            jet_i = (jet_i + 1) % jets_len
            total_i += 1
            break
        jet_i = (jet_i + 1) % jets_len

print(max(top) * (1000000000000 / lcm))
print(top)
print(mountain)

