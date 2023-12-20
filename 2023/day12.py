import re
import numpy as np

with open('day12', 'r') as f:
    file = f.read().splitlines()


def check_valid(s, numbers):
    for number in numbers:
        match = re.search('[#?]{' + str(number) + '}', s)
        if match is None:
            return 0
        s = s[min(match.span()[1] + 1, len(s)):]
    return 1


def check_end(s, numbers):
    match = re.search('#', s)
    if len(numbers) == 0 and match is None:
        return 1
    elif len(numbers) == 0 and match is not None:
        return 0
    elif check_valid(s, numbers) == 0:
        return 0


def recursion_1(s, numbers):
    end = check_end(s, numbers)
    if end is not None:
        return end

    match = re.search('[#?]', s)
    s = s[match.span()[0]:]

    match = re.search('[#?]', s)
    options = 0
    if match.group()[0] == '#':
        if s[:numbers[0]].count('.') > 0:
            return 0
        if len(s) == numbers[0] or s[numbers[0]] in ['.', '?']:
            return recursion_1(s[numbers[0] + 1:], numbers[1:])
        else:
            return 0
    else:
        if s[:numbers[0]].count('.') == 0:
            if len(s) == numbers[0] or s[numbers[0]] in ['.', '?']:
                options += recursion_1(s[numbers[0] + 1:], numbers[1:])
        options += recursion_1(s[1:], numbers)
    return options


res = 0
for i, line in enumerate(file):  # [file[593]]):
    record, damaged = line.split(' ')
    damaged_groups = [int(i) for i in damaged.split(',')]
    res += recursion_1(record, damaged_groups)
print(res)


def max_pattern(x, s):
    pattern = '(^|\.|\?)#{' + str(x) + '}(\.|\?|$)'
    return list(re.finditer(pattern, s))


def max_patterns(x, s):
    pattern = '(?=(^[#?]{' + str(x) + '}$))'
    matches = [(0, match) for match in list(re.finditer(pattern, s))]
    pattern = '(?=((\.|\?)[#?]{' + str(x) + '}$))'
    matches.extend([(1, match) for match in list(re.finditer(pattern, s))])
    pattern = '(?=(^[#?]{' + str(x) + '}(\.|\?)))'
    matches.extend([(1, match) for match in list(re.finditer(pattern, s))])
    pattern = '(?=((\.|\?)[#?]{' + str(x) + '}(\.|\?)))'
    matches.extend([(2, match) for match in list(re.finditer(pattern, s))])
    return matches


def split_record(i, span, numbers, s, memory):
    n1 = numbers[:i]
    s1 = s[:span[0]]
    n2 = numbers[i + 1:]
    s2 = s[span[1]:]
    if check_valid(s1, n1) == 0 or check_valid(s2, n2) == 0:
        return 0, 0, memory
    else:
        option1, memory = recursion(s1, n1, memory)
        option2, memory = recursion(s2, n2, memory)
        return option1, option2, memory


def recursion(s, numbers, memory):
    if hash(str([s, numbers])) in memory:
        return memory[hash(str([s, numbers]))], memory
    end = check_end(s, numbers)
    if end is not None:
        memory[hash(str([s, numbers]))] = end
        return end, memory

    number, i = max(numbers), np.argmax(numbers)
    matches = max_pattern(number, s)
    if len(matches) > numbers.count(number):
        memory[hash(str([s, numbers]))] = 0
        return 0, memory
    elif numbers.count(number) == len(numbers) and len(matches) > 0:
        for match in matches:
            numbers = numbers[1:]
            s = (s[:match.span()[0]] + '.' * (match.span()[1] - match.span()[0])
                 + s[match.span()[1]:])
        options, memory = recursion(s, numbers, memory)
        memory[hash(str([s, numbers]))] = options
        return options, memory

    matches = max_patterns(number, s)
    options = 0
    for j, match in matches:
        span = (match.span()[0], min(match.span()[1] + number + j, len(s)))
        option1, option2, memory = split_record(i, span, numbers, s, memory)
        if option1 > 0 and option2 > 0:
            options += option1 * option2
    memory[hash(str([s, numbers]))] = options
    return options, memory


res = 0
multiplier = 5
for i, line in enumerate(file):  # [file[593]]):
    empty_memory = {}
    record, damaged = line.split(' ')
    record = ((record + '?') * multiplier)[:-1]
    damaged_groups = [int(i) for i in damaged.split(',')] * multiplier
    # print(record, damaged_groups)
    tmp, _ = recursion(record, damaged_groups, empty_memory)
    res += tmp
print(res)
# 28458170711449  # too low


# https://adventofcode.com/2023/day/12#part2
# This is the same code as the solution for part 1, with the addition of two lines to perform the 'unfolding'

# ways = 0
# for row in file:
#     record, checksum = row.split()
#     checksum = [int(n) for n in checksum.split(',')]
#     # record = '?'.join([record for i in range(5)])
#     # checksum *= 5
#     positions = {0: 1}
#     for i, contiguous in enumerate(checksum):
#         new_positions = {}
#         for k, v in positions.items():
#             for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
#                 if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
#                     if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) or (i < len(checksum) - 1 and n + contiguous < len(record) and record[n + contiguous] != '#'):
#                         new_positions[n + contiguous + 1] = new_positions[n + contiguous + 1] + v if n + contiguous + 1 in new_positions else v
#                 if record[n] == '#':
#                     break
#         positions = new_positions
#     ways += sum(positions.values())
# print(ways)