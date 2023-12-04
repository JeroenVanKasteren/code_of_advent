with open('day14', 'r') as f:
    file = f.read()

coordinates = [[coordinate.split(',') for coordinate in line.split(' -> ')] for line in file.split('\n')]
coordinates = [[[int(a), int(b)] for a, b in line] for line in coordinates]

# +1 to also add last wall, this will also activate the other loop, however, that duplicate wall will not be added.
walls = set()
highest_y = 0
for block in coordinates:
    for i in range(len(block) - 1):
        for x in range(min(block[i][0], block[i + 1][0]), max(block[i][0], block[i + 1][0]) + 1):
            walls.add((x, block[i][1]))
        for y in range(min(block[i][1], block[i + 1][1]), max(block[i][1], block[i + 1][1]) + 1):
            walls.add((block[i][0], y))
        highest_y = max(highest_y, block[i][1], block[i + 1][1])

# sand falls down
abyss = False
all_sand = set()
while not abyss:
    sand_x, sand_y = 500, 0
    blocked = False
    while not blocked:
        if sand_y > highest_y:
            abyss = True
            break
        if (sand_x, sand_y + 1) in walls or (sand_x, sand_y + 1) in all_sand:
            if (sand_x - 1, sand_y + 1) in walls or (sand_x - 1, sand_y + 1) in all_sand:
                if (sand_x + 1, sand_y + 1) in walls or (sand_x + 1, sand_y + 1) in all_sand:
                    blocked = True
                    all_sand.add((sand_x, sand_y))
                else:
                    sand_x += 1
                    sand_y += 1
            else:
                sand_x -= 1
                sand_y += 1
        else:
            sand_y += 1
print(len(all_sand))

floor_y = highest_y + 2

all_sand = set()
stuck = False
while not stuck:
    sand_x, sand_y = 500, 0
    blocked = False
    while not blocked:
        if (500, 0) in all_sand:
            stuck = True
            break
        if sand_y + 1 == floor_y:
            blocked = True
            all_sand.add((sand_x, sand_y))
        if (sand_x, sand_y + 1) in walls or (sand_x, sand_y + 1) in all_sand:
            if (sand_x - 1, sand_y + 1) in walls or (sand_x - 1, sand_y + 1) in all_sand:
                if (sand_x + 1, sand_y + 1) in walls or (sand_x + 1, sand_y + 1) in all_sand:
                    blocked = True
                    all_sand.add((sand_x, sand_y))
                else:
                    sand_x += 1
                    sand_y += 1
            else:
                sand_x -= 1
                sand_y += 1
        else:
            sand_y += 1
print(len(all_sand))
