import numpy as np

with open('day15', 'r') as f:
    file = f.read()

report = [line.split(':') for line in file.split('\n')]

sensors = np.empty((0, 2), int)
# sensors_set = set()
# sensors.add((sensor_x, sensor_y))
beacons = np.empty((0, 2), int)
beacons_set = set()
min_x = np.infty
max_x = -np.infty
for line in report:
    sensor_x, sensor_y = line[0].split(', ')
    sensor_x, sensor_y = sensor_x.split('=')[-1], sensor_y.split('=')[-1]
    sensors = np.append(sensors, np.array([[int(sensor_x), int(sensor_y)]]), axis=0)
    beacon_x, beacon_y = line[1].split(', ')
    beacon_x, beacon_y = beacon_x.split('=')[-1], beacon_y.split('=')[-1]
    beacons = np.append(beacons, np.array([[int(beacon_x), int(beacon_y)]]), axis=0)
    beacons_set.add((int(beacon_x), int(beacon_y)))
    min_x, max_x = min(min_x, int(sensor_x), int(beacon_x)), max(max_x, int(sensor_x), int(beacon_x))

# manhattan_distance
distances = np.sum(np.abs(sensors - beacons), axis=1)

# y = 2000000
y = 10
width = np.abs(sensors[:, 1] - y)
ranges_x = np.array([sensors[:, 0] - distances + width, sensors[:, 0] + distances - width]).T
ranges_x = ranges_x[width <= distances]
ranges_x = ranges_x[ranges_x[:, 0].argsort()]

def_ranges = np.array([ranges_x[0]])
for range_x in ranges_x[1:]:
    added = False
    for def_range in def_ranges:
        if np.sign(def_range[0] - range_x[1])*np.sign(def_range[1] - range_x[0]) <= 0:
            def_range[0] = min(range_x[0], def_range[0])
            def_range[1] = max(range_x[1], def_range[1])
            added = True
            break
    if not added:
        def_ranges = np.append(def_ranges, [range_x], axis=0)

subtract = len([(beacon_x, beacon_y) for beacon_x, beacon_y in beacons_set if beacon_y == y])
print(sum(def_ranges[:, 1] - def_ranges[:, 0]))

# for x in range(min_x, max_x + 1):
#     coordinate = np.array([x, y])
#     if np.any(np.sum(np.abs(coordinate - sensors), axis=1) <= distances):
#         count += 1
# print(count - subtract)

max_xy = 4000000
# max_xy = 20
breaking = False
# for y in range(max_xy+1):
for y in range(3100000, max_xy+1):
    width = np.abs(sensors[:, 1] - y)
    ranges_x = np.array([sensors[:, 0] - distances + width, sensors[:, 0] + distances - width]).T
    ranges_x = ranges_x[width <= distances]
    ranges_x = ranges_x[ranges_x[:, 0].argsort()]

    def_ranges = np.array([ranges_x[0]])
    for range_x in ranges_x[1:]:
        added = False
        for def_range in def_ranges:
            if np.sign(def_range[0] - range_x[1])*np.sign(def_range[1] - range_x[0]) <= 0:
                def_range[0] = min(range_x[0], def_range[0])
                def_range[1] = max(range_x[1], def_range[1])
                added = True
                break
        if not added:
            def_ranges = np.append(def_ranges, [range_x], axis=0)

    subtract = len([(beacon_x, beacon_y) for beacon_x, beacon_y in beacons_set if beacon_y == y])
    if def_ranges[0, 0] == 1:
        print('pos', 0, y)
        breaking = True
    elif def_ranges[-1, 1] == max_xy:
        print('pos', max_xy, y, max_xy*4000000+y)
        breaking = True
    elif len(def_ranges) > 1:
        for i in range(len(def_ranges)-1):
            if def_ranges[i + 1, 0] - def_ranges[i, 1] > 1:
                print(def_ranges)
                print(def_ranges[i, 1] + 1, y)
                print((def_ranges[i, 1] + 1)*4)
                breaking = True
    if breaking:
        break
# 11600820 * 1000000 + 3139120 = 11600823139120