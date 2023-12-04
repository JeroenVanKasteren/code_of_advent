import numpy as np

with open('day12', 'r') as f:
    file = f.read()

graph = {}
unvisited = {}
grid = np.array([list(row) for row in file.split('\n')])
heights = grid.copy()
start = (-1, -1)
end = (-1, -1)
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        graph[(r, c)] = set()
        unvisited[(r, c)] = len(grid) * len(grid[0]) + 1
        if item == 'S':
            start = (r, c)
            unvisited[(r, c)] = 0
            heights[r, c] = 'a'
        if item == 'E':
            end = (r, c)
            heights[r, c] = 'z'
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= r + x < len(grid) and 0 <= c + y < len(row):
                if ord(heights[r, c]) + 1 >= ord(heights[r + x, c + y]):
                    graph[(r, c)].add((r + x, c + y))
visited = {}

while len(unvisited) > 0:
    if end in visited:
        break
    visit = min(unvisited, key=unvisited.get)
    for neighbour in graph[visit]:
        if neighbour not in visited:
            unvisited[neighbour] = min(unvisited[neighbour], unvisited[visit] + 1)
    visited[visit] = unvisited[visit]
    del unvisited[visit]

print(visited[end]+2)  # Add first and last node
print('done')

graph = {}
unvisited = {}
grid = np.array([list(row) for row in file.split('\n')])
heights = grid.copy()
start = (-1, -1)
end = (-1, -1)
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        graph[(r, c)] = set()
        unvisited[(r, c)] = len(grid) * len(grid[0]) + 1
        if item == 'a':
            unvisited[(r, c)] = 0
        elif item == 'S':
            start = (r, c)
            unvisited[(r, c)] = 0
            heights[r, c] = 'a'
        elif item == 'E':
            end = (r, c)
            heights[r, c] = 'z'
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= r + x < len(grid) and 0 <= c + y < len(row):
                if ord(heights[r, c]) + 1 >= ord(heights[r + x, c + y]):
                    graph[(r, c)].add((r + x, c + y))

visited = {}

while len(unvisited) > 0:
    if end in visited:
        break
    visit = min(unvisited, key=unvisited.get)
    for neighbour in graph[visit]:
        if neighbour not in visited:
            unvisited[neighbour] = min(unvisited[neighbour], unvisited[visit] + 1)
    visited[visit] = unvisited[visit]
    del unvisited[visit]

print(visited[end]+2)  # Add first and last node
print('done')
# 386

# for r, row in enumerate(grid):
#     for c, item in enumerate(row):
#         if heights[r, c] == 'a':
#             min_dist = min(min_dist, visited[(r, c)])


