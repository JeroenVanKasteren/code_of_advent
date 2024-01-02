import re
import random
import copy

with open('day25', 'r') as f:
    file = f.read()

graph = {}
edges = {}
for line in file.split('\n'):
    items = re.split(' |: ', line)
    for i, item in enumerate(items):
        if item not in graph:
            graph[item] = set()
        if i > 0:
            graph[items[0]].add(item)
            graph[item].add(items[0])
            edges[items[0] + item] = 1
            edges[item + items[0]] = 1


def min_cut_phase():
    global sub_graph, sub_edges
    start = next(iter(sub_graph))
    found_set = [start]
    candidates = set(sub_graph[start])
    max_weight = 0
    t = None

    while len(candidates) > 0:
        max_weight = 0
        for candidate in candidates:
            weight_sum = 0
            for vertex in found_set:
                if vertex + candidate in sub_edges:
                    weight_sum += sub_edges[vertex + candidate]
            if weight_sum > max_weight:
                t = candidate
                max_weight = weight_sum
        found_set.append(t)
        candidates = candidates.union(sub_graph[t]).difference(found_set)
    return max_weight, found_set[-2], found_set[-1]


def merge_vertices(s, t):
    global sub_graph, sub_edges, vertex_size
    sub_graph[s + t] = sub_graph[s].union(sub_graph[t]).difference([s, t])
    for vertex in sub_graph[s + t]:
        if s in sub_graph[vertex] and t in sub_graph[vertex]:
            sub_graph[vertex].remove(s), sub_graph[vertex].remove(t)
            new_weight = sub_edges[s + vertex] + sub_edges[t + vertex]
            sub_edges.pop(s + vertex), sub_edges.pop(vertex + s)
            sub_edges.pop(t + vertex), sub_edges.pop(vertex + t)
        elif s in sub_graph[vertex]:
            sub_graph[vertex].remove(s)
            new_weight = sub_edges[s + vertex]
            sub_edges.pop(s + vertex), sub_edges.pop(vertex + s)
        else:  # t in sub_graph[vertex]:
            sub_graph[vertex].remove(t)
            new_weight = sub_edges[t + vertex]
            sub_edges.pop(t + vertex), sub_edges.pop(vertex + t)
        sub_graph[vertex].add(s + t)
        sub_edges[s + t + vertex] = new_weight
        sub_edges[vertex + s + t] = new_weight
    sub_graph.pop(s), sub_graph.pop(t)
    vertex_size[s + t] = vertex_size[s] + vertex_size[t]
    return sub_graph, sub_edges, vertex_size


def merge_too_heavy(u):
    global sub_graph, sub_edges, vertex_size, min_cut_guess
    changed = True
    while changed:
        changed = False
        for v in sub_graph[u]:
            if sub_edges[u + v] > min_cut_guess:
                merge_vertices(u, v)
                u += v
                changed = True
                break
    return sub_graph, sub_edges, vertex_size


def cal_min_cut():
    global sub_graph, sub_edges, vertex_size
    min_cut = len(sub_graph)
    size = 0

    while len(sub_graph) > 1:
        new_min_cut, s, t = min_cut_phase()
        if new_min_cut < min_cut:
            min_cut = new_min_cut
            size = vertex_size[t]
        if new_min_cut == min_cut_guess:
            break
        merge_vertices(s, t)
        merge_too_heavy(s + t)
    return min_cut, size


max_tries = 20
tries = 0
n = int(len(graph)*0.1)
min_cut_guess = 3
min_cut = min_cut_guess + 1
random.seed(1)
while tries < max_tries and min_cut != min_cut_guess:
    tries += 1
    sub_graph = copy.deepcopy(graph)
    sub_edges = copy.deepcopy(edges)
    vertex_size = {k: 1 for k in sub_graph.keys()}
    while len(sub_graph) > n:
        s_r = random.choice(sorted(sub_graph.keys()))
        t_r = random.choice(sorted(sub_graph[s_r]))
        merge_vertices(s_r, t_r)
        merge_too_heavy(s_r + t_r)
    min_cut, size = cal_min_cut()
    print(tries, min_cut, len(sub_graph))
    if min_cut == 3:
        break

print(size * (len(graph) - size))
