import numpy as np

with open('day13', 'r') as f:
    file = f.read()

pairs = [row for row in file.split('\n')]


def traverse(input1, input2):
    if isinstance(input1, int) and isinstance(input2, int):
        return input1 <= input2
    if isinstance(input1, int):
        input1 = [input1]
    elif isinstance(input2, int):
        input2 = [input2]
    if len(input1) == 0 > len(input2) == 0:
        return True
    elif len(input1) == 0 < len(input2) == 0:
        return False
    for i in range(max(len(input1), len(input2))):
        if i == len(input1):
            return True
        elif i == len(input2):
            return False
        order_right = traverse(input1[i], input2[i])
        if not order_right:
            return False
    return True


# i = 0
# while i < len(pairs):
#     print(pairs[i])
#     print(pairs[i + 1])
#     print(traverse(eval(pairs[i]), eval(pairs[i + 1])))
#     i += 3

# [1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
# [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]

input1 = [[1], [2, 3, 4]]
input2 = [[1], 4]
print(traverse(input1, input2))
