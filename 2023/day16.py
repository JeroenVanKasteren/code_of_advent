import re

with open('day16', 'r') as f:
    file = f.read()

map = [line for line in file.split('\n')]

start_pos = []
for x in range(len(map)):
    start_pos.append((x, -1, 'Right'))
    start_pos.append((x, len(map[0]), 'Left'))
for y in range(len(map[0])):
    start_pos.append((-1, y, 'Down'))
    start_pos.append((len(map), y, 'Up'))

energized_max = 0
for pos in start_pos:
    beams = [pos]
# beams = [(0, -1, 'Right')]
    energized = set()
    beams_set = set()

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            x, y, direction = beam[0], beam[1], beam[2]
            if direction == 'Right':
                way = map[x][y + 1:]
                search = re.search('[^.-]', way)
                end = len(way) - 1 if search is None else search.span()[0]
                for i in range(0, end + 1):
                    energized.add((x, y + 1 + i))
                if search is not None:
                    y_end = search.span()[0] + y + 1
                    match = search.group()
                    if match == '/':
                        new_beams.append((x, y_end, 'Up'))
                    elif match == '\\':
                        new_beams.append((x, y_end, 'Down'))
                    elif match == '|':
                        new_beams.append((x, y_end, 'Up'))
                        new_beams.append((x, y_end, 'Down'))
            elif direction == 'Down':
                way = ''.join([line[y] for line in map[x + 1:]])
                search = re.search('[^.|]', way)
                end = len(way) - 1 if search is None else search.span()[0]
                for i in range(0, end + 1):
                    energized.add((x + 1 + i, y))
                if search is not None:
                    x_end = search.span()[0] + x + 1
                    match = search.group()
                    if match == '/':
                        new_beams.append((x_end, y, 'Left'))
                    elif match == '\\':
                        new_beams.append((x_end, y, 'Right'))
                    elif match == '-':
                        new_beams.append((x_end, y, 'Left'))
                        new_beams.append((x_end, y, 'Right'))
            elif direction == 'Left':
                way = map[x][:y]
                search = re.search('[^.-]', way[::-1])
                if search is not None:
                    y_end = len(way) - 1 - search.span()[0]
                else:
                    y_end = 0
                for y_new in range(y - 1, y_end - 1, -1):
                    energized.add((x, y_new))
                if search is not None:
                    match = search.group()
                    if match == '/':
                        new_beams.append((x, y_end, 'Down'))
                    elif match == '\\':
                        new_beams.append((x, y_end, 'Up'))
                    elif match == '|':
                        new_beams.append((x, y_end, 'Up'))
                        new_beams.append((x, y_end, 'Down'))
            elif direction == 'Up':
                way = ''.join([line[y] for line in map[:x]])
                search = re.search('[^.|]', way[::-1])
                x_end = 0 if search is None else len(way) - 1 - search.span()[0]
                for x_new in range(x - 1, x_end - 1, -1):
                    energized.add((x_new, y))
                if search is not None:
                    match = search.group()
                    if match == '/':
                        new_beams.append((x_end, y, 'Right'))
                    elif match == '\\':
                        new_beams.append((x_end, y, 'Left'))
                    elif match == '-':
                        new_beams.append((x_end, y, 'Left'))
                        new_beams.append((x_end, y, 'Right'))
        beams = []
        for beam in new_beams:
            if beam not in beams_set:
                beams.append(beam)
                beams_set.add(beam)

        # print(beams)
        # new_map = [''.join(['.' for _ in range(len(map[0]))]) for _ in range(len(map))]
        # for x, y in energized:
        #     s = list(new_map[x])
        #     s[y] = '#'
        #     new_map[x] = ''.join(s)
        # for x, y, direction in beams:
        #     s = list(new_map[x])
        #     if direction == 'Right':
        #         s[y] = '>'
        #     elif direction == 'Down':
        #         s[y] = 'v'
        #     elif direction == 'Left':
        #         s[y] = '<'
        #     elif direction == 'Up':
        #         s[y] = '^'
        #     new_map[x] = ''.join(s)
        # for line in new_map:
        #     print(line)
        # print('\n')
    if len(energized) > energized_max:
        energized_max = len(energized)
print(energized_max)
