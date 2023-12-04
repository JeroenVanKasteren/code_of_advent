import numpy as np

with open('day3', 'r') as f:
    s = f.read()

lines = s.strip().split("\n")

directions = [(1, 0), (1, -1), (0, -1),
              (-1, -1), (-1, 0), (-1, 1),
              (0, 1), (1, 1)]

symbol = False
number = ''
res = 0


def valid(x, y):
    return (0 <= x < len(lines[0])) and (0 <= y < len(lines))


def check_symbol(x, y):
    for direction in directions:
        x_n, y_n = x + direction[0], y + direction[1]
        if valid(x_n, y_n):
            if direction in [(1, 0), (-1, 0)]:
                if not (lines[y_n][x_n].isdigit() or (lines[y_n][x_n] == '.')):
                    return True
            else:
                if not (lines[y_n][x_n] == '.'):
                    return True
    return False


for y in range(len(lines)):
    for x in range(len(lines[y])):
        last_number = (x == len(lines[y]) - 1) \
                      or (not lines[y][x + 1].isdigit())
        if lines[y][x].isdigit():
            number += lines[y][x]
            if check_symbol(x, y):
                symbol = True
            if last_number & symbol:
                res += int(number)

        if last_number:
            number = ''
            symbol = False

print(res)

# Is a number also a symbol?
# 533421, too low
# 535078, correct

symbol = False
res = 0


def return_number(x, y):
    number = lines[y][x]
    # get all numbers right from it
    x_n = x + 1
    while valid(x_n, y) and lines[y][x_n].isdigit():
        number = number + lines[y][x_n]
        x_n = x_n + 1
    # get all numbers left form it
    x_n = x - 1
    while valid(x_n, y) and lines[y][x_n].isdigit():
        number = lines[y][x_n] + number
        x_n = x_n - 1
    return int(number)

def check_numbers(x, y, count, res):
    if valid(x, y) and lines[y][x].isdigit():
        res *= return_number(x, y)
        count += 1
    return count, res

def check_gear(x, y):
    count = 0
    res = 1

    # number right
    x_n, y_n = x + 1, y + 0
    count, res = check_numbers(x_n, y_n, count, res)

    # number left
    x_n, y_n = x - 1, y + 0
    count, res = check_numbers(x_n, y_n, count, res)

    # number(s) up
    x_n, y_n = x + 0, y - 1
    if valid(x_n, y_n) and (not lines[y_n][x_n].isdigit()):
        x_n, y_n = x - 1, y - 1
        count, res = check_numbers(x_n, y_n, count, res)
        x_n, y_n = x + 1, y - 1
        count, res = check_numbers(x_n, y_n, count, res)
    else:
        count, res = check_numbers(x_n, y_n, count, res)

    # number(s) down
    x_n, y_n = x + 0, y + 1
    if valid(x_n, y_n) and (not lines[y_n][x_n].isdigit()):
        x_n, y_n = x - 1, y + 1
        count, res = check_numbers(x_n, y_n, count, res)
        x_n, y_n = x + 1, y + 1
        count, res = check_numbers(x_n, y_n, count, res)
    else:
        count, res = check_numbers(x_n, y_n, count, res)

    if count == 2:
        return res
    else:
        return 0


for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '*':
            res += check_gear(x, y)
print(res)
