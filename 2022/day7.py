class Tree:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0
        self.total_size = 0

    def add_child(self, name):
        if name not in self.children:
            child = Tree(name, self)
            self.children.append(child)
        return child

    def get_child(self, name):
        if len(self.children):
            for child in self.children:
                if child.name == name:
                    return child
        return self.add_child(name)

    def get_size(self):
        res = self.size
        if len(self.children):
            for child in self.children:
                res += child.get_size()
        self.total_size = res
        return res

    def get_small_size(self, threshold):
        res = self.total_size if self.total_size <= threshold else 0
        if len(self.children):
            for child in self.children:
                res += child.get_small_size(threshold)
        return res

    def small_directory(self, space_to_delete, current_best):
        if len(self.children):
            for child in self.children:
                current_best = child.small_directory(space_to_delete, current_best)
        if current_best > self.total_size >= space_to_delete:
            return self.total_size
        return current_best

with open('day7', 'r') as f:
    lines = f.read()

commands = lines.split('\n')
root = Tree('/', 0)
pointer = root
i = 0

while i < len(commands):
    if commands[i] == '$ ls':
        i += 1
        while commands[i][0] != '$':
            element = commands[i].split(' ')
            if element[0] == 'dir':
                pointer.add_child(element[1])
            elif element[0].isnumeric():
                pointer.size += int(element[0])
            i = i + 1
            if i == len(commands):
                break
    if i == len(commands):
        break
    if commands[i] == '$ cd /':
        pointer = root
    elif commands[i] == '$ cd ..':
        pointer = pointer.parent
    elif commands[i][:4] == '$ cd':
        element = commands[i].split(' ')
        pointer = pointer.get_child(element[2])
    else:
        print(commands[i])
        break
    i += 1

print(root.get_size())
print(root.get_small_size(100000))
total = 70000000
needed = 30000000
current_free = total - root.total_size
space_to_delete = needed - current_free
print(space_to_delete)
print(root.small_directory(space_to_delete, root.total_size))
