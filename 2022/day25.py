with open('day25', 'r') as f:
    file = f.read()

report = [line for line in file.split('\n')]


def base_to_deci(base, b):
    decimal = 0
    for digit in list(base):
        decimal = decimal * b + int(digit)
    return decimal


def snafu_to_deci(snafu):
    base_5 = list(snafu)
    for i in range(len(base_5)):
        if snafu[i] == '-':
            base_5[i] = 4
            base_5[i-1] = str(int(base_5[i-1]) - 1)
        elif snafu[i] == '=':
            base_5[i] = 3
            base_5[i-1] = str(int(base_5[i-1]) - 1)
    return base_to_deci(base_5, 5)


def convert_to_base(n, b):
    number = ''
    if n > b - 1:
        number = convert_to_base(n//b, b)
    return number + str(n % b)


def deci_to_snafu(deci):
    base_5 = convert_to_base(deci, 5)
    snafu = list(base_5)

    i = len(base_5) - 1
    while i >= 0:
        if int(snafu[i]) > 4:
            if i - 1 == -1:
                snafu.insert(0, '1')
                i += 1
            else:
                snafu[i-1] = str(int(snafu[i-1]) + 1)
        snafu[i] = str(int(snafu[i]) % 5)
        if snafu[i] == '3':
            snafu[i] = '='
            if i - 1 == -1:
                snafu.insert(0, '1')
                i += 1
            else:
                snafu[i-1] = str(int(snafu[i-1]) + 1)
        elif snafu[i] == '4':
            snafu[i] = '-'
            if i - 1 == -1:
                snafu.insert(0, '1')
                i += 1
            else:
                snafu[i-1] = str(int(snafu[i-1]) + 1)
        i -= 1
    return ''.join(snafu)


res = 0
for snafu_number in report:
    res += snafu_to_deci(snafu_number)
print(res)
print(convert_to_base(res, 5))
print(deci_to_snafu(res))
