with open('day1', 'r') as f:
    # with open('day1', 'r') as f:
    lines = f.readlines()
    calories = [line.strip() for line in lines]

res = 0
current = 0
for item in calories:
    if item == '':
        res = current if current > res else res
        current = 0
    else:
        current += int(item)
print(res)

# copycat
with open('day1', 'r') as f:
    s = f.read()
s = s.strip().split("\n\n")
s = [[int(x) for x in y.split("\n")] for y in s]

sum(sorted([sum(z) for z in s], reverse=True)[:3])
