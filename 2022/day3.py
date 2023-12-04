import numpy as np
with open('day3', 'r') as f:
    s = f.read()
rucksack = np.array([[x, x[:int(len(x)/2)], x[-int(len(x)/2):], len(x)] for x in s.split("\n")])

items = [set(x[:int(len(x)/2)]).intersection(set(x[-int(len(x)/2):])).pop() for x in s.split("\n")]
print(sum([ord(item) + (-ord('a') + 1) * item.islower() + (-ord('A') + 27) * item.isupper() for item in items]))

groups = np.array([x for x in s.split("\n")]).reshape(-1, 3)
items = [set(group[0]).intersection(group[1]).intersection(group[2]).pop() for group in groups]
print(sum([ord(item) + (-ord('a') + 1) * item.islower() + (-ord('A') + 27) * item.isupper() for item in items]))

rucksack = np.array([[x, x[:int(len(x)/2)], x[-int(len(x)/2):], len(x)] for x in s.split("\n")])


