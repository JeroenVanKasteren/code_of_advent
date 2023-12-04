with open('day6', 'r') as f:
    s = f.read()

for i in range(len(s)):
    if len(set(s[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(s)):
    if len(set(s[i:i+14])) == 14:
        print(i+14)
        break
