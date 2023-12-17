import re
import numpy as np

with open('day12', 'r') as f:
    file = f.read().splitlines()


def exact_pattern(x):
    return ('(^#{' + str(x) + '}(\.))'
            + '|((\.)#{' + str(x) + '}(\.))'
            + '|((\.)#{' + str(x) + '}$)')


def max_pattern(x):
    return ('(^#{' + str(x) + '}(\.|\?))'
            + '|((\.|\?)#{' + str(x) + '}(\.|\?))'
            + '|((\.|\?)#{' + str(x) + '}$)')


def recursion(s, numbers):
    match = re.search('#', s)
    if len(numbers) == 0 and match is None:
        return 1
    elif len(numbers) == 0 and match is not None:
        return 0

    match = re.search('[#?]', s)
    if match is None:
        return 0
    s = s[match.span()[0]:]
    if len(s) < sum(numbers):
        return 0

    number, i = max(numbers), np.argmax(numbers)
    pattern = max_pattern(number)
    matches = list(re.finditer(pattern, s))
    if len(matches) > numbers.count(number):
        return 0
    elif len(matches) == numbers.count(number):
        n1 = numbers[:i]
        s1 = s[:matches[0].span()[0]]
        option1 = recursion(s1, n1)
        n2 = numbers[i + 1:]
        s2 = s[matches[0].span()[1]:]
        option2 = recursion(s2, n2)
        if option1 > 0 and option2 > 0:
            return option1 * option2
        else:
            return 0
    elif numbers.count(number) == len(numbers) and len(matches) > 0:
        for match in matches:
            numbers = numbers[1:]
            s = s[:match.span()[0]] + '.' + s[match.span()[1]:]
        return recursion(s, numbers)
    for i, number in enumerate(numbers):
        if numbers.count(number) == 1:
            pattern = exact_pattern(number)
            matches = list(re.finditer(pattern, s))
            if len(matches) > numbers.count(number):
                return 0
            if len(matches) == numbers.count(number):
                n1 = numbers[:i]
                s1 = s[:matches[0].span()[0]]
                option1 = recursion(s1, n1)
                n2 = numbers[i + 1:]
                s2 = s[matches[0].span()[1]:]
                option2 = recursion(s2, n2)
                if option1 > 0 and option2 > 0:
                    return option1 * option2
                else:
                    return 0

    match = re.search('[#?]', s)
    options = 0
    if match.group()[0] == '#':
        if s[:numbers[0]].count('.') > 0:
            return 0
        if len(s) == numbers[0] or s[numbers[0]] in ['.', '?']:
            return recursion(s[numbers[0] + 1:], numbers[1:])
        else:
            return 0
    else:
        if s[:numbers[0]].count('.') == 0:
            if len(s) == numbers[0] or s[numbers[0]] in ['.', '?']:
                options += recursion(s[numbers[0] + 1:], numbers[1:])
        options += recursion(s[1:], numbers)
    return options


res = 0
multiplier = 5
for line in file:
    record, damaged = line.split(' ')
    record = ((record + '?') * multiplier)[:-1]
    damaged_groups = [int(i) for i in damaged.split(',')] * multiplier
    tmp = recursion(record, damaged_groups)
    print(tmp)
    res += tmp
print(res)
