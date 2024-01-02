import numpy as np

with open('day14', 'r') as f:
    file = f.read()

data = [row for row in file.split('\n')]
data = [''.join(column) for column in list(zip(*data))]

res = 0
max_load = len(data[0])
for c in range(len(data)):
    current = 0
    while current < len(data[c]):
        rocks = 0
        for i in range(current, len(data[c])):
            if data[c][i] == 'O':
                res += max_load - current - rocks
                rocks += 1
            if data[c][i] == '#' or i == len(data[c]) - 1:
                current = i + 1
                break
print(res)


# Part 14.2
def tilt(line):
    beams = np.where(line == terrain['#'])[0]
    beams = np.append(beams, len(line))
    start = 0
    for beam_i in beams:
        rocks = int(sum(line[start:beam_i]))
        line[start:start+rocks] = terrain['O']
        line[start+rocks:beam_i] = terrain['.']
        start = beam_i + 1
    return line


def load_calculator(platform):
    res = 0
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            if platform[r][c] == terrain['O']:
                res += len(platform) - r
    return res


def tilt_simulator(platform):
    for c, line in enumerate(platform.T):  # north, columns
        platform[:, c] = tilt(line)
    for r, line in enumerate(platform):  # west, rows
        platform[r, :] = tilt(line)
    for c, line in enumerate(platform.T):  # south, columns reversed
        platform[:, c] = tilt(line[::-1])[::-1]
    for r, line in enumerate(platform):  # east, rows
        platform[r, :] = tilt(line[::-1])[::-1]
    return platform


data = [row for row in file.split('\n')]
platform = np.zeros((len(data), len(data[0])))
terrain = {'.': 0, '#': -1, 'O': 1}  # space, beam, rock
terrain_inv = {0: ',', -1: '#', 1: 'O'}
for r in range(len(data)):
    for c in range(len(data[0])):
        platform[r, c] = terrain[data[r][c]]
memory = {}
i = 1
while i < 1e3:
    platform = tilt_simulator(platform)
    platform_hash = hash(platform.tobytes())
    if platform_hash in memory:
        cycle = i - memory[platform_hash]
        print(cycle, memory[platform_hash], i, load_calculator(platform))
        break
    memory[platform_hash] = i
    i += 1

remainder = (1000000000 - memory[platform_hash]) % cycle
for i in range(remainder):
    platform = tilt_simulator(platform)
print(load_calculator(platform))

# for r in range(len(data)):
#     s = ''
#     for c in range(len(data[0])):
#         s += terrain_inv[platform[r][c]]
#     print(s)
# print('\n')
