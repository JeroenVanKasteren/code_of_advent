import scipy

with open('day21', 'r') as f:
    file = f.read()

report = [line.split(': ') for line in file.split('\n')]
monkeys = {}
for line in report:
    if line[1].isnumeric():
        monkeys[line[0]] = int(line[1])
    else:
        monkeys[line[0]] = line[1].split(' ')


def get_number(name):
    global monkeys

    if isinstance(monkeys[name], int):
        return monkeys[name]

    a = get_number(monkeys[name][0])
    b = get_number(monkeys[name][2])
    if monkeys[name][1] == '+':
        monkeys[name] = a + b
        return a + b
    elif monkeys[name][1] == '-':
        monkeys[name] = a - b
        return a - b
    elif monkeys[name][1] == '*':
        monkeys[name] = a * b
        return a * b
    elif monkeys[name][1] == '/':
        monkeys[name] = a / b
        return a / b


print(get_number('root'))

print(monkeys)
print(monkeys['root'])

# ###############################################################################################
# ########## part 2, solution with string formula (eval(string)) and scipy optimize #############
# ###############################################################################################

report = [line.split(': ') for line in file.split('\n')]
monkeys = {}
for line in report:
    if line[1].isnumeric():
        monkeys[line[0]] = float(line[1])
    else:
        monkeys[line[0]] = line[1].split(' ')


def normal_arithmatic(name, a, b):
    global monkeys

    if monkeys[name][1] == '+':
        monkeys[name] = a + b
        return a + b
    elif monkeys[name][1] == '-':
        monkeys[name] = a - b
        return a - b
    elif monkeys[name][1] == '*':
        monkeys[name] = a * b
        return a * b
    else:  # monkeys[name][1] == '/':
        monkeys[name] = a / b
        return a / b


def get_number_string(name):
    global monkeys

    if name == 'humn':
        return 'x'
    if isinstance(monkeys[name], float):
        return monkeys[name]

    a = get_number_string(monkeys[name][0])
    b = get_number_string(monkeys[name][2])
    if isinstance(a, float) and isinstance(b, float):
        return normal_arithmatic(name, a, b)
    return '('+str(a) + monkeys[name][1] + str(b)+')'


print(get_number_string(monkeys['root'][0]))
print(get_number_string(monkeys['root'][2]))

y = get_number_string(monkeys['root'][2])
formula = get_number_string(monkeys['root'][0]) + '-' + str(y)


def f(x):
    global formula

    return abs(eval(formula))


max_x = scipy.optimize.fmin(f, 10000000)
print('{:.20f}'.format(max_x[0]))

# ###############################################################################################
# ################################### part 2,puzzle solution ####################################
# ###############################################################################################

# file = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32"""


report = [line.split(': ') for line in file.split('\n')]
monkeys = {}
for line in report:
    if line[1].isnumeric():
        monkeys[line[0]] = float(line[1])
    else:
        monkeys[line[0]] = line[1].split(' ')


def normal_arithmatic(name, a, b):
    global monkeys

    if monkeys[name][1] == '+':
        monkeys[name] = a + b
        return a + b
    elif monkeys[name][1] == '-':
        monkeys[name] = a - b
        return a - b
    elif monkeys[name][1] == '*':
        monkeys[name] = a * b
        return a * b
    else:  # monkeys[name][1] == '/':
        monkeys[name] = a / b
        return a / b


def get_number2(name):
    global monkeys

    if name == 'humn':
        return 'x'
    elif isinstance(monkeys[name], float):
        return monkeys[name]

    a = get_number2(monkeys[name][0])
    b = get_number2(monkeys[name][2])
    if isinstance(a, float) and isinstance(b, float):
        return normal_arithmatic(name, a, b)
    elif isinstance(a, float):
        monkeys[monkeys[name][0]] = a
    elif isinstance(b, float):
        monkeys[monkeys[name][2]] = b
    return 'x'


def reverse_arithmatic(name, a, y, left):
    global monkeys

    if monkeys[name][1] == '+':
        monkeys[name] = y - a
        return y - a
    elif monkeys[name][1] == '-' and left:
        monkeys[name] = a - y
        return a - y
    elif monkeys[name][1] == '-' and not left:
        monkeys[name] = y + a
        return y + a
    elif monkeys[name][1] == '/' and left:
        monkeys[name] = a / y
        return a / y
    elif monkeys[name][1] == '/' and not left:
        monkeys[name] = a * y
        return a * y
    elif monkeys[name][1] == '*':
        monkeys[name] = y / a
        return y / a


def solve_x(name, y):
    global monkeys

    a = monkeys[monkeys[name][0]]
    b = monkeys[monkeys[name][2]]

    if monkeys[name][0] == 'humn':
        print(reverse_arithmatic(name, b, y, left=False))
    elif monkeys[name][2] == 'humn':
        print(reverse_arithmatic(name, a, y, left=True))
    elif isinstance(monkeys[name], float):
        return monkeys[name]
    elif isinstance(a, float):
        solve_x(monkeys[name][2], reverse_arithmatic(name, a, y, left=True))
    elif isinstance(b, float):
        solve_x(monkeys[name][0], reverse_arithmatic(name, b, y, left=False))


get_number2(monkeys['root'][0])
get_number2(monkeys['root'][2])

if isinstance(monkeys[monkeys['root'][0]], float):
    solve_x(monkeys['root'][2], monkeys[monkeys['root'][0]])
else:
    solve_x(monkeys['root'][0], monkeys[monkeys['root'][2]])
