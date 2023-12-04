import numpy as np

with open('day10', 'r') as f:
    file = f.read()

commands = [row for row in file.split('\n')]

count = 0
X = 1
signal = 0
for instruction in commands:
    count += 1
    if instruction == 'noop':
        if (count - 20) % 40 == 0:
            signal += count * X
    else:
        _, v = instruction.split(' ')
        if (count - 20) % 40 == 0:
            signal += count*X
        count += 1
        if (count - 20) % 40 == 0:
            signal += count * X
        X += int(v)
print(signal)
# [[i, (i - 20) % 40 == 0] for i in range(250) if (i - 20) % 40 == 0]

def draw_lit(output, count):
    print(count, int(count / 40))
    s = output[0, int(count / 40)]
    return s[:count % 40] + '#' + s[(count % 40) + 1:]

output = np.array([['.'*40]*6])
sprite = np.array([-1, 0, 1])
count = 0
X = 1

for instruction in commands:
    if instruction == 'noop':
        if count % 40 in X + sprite:
            output[0, int(count/40)] = draw_lit(output, count)
    else:
        _, v = instruction.split(' ')
        if count % 40 in X + sprite:
            output[0, int(count/40)] = draw_lit(output, count)
        count += 1
        if count % 40 in X + sprite:
            output[0, int(count/40)] = draw_lit(output, count)
        X += int(v)
    count += 1
print(output)
