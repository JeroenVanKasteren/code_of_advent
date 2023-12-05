import numpy as np
import re
import copy

with open('day5', 'r') as f:
    s = f.read()

data = s.split('\n\n')
category = np.array(re.findall(r'\d+', data.pop(0))).astype(np.int64)

for kind in data:
    category_map = kind.split('\n')
    change = np.zeros(len(category), dtype=np.int64)
    for i in range(1, len(category_map)):
        destination, source, range_length = \
            np.array(category_map[i].split(' ')).astype(np.int64)
        change = np.where((category >= source) &
                          (category < source + range_length),
                          destination - source,
                          change)
    category += change

print(np.min(category))


data = s.split('\n\n')
category = np.array(re.findall(r'\d+', data.pop(0))).astype(np.int64)
category_ranges = [[category[i], category[i] + category[i+1] - 1]
                   for i in range(0, len(category), 2)]
print(category_ranges)
for kind in data:
    category_map = kind.split('\n')
    # print(category_map[0])
    changed_ranges = []
    for i in range(1, len(category_map)):
        destination, source, range_length = \
            np.array(category_map[i].split(' ')).astype(np.int64)
        change = destination - source
        source_end = source + range_length - 1
        new_ranges = []
        for category_range in category_ranges:
            range_s = category_range[0]
            range_e = category_range[1]
            if (source <= range_s) & (range_s <= source_end < range_e):
                changed_ranges.append([range_s + change, range_e + change])
                new_ranges.append([source_end + 1, range_e])
                # print('overlap begin')
                # print(source, source_end, change)
                # print(category_range)
                # print([[range_s + change, source_end + change],
                #        [source_end + 1, range_e]])
            elif (range_s < source <= range_e) & (range_e <= source_end):
                new_ranges.append([range_s, source - 1])
                changed_ranges.append([source + change, range_e + change])
                # print('overlap end')
                # print(source, source_end, change)
                # print(category_range)
                # print([[range_s, source - 1],
                #                    [source + change, range_e + change]])
            elif (range_s < source) & (source_end < range_e):
                new_ranges.extend([[range_s, source - 1],
                                   [source_end + 1, range_e]])
                changed_ranges.append([source + change, source_end + change])
                # print('overlap all')
                # print(source, source_end, change)
                # print(category_range)
                # print([[range_s, source - 1],
                #                    [source + change, source_end + change],
                #                    [source_end + 1, range_e]])
            elif (source <= range_s) & (range_e <= source_end):
                changed_ranges.append([range_s + change, range_e + change])
                # print('between')
                # print(source, source_end, change)
                # print(category_range)
                # print([range_s + change, range_e + change])
            else:
                new_ranges.append(category_range)
        category_ranges = new_ranges
    category_ranges.extend(changed_ranges)
    # print(category_ranges)
print(np.min(category_ranges))
# 7111590 -> too low
