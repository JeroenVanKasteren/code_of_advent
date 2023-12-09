import numpy as np

with open('day9', 'r') as f:
    file = f.read()

patterns = [np.array(pattern.split(' ')).astype(np.int64)
            for pattern in file.split('\n')]

res = 0
for pattern in patterns:
    sub_res = 0
    while sum(pattern == 0) < len(pattern):
        sub_res += pattern[-1]
        pattern = np.diff(pattern)
    res += sub_res
print(res)


res = 0
for pattern in patterns:
    # print(pattern)
    sub_res = pattern[0]
    sign = -1
    while sum(pattern == 0) < len(pattern):
        pattern = np.diff(pattern)
        sub_res += sign * pattern[0]
        sign *= -1
        # print(pattern)
    # print(sub_res)
    res += sub_res
print(res)
