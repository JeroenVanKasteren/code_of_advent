with open('day21', 'r') as f:
    map = f.read().split('\n')

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
current = set()  # (r, c)
unvisited = set()

for r, row in enumerate(map):
    for c, char in enumerate(row):
        if char == '.':
            unvisited.add((r, c))
        elif char == 'S':
            current.add((r, c))


# def pos_visits(steps, goal):
#     if steps % 2 == goal % 2:
#         times = goal // 2
#     else:
#         times = goal // 2 - 1
#     return times - steps // 2 + 1


def visits_at_end(steps, goal):
    return 1 if steps % 2 == goal % 2 else 0


goal = 64
steps = 0
res = visits_at_end(steps, goal)
while steps < goal and len(current) > 0:
    steps += 1
    next_places = set()
    for node in current:
        for d in dirs.values():
            r, c = node[0] + d[0], node[1] + d[1]
            if (r, c) in unvisited:
                next_places.add((r, c))
                unvisited.remove((r, c))
    res += len(next_places) * visits_at_end(steps, goal)
    current = next_places
print(res)


# Part 2
current = set()
visited = set()

for r, row in enumerate(map):
    for c, char in enumerate(row):
        if char == 'S':
            current.add((r, c))
            visited.add((r, c))


def valid_position(r, c):
    return map[r % len(map)][c % len(map[0])] != '#'


goal = 5000
steps = 0
res = visits_at_end(steps, goal)
while steps < goal and len(current) > 0:
    steps += 1
    next_places = set()
    for node in current:
        for d in dirs.values():
            r, c = node[0] + d[0], node[1] + d[1]
            if valid_position(r, c) and (r, c) not in visited:
                next_places.add((r, c))
                visited.add((r, c))
    res += len(next_places) * visits_at_end(steps, goal)
    current = next_places
print(res)
