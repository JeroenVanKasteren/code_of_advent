import numpy as np

with open('day20', 'r') as f:
    file = f.read()

# file = """1
# 2
# -3
# 3
# -2
# 0
# 4"""
numbers = np.array([int(number) for number in file.split('\n')])
indices = np.arange(len(numbers))

for i, number in enumerate(numbers):
    start = indices[i]
    end = (indices[i] + number) % (len(numbers) - 1)
    # print(i, number, start, end)
    if number > 0:
        if start < end:
            indices[(start < indices) & (indices <= end)] -= 1
        elif end < start:
            indices[(end <= indices) & (indices < start)] += 1
    elif number < 0:
        if end < start:
            indices[(end <= indices) & (indices < start)] += 1
        elif start < end:
            indices[(start < indices) & (indices <= end)] -= 1
    indices[i] = end
    # print(numbers, indices, numbers[indices.argsort()])
    # print('next')

print(numbers[indices.argsort()][(indices[numbers == 0][0] + 1000) % len(numbers)])
print(numbers[indices.argsort()][(indices[numbers == 0][0] + 2000) % len(numbers)])
print(numbers[indices.argsort()][(indices[numbers == 0][0] + 3000) % len(numbers)])
print(numbers[indices.argsort()][(indices[numbers == 0][0] + 1000) % len(numbers)] +
      numbers[indices.argsort()][(indices[numbers == 0][0] + 2000) % len(numbers)] +
      numbers[indices.argsort()][(indices[numbers == 0][0] + 3000) % len(numbers)])
# 7395

# Part 2
numbers = np.array([int(number) for number in file.split('\n')], dtype="int64")
indices = np.arange(len(numbers))

DECRYPTION_KEY = 811589153
MIXES = 10
numbers *= DECRYPTION_KEY

for _ in range(MIXES):
    for i, number in enumerate(numbers):
        start = indices[i]
        end = (indices[i] + number) % (len(numbers) - 1)
        if number > 0:
            if start < end:
                indices[(start < indices) & (indices <= end)] -= 1
            elif end < start:
                indices[(end <= indices) & (indices < start)] += 1
        elif number < 0:
            if end < start:
                indices[(end <= indices) & (indices < start)] += 1
            elif start < end:
                indices[(start < indices) & (indices <= end)] -= 1
        indices[i] = end

print(numbers[indices.argsort()][(indices[numbers == 0][0] + 1000) % len(numbers)] +
      numbers[indices.argsort()][(indices[numbers == 0][0] + 2000) % len(numbers)] +
      numbers[indices.argsort()][(indices[numbers == 0][0] + 3000) % len(numbers)])
