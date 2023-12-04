import re

with open('day1', 'r') as f:
    s = f.read()
text = s.strip().split("\n")

# pattern = re.compile("\d")
pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

res = 0
for line in text:
    current = ''
    items = re.findall(pattern, line)
    first_and_last = [items[0], items[-1]]
    for item in first_and_last:
        if item in words:
            current += words[item]
        else:
            current += item
    print(line)
    print(current)
    res += int(current)
print(res)
