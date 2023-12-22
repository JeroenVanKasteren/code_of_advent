with open('day15', 'r') as f:
    file = f.read()

words = [word for word in file.split(',')]


def hashmap(word):
    res = 0
    for letter in word:
        res = ((res + ord(letter)) * 17) % 256
    return res


print(sum([hashmap(word) for word in words]))

# Part 2
boxes = {}  # Key = nr of box, Value = [[Labels], [focus]]


def remove(number, label, boxes):
    if number in boxes and label in boxes[number][0]:
        index = boxes[number][0].index(label)
        boxes[number][0].pop(index)
        boxes[number][1].pop(index)
        return boxes, index
    if number in boxes:
        return boxes, len(boxes[number][0])
    return boxes, 0


word = words[0]
for word in words:
    if word[-1] == '-':
        label = word[:-1]
        boxes, index = remove(hashmap(label), label, boxes)
    else:
        label, focus = word.split('=')
        number = hashmap(label)
        boxes, index = remove(hashmap(label), label, boxes)
        if number not in boxes:
            boxes[number] = [[], []]
        boxes[number][0].insert(index, label)
        boxes[number][1].insert(index, int(focus))


res = 0
for box_nr, (labels, focuses) in boxes.items():
    for i, focus in enumerate(focuses):
        res += (box_nr + 1) * (i + 1) * focus
print(res)
