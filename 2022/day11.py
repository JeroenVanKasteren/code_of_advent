import numpy as np
import copy

with open('day11', 'r') as f:
    file = f.read()

# file="""test_input"""

lines = [row for row in file.split('\n')]
monkeys = []
items = []
test = []

i = 0
while i < len(lines):
    if lines[i][:6] == 'Monkey':
        i += 1
        line = lines[i].replace(',', '')
        items.append([int(item) for item in line.split(' ')[4:]])
        i += 1
        if '+' in lines[i]:
            monkeys.append(['+', lines[i].split(' ')[-1]])
        else:
            monkeys.append(['*', lines[i].split(' ')[-1]])
        i += 1
        test.append([int(lines[i].split(' ')[-1]), int(lines[i+1].split(' ')[-1]), int(lines[i+2].split(' ')[-1])])
        i += 2
    i += 1

activity = [0]*len(monkeys)
items_original = copy.deepcopy(items)

rounds = 20
for _ in range(rounds):
    for monkey in range(len(monkeys)):
        tmp_items = items[monkey].copy()
        for item in tmp_items:
            activity[monkey] += 1
            if monkeys[monkey][0] == '+':
                if monkeys[monkey][1] == 'old':
                    new = int(item) + int(item)
                else:
                    new = int(item) + int(monkeys[monkey][1])
            else:
                if monkeys[monkey][1] == 'old':
                    new = int(item) * int(item)
                else:
                    new = int(item) * int(monkeys[monkey][1])
            new = int(new/3)
            if new % test[monkey][0] == 0:
                items[test[monkey][1]].append(new)
            else:
                items[test[monkey][2]].append(new)
            items[monkey].pop(0)

print(sorted(activity)[-2]*sorted(activity)[-1])

activity = [0]*len(monkeys)
items = items_original.copy()
print(items)

divisors = [x[0] for x in test]
np.lcm.reduce(divisors)  # all prime, therefore its the multiple of all
lcm = np.prod(divisors)

rounds = 10000
for _ in range(rounds):
    for monkey in range(len(monkeys)):
        tmp_items = items[monkey].copy()
        for item in tmp_items:
            activity[monkey] += 1
            if monkeys[monkey][0] == '+':
                if monkeys[monkey][1] == 'old':
                    new = int(item) + int(item)
                else:
                    new = int(item) + int(monkeys[monkey][1])
            else:
                if monkeys[monkey][1] == 'old':
                    new = int(item) * int(item)
                else:
                    new = int(item) * int(monkeys[monkey][1])
            # new = new % lcm
            if new % test[monkey][0] == 0:
                items[test[monkey][1]].append(new)
            else:
                items[test[monkey][2]].append(new)
            items[monkey].pop(0)

print(sorted(activity)[-2]*sorted(activity)[-1])
