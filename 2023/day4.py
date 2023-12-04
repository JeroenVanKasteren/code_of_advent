import numpy as np
import re
with open('day4', 'r') as f:
    s = f.read()

sections = [[re.findall(r'\d+', row.split('|')[0].strip().split(':')[1]),
             re.findall(r'\d+', row.split('|')[1].strip())]
            for row in s.split("\n")]

res = 0
for section1, section2 in sections:
    n = len(set(section1).intersection(set(section2)))
    if n > 0:
        res += 2**(n-1)

print(res)
# 24160


def get_copies(subsections):
    copies = 1
    winning, yours = subsections[0]
    n = len(set(winning).intersection(set(yours)))
    for i in range(n):
        copies += get_copies(subsections[i+1:])
    return copies


res = 0
for i, section in enumerate(sections):
    res += get_copies(sections[i:])

print(res)
# 24160
