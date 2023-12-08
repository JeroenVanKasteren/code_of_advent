import re
import math

with open('day8', 'r') as f:
    file = f.read()

instructions, places = file.split('\n\n')
place = places.split('\n')[0]
locations = {}
current = []
notes = []
for place in places.split('\n'):
    key = place.split('=')[0].strip()
    locations[key] = [re.sub("[^a-zA-Z1-9]+", '', str) for str in
                      place.split('=')[1].split(',')]
    if key[2] == 'A':
        current.append(key)
        notes.append([key, 0, 0])  # Key, first Z, second Z

for j, current_j in enumerate(current):
    res = 0
    found_z = 0
    i = 0
    while res < 1e6:
        new = ''
        # print(current_j, res)
        destination = ''.join(current_j)[2::3]
        if destination.count('Z') == len(destination):
            if found_z == 0:
                notes[j][1] = res
                found_z = 1
            else:
                notes[j][2] = res
                break
        if instructions[i] == 'L':
            new_location = locations[current_j][0]
        else:
            new_location = locations[current_j][1]
        res += 1
        i = (i + 1) % len(instructions)
        current_j = new_location

diff = [notes[2] - notes[1] for notes in notes]
print(notes)

print(math.lcm(*diff))
