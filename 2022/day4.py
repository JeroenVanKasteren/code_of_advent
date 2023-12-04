import numpy as np
with open('day4', 'r') as f:
    s = f.read()

sections = np.array([[section.split('-') for section in row.split(',')] for row in s.split("\n")]).reshape(-1, 4).astype(int)
print(sum((sections[:, 0] - sections[:, 2])*(sections[:, 1] - sections[:, 3]) <= 0))
print(sum((sections[:, 0] - sections[:, 3])*(sections[:, 1] - sections[:, 2]) <= 0))

