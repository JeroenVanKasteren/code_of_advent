with open('day14', 'r') as f:
    file = f.read()

data = [row for row in file.split('\n')]
data = [''.join(column) for column in list(zip(*data))]

res = 0
max_load = len(data[0])
for c in range(len(data)):
    current = 0
    while current < len(data[c]):
        rocks = 0
        for i in range(current, len(data[c])):
            if data[c][i] == 'O':
                res += max_load - current - rocks
                rocks += 1
            if data[c][i] == '#' or i == len(data[c]) - 1:
                current = i + 1
                break
print(res)

    # Do not forget last pilar!

# Per column
# Findall #
# For every # + 1
# If last
# sub_string = string[current:]
# Else
# sub_string = string[current: index #]
#
# For i in len sub string
# If i < sub_string.count(O)
# Place[current + i] = O
# Else
# Place[current + i] = .
