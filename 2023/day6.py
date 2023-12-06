import numpy as np
import re
with open('day6', 'r') as f:
    s = f.read()

times, records = s.split('\n')
times = np.array(re.findall(r'\d+', times)).astype(int)
records = np.array(re.findall(r'\d+', records)).astype(int)

res = 1
for i in range(len(records)):
    ways = 0
    for wait in range(times[i]):
        ways += 1 if ((times[i] - wait) * wait) > records[i] else 0
    res *= ways
print(res)


def equationroots(a, b, c):
    dis = b**2 - 4 * a * c  # discriminant
    sqrt_dis = np.sqrt(abs(dis))
    if dis > 0:
        print("real and different roots")
        return [(-b + sqrt_dis) / (2 * a), (-b - sqrt_dis) / (2 * a)]
    elif dis == 0:
        print("real and same roots")
        return [-b / (2 * a), -b / (2 * a)]
    else:
        print("Complex Roots")
        # return [(- b / (2 * a), " + i", sqrt_dis),
        #         (- b / (2 * a), " - i", sqrt_dis)]


times, records = s.split('\n')
times = np.array(re.findall(r'\d+', times.replace(' ', ''))).astype(np.float64)
records = np.array(re.findall(r'\d+',
                              records.replace(' ', ''))).astype(np.float64)

roots = equationroots(1, -times[0], records[0])
print(int(np.floor(max(roots)) - np.ceil(min(roots))) + 1)
