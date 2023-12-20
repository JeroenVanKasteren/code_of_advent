with open('day13', 'r') as f:
    file = f.read()

islands = [island.split('\n') for island in file.split('\n\n')]


res = 0
m = 100
for island in islands:
    reflection = False
    for r in range(len(island) - 1):
        reflection = True
        for i in range(min(r + 1, len(island) - (r + 1))):
            if island[r - i] != island[r + i + 1]:
                reflection = False
                break
        if reflection is True:
            res += (r + 1) * m
            break

    island_t = [''.join(strip_of_land) for strip_of_land in list(zip(*island))]
    for c in range(len(island_t) - 1):
        reflection = True
        for i in range(min(c + 1, len(island_t) - (c + 1))):
            if island_t[c - i] != island_t[c + i + 1]:
                reflection = False
                break
        if reflection is True:
            res += c + 1
            break

print(res)

# island = islands[0]
# for strip_of_land in island:
#     print(strip_of_land)
# print('\n')
# island_t = [''.join(strip_of_land) for strip_of_land in list(zip(*island))]
# for strip_of_land in island_t:
#     print(strip_of_land)

# Part 2


def mirror(island):
    for r in range(len(island) - 1):
        smudges = 0
        for i in range(min(r + 1, len(island) - (r + 1))):
            if island[r - i] != island[r + i + 1]:
                for j in range(len(island[r - i])):
                    if island[r - i][j] != island[r + i + 1][j]:
                        smudges += 1
                if smudges > 1:
                    break
        if smudges == 1:
            return r + 1
    return 0


res = 0
m = 100
for island in islands:
    res += mirror(island) * m
    island_t = [''.join(strip_of_land) for strip_of_land in list(zip(*island))]
    res += mirror(island_t)
print(res)
