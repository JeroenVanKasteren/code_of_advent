import re

with open('day23', 'r') as f:
    maze = f.read().split('\n')

start_node = 0, re.search('\.', maze[0]).span()[0]
end_node = 0, 0
dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
u_turn = {'R': 'L', 'D': 'U', 'L': 'R', 'U': 'D'}
slopes = {'R': '>', 'D': 'v', 'L': '<', 'U': '^'}
nodes = {start_node: set()}
ordered_nodes = []
permanent = set()
temporary = set()


def valid_step(r, c, d, d_last):
    if u_turn[d] == d_last:
        return False
    r_n, c_n = r + dirs[d][0], c + dirs[d][1]
    if maze[r_n][c_n] == '.' or maze[r_n][c_n] == slopes[d]:
        return True
    return False


def next_node(r, c, d):
    global end_node
    if ((r == 0 and d == 'U') or (r == len(maze) - 1) or
            not valid_step(r, c, d, None)):
        return None, None
    r, c = r + dirs[d][0], c + dirs[d][1]
    steps = 1
    if maze[r][c] == slopes[d]:
        r, c = r + dirs[d][0], c + dirs[d][1]
        steps += 1
    d_last = d
    dead_end = False
    while r < len(maze) and not dead_end:
        for d in dirs:
            dead_end = True
            if valid_step(r, c, d, d_last):
                dead_end = False
                r, c = r + dirs[d][0], c + dirs[d][1]
                d_last = d
                steps += 1
                if r == len(maze) - 1:
                    end_node = r, c
                    return tuple([r, c]), steps
                if maze[r][c] == slopes[d]:
                    r, c = r + dirs[d][0], c + dirs[d][1]
                    return tuple([r, c]), steps + 1
                break
    return None, None


def add_node(origin, new_node, steps):
    global nodes
    if new_node not in nodes:
        nodes[new_node] = set()
    nodes[origin].add((new_node, steps))


def visit(node):
    if node in permanent:
        return
    assert node not in temporary, f'node {node} in temporary'
    temporary.add(node)
    for d in dirs:
        new_node, steps = next_node(node[0], node[1], d)
        if new_node is not None:
            add_node(node, new_node, steps)
            visit(new_node)
    temporary.remove(node)
    permanent.add(node)
    ordered_nodes.insert(0, node)


visit(start_node)

longest_path = {k: 0 for k in nodes.keys()}
for origin in ordered_nodes:
    for destination, distance in nodes[origin]:
        longest_path[destination] = max(distance + longest_path[origin],
                                        longest_path[destination])
print(longest_path[end_node])

# x, y = 13, 13
# radius = 3
# x, y = new_node[0], new_node[1]
# for i in range(x-radius, x+radius+1):
#     print(maze[i][y-radius:y+radius+1])

# add directions uphill
for keys in nodes:
    for node, steps in nodes[keys]:
        nodes[node].add((keys, steps))

count = 0
for keys in nodes:
    if len(nodes[keys]) <= 2:
        count += 1
print(count)

class Node:
    def __init__(self, node, steps_to_node, path_to_node):
        self.node = node
        self.steps_to_node = steps_to_node
        self.path_to_node = path_to_node

    def get_path(self, new_node=None):
        new_path = self.path_to_node.copy()
        if new_node is not None:
            new_path.add(new_node)
        return new_path

    def print(self):
        print(f'Node: {self.node}, steps: {self.steps_to_node}, path: '
              f'{self.path_to_node}')


# DFS
nodes_to_visit = [Node(start_node, 0, set())]  # stack
longest_path = set()
most_steps = 0
while len(nodes_to_visit) > 0:
    current = nodes_to_visit.pop()
    for neighbour, new_steps in nodes[current.node]:
        if neighbour == end_node:
            most_steps = max(most_steps, current.steps_to_node + new_steps)
            longest_path = current.get_path(neighbour)
            break
        elif neighbour not in current.path_to_node:
            nodes_to_visit.append(Node(neighbour,
                                       current.steps_to_node + new_steps,
                                       current.get_path(neighbour)))
print(longest_path)
print(most_steps)

# def dfs(node, path_steps, path, most_steps):
#     if node == end_node:
#         return path, max(path_steps, most_steps)
#     path.add(node)
#     for neighbour, steps in nodes[node]:
#         if neighbour not in path:
#             path, most_steps = dfs(neighbour, path_steps + steps, path,
#                                    most_steps)
#     return path, most_steps
#
# print(dfs(start_node, 0, set(), 0))
