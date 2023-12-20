import copy

with open('day19', 'r') as f:
    file = f.read()

workflow_data, items_data = file.split('\n\n')
workflows_data = [workflow.split('{') for workflow in workflow_data.split('\n')]

workflow = workflows_data[0]
rule_data = workflow[1].split(',')[0]
workflows = {}
for workflow in workflows_data:
    rules = []
    for rule_data in workflow[1].split(','):
        if rule_data[0] in ['A', 'R']:
            rules.append([rule_data[0]])
            continue
        if ':' not in rule_data:
            rules.append([rule_data[:-1]])
            continue
        rule, destination = rule_data.split(':')
        category, sign, number = rule[0], rule[1], rule[2:]
        rules.append([category, sign, int(number), destination])
    workflows[workflow[0]] = rules


items = []
for line in items_data.split('\n'):
    line = line[1:-1]
    categories = {}
    for item in line.split(','):
        category, number = item.split('=')
        categories[category] = int(number)
    items.append(categories)

res = 0
for item in items:
    value = sum(item.values())
    workflow = workflows['in']
    rule_i = 0
    while True:
        rule = workflow[rule_i]
        if rule[0] == 'A':
            res += value
            break
        elif rule[0] == 'R':
            break
        elif len(rule) == 1:
            rule_i = 0
            workflow = workflows[rule[0]]
        else:
            category, sign, number, destination = rule
            if sign == '>':
                if item[category] > number:
                    if destination == 'A':
                        res += value
                        break
                    elif destination == 'R':
                        break
                    workflow = workflows[destination]
                    rule_i = 0
                else:
                    rule_i += 1
            elif sign == '<':
                if item[category] < number:
                    if destination == 'A':
                        res += value
                        break
                    elif destination == 'R':
                        break
                    workflow = workflows[destination]
                    rule_i = 0
                else:
                    rule_i += 1
print(res)


# Part 2
class RangeObj:
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi

    def __copy__(self):
        return RangeObj(self.mini, self.maxi)

    def adjust(self, number, sign):
        if sign == '<':
            if self.mini < number:
                return False
            elif number < self.maxi:
                self.maxi = number
        else:  # sign == '>'
            if self.maxi < number:
                return False
            elif self.mini < number:
                self.mini = number
        return True

    def size(self):
        return self.maxi - self.mini + 1

    def combine(self, other_ranges):
        if other_ranges == []:
            return [self]
        for other_range in other_ranges:
            if other_range.mini < self.mini:
                self.mini = other_range.mini
            if other_range.maxi > self.maxi:
                self.maxi = other_range.maxi


category_letters = ['x', 'm', 'a', 's']
reverse_sign = {'<': '>', '>': '<'}
unknown_dict = {category: []
                for category in category_letters}
accepted_dict = {category: [RangeObj(0, 4000)]
                 for category in category_letters}

v = {}
for destination, rules in workflows.items():
    rule_dicts = []
    for rule in rules:
        if rule[0] == 'A':
            rule_dicts.append(accepted_dict)
        elif rule[0] == 'R':
            rule_dicts.append(unknown_dict)
        else:
            rule_dicts.append(unknown_dict)
    v[destination] = rule_dicts


# def combine_ranges(rule_range, other_range):
#     continue_min = max(rule_range[0], other_range[0])
#     continue_max = min(rule_range[1], other_range[1])
#     if continue_min > continue_max:
#         continue_min, continue_max = -1, 4000 + 1
#     return continue_min, continue_max
#
#
# def combine_dict(category, new_range, destination_dict, next_dict):
#     if destination_dict == unknown_dict:
#         new_dict = copy.deepcopy(next_dict)
#         new_dict[category] = new_range
#         return new_dict
#     elif next_dict == unknown_dict:
#         new_dict = copy.deepcopy(destination_dict)
#         new_dict[category] = new_range
#         return new_dict
#     new_dict = copy.deepcopy(unknown_dict)
#     new_dict[category] = new_range
#     other_categories = set(category_letters).difference(category)
#     for other_category in other_categories:
#         rule_range = next_dict[other_category]
#         other_range = destination_dict[other_category]
#         continue_min = max(rule_range[0], other_range[0])
#         continue_max = min(rule_range[1], other_range[1])
#         new_dict[other_category] = [continue_min, continue_max]
#     return new_dict


