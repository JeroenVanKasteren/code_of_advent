with open('day15', 'r') as f:
    file = f.read()

words = [word for word in file.split(',')]

res = 0
for word in words:
    sub_res = 0
    for letter in word:
        sub_res = ((sub_res + ord(letter)) * 17) % 256
    res += sub_res
print(res)
