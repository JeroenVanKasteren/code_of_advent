import numpy as np
import re

with open('day8', 'r') as f:
    file = f.read()

instructions, places = file.split('\n\n')
place = places.split('\n')[0]
locations = {}
current = []
for place in places.split('\n'):
    key = place.split('=')[0].strip()
    locations[key] = [re.sub("[^a-zA-Z]+", '', str) for str in
                      place.split('=')[1].split(',')]
    if key[2] == 'A':
        current.append(key)

res = 0
i = 0
while res < 100000:
    # if all currents end with Z, break
    if ''.join(current)[0::1] == 'ZZZ':
        break
    for x in current:
    if instructions[i] == 'L':
        current = locations[current][0]
    else:
        current = locations[current][1]
    res += 1
    i = (i + 1) % len(instructions)
print(res)
