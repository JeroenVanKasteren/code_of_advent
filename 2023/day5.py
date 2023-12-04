import numpy as np
with open('day5', 'r') as f:
    s = f.read()

platform, moves = s.split('\n\n')
platform = platform.split('\n')
moves = moves.split('\n')

locations = [[[int(i/4)+1, char] for i, char in enumerate(line) if char.isalpha()] for line in platform]

stacks = [''.join([element[1] for r in locations for element in r if element[0] == i]) for i in range(1, 10)]
instructions = [move.split(' ') for move in moves]
for row in instructions:
    move = int(row[1])
    frm = int(row[3]) - 1
    to = int(row[5]) - 1
    for i in range(int(move)):
        stacks[to] = stacks[frm][0] + stacks[to]
        if len(stacks[frm]) > 1:
            stacks[frm] = stacks[frm][1:]
        else:
            stacks[frm] = ''
print(''.join([stack[0] for stack in stacks]))

stacks = [''.join([element[1] for r in locations for element in r if element[0] == i]) for i in range(1, 10)]
instructions = [move.split(' ') for move in moves]
for row in instructions:
    move = int(row[1])
    frm = int(row[3]) - 1
    to = int(row[5]) - 1
    stacks[to] = stacks[frm][:move] + stacks[to]
    if len(stacks[frm]) > 1:
        stacks[frm] = stacks[frm][move:]
    else:
        stacks[frm] = ''
print(''.join([stack[0] for stack in stacks]))