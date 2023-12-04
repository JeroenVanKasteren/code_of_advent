import numpy as np

with open('day18', 'r') as f:
    file = f.read()

coordinates = np.array([[int(coordinate) for coordinate in line.split(',')] for line in file.split('\n')])

res = 0
for coordinate in coordinates:
    res += 6 - np.sum((np.sum(coordinates - coordinate == 0, axis=1) == 2) &
                      (np.sum(abs(coordinates - coordinate) == 1, axis=1) == 1))
print(res)

lava = {(x, y, z) for x, y, z in coordinates}
air_touched = {}
for coordinate in coordinates:
    for direction in [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]:
        side = tuple(coordinate + direction)
        if side not in lava:
            if side in air_touched:
                air_touched[side] += 1
            else:
                air_touched[side] = 1

print(np.sum(np.array(list(air_touched.values())) == 6))
print(res - np.sum(np.array(list(air_touched.values())) == 6))