def one_step_look_ahead(v_t, origin, rule, rule_i):
    category, sign, number, destination = rule
    if destination == 'A':
        destination_dict = copy.deepcopy(accepted_dict)
    elif destination == 'R':
        destination_dict = copy.deepcopy(unknown_dict)
    else:
        destination_dict = v_t[destination][0]
    next_dict = v_t[origin][rule_i + 1]
    # exclude part of range based on condition
    for range_obj in destination_dict[category]:
        outcome = range_obj.adjust(number, sign)
        if outcome is False:
            destination_dict[category].remove(range_obj)
    for range_obj in next_dict[category]:
        outcome = range_obj.adjust(number, reverse_sign[sign])
        if outcome is False:
            next_dict[category].remove(range_obj)
    # combine all ranges

    # if destination_dict != unknown_dict:
    #     rule_range = combine_ranges(rule_range, destination_dict[category])
    # else:
    #     rule_range = [4000 + 1, -1]
    # if next_dict != unknown_dict:
    #     continue_range = combine_ranges(continue_range, next_dict[category])
    # else:
    #     continue_range = [4000 + 1, -1]
    # new_range = [min(rule_range[0], continue_range[0]),
    #              max(rule_range[1], continue_range[1])]
    # return combine_dict(category, new_range, destination_dict, next_dict)


for n in range(1000):
    v_t = copy.deepcopy(v)
    for origin, rules in workflows.items():
        for rule_i, rule in enumerate(rules):
            if rule[0] in ['A', 'R']:
                continue
            if len(rule) == 1:
                v[origin][rule_i] = v_t[rule[0]][0]
                print(origin, rule_i, v[origin][rule_i])
                continue
            v[origin][rule_i] = one_step_look_ahead(v_t, origin, rule, rule_i)
            print(origin, rule_i, v[origin][rule_i])
    print('\n')
    if v_t == v:
        break

res = 1
for category_ranges in v['in'][0].values():
    sizes = 0
    for category_range in category_ranges:
        sizes += category_range.size()
    res *= sizes
print(res)

###########################################################################


# Day 19.2
# deepcopy object correctly?
# Remove _copy_ or add _deepcopy_
#
# ranges_dict1
# ranges_dict2
# new = copy.deepcopy(unknown_dict)
#
# for every category
# if len(ranges_dict1[category]) == 0:
# new_ranges = ranges_dict2[category]
# continue
# elif len(ranges_dict2[category]) == 0:
# new_ranges = ranges_dict1[category]
# continue
#
# new_ranges = []
# ranges1 = copy.deepcopy(ranges_dict1[category])
# ranges2 = copy.deepcopy(ranges_dict2[category])
#
# for i, range1 in enu( ranges1):
# add1 = false
# for range2 in ranges2:
#
# if range1.maxi < range2.mini
# add1 = true
# break
#
# elif range1.maxi < range2.maxi:
# range2.mini = min(range1.mini, range2.mini)
# break
#
# elif range1.mini < range2.maxi
# range2.mini = min(range1.mini, range2.mini)
# range2.maxi = max(range1.maxi, range2.maxi
# )
# add range2 to new
# remove range2 from ranges2
# break
#
# else:
# add range2 to new
# remove range2 from ranges2
# break
#
# if i == len(ranges 1) - 1:
# for range2 in ranges2:
# add range2
#
# # only happens if smaller than all ranges2 or bigger, otherwise merged with range2
# If add1 == true:
# add range1
