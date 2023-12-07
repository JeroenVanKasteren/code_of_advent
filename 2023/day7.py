"""
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456

    jokers and full house:
    with 3 or more jokers, make four or five of a kind.
    with 2 jokers, need other 2 pair --> which would be a better 4 kind.
    with 1 joker, need one 2 pair (a 3 kind would make 4 kind)
"""

from functools import cmp_to_key
from collections import Counter
import numpy as np

with open('day7', 'r') as f:
    s = f.read()

hands = s.split('\n')

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def poker(cards):
    counted = Counter(cards)
    cards_ordered = sorted(counted.items(), key=lambda x: x[1], reverse=True)
    counts = [x[1] for x in cards_ordered]

    if len(counted) == 1:
        return 6
    elif cards_ordered[0][0] != 'J':
        most = cards_ordered[0][1] + counted['J']
    elif cards_ordered[1][0] != 'J':
        most = cards_ordered[1][1] + counted['J']

    if most == 5:
        return 6  # + order.index(next(iter(counted)))/len(order)
    if most == 4:
        return 5
    if (3 in counts and 2 in counts) or \
            (counted['J'] == 1 and counts.count(2) == 2):
        return 4
    if most == 3:
        return 3
    if counts.count(2) == 2 or (counted['J'] == 1 and counts.count(2) == 1):
        return 2
    if most == 2:
        return 1
    else:
        return 0

# def sort_cards(cards):
#     return sorted(cards, key=lambda x: order.index(x))

def compare(hand1, hand2):
    cards1, _ = hand1.split(' ')
    cards2, _ = hand2.split(' ')
    if poker(cards1) > poker(cards2):
        return 1
    elif poker(cards1) < poker(cards2):
        return -1
    else:
        # cards1, cards2 = sort_cards(cards1), sort_cards(cards2)
        for i in range(len(cards1)):
            if order.index(cards1[i]) < order.index(cards2[i]):
                return 1
            elif order.index(cards1[i]) > order.index(cards2[i]):
                return -1
        return 0


hands = sorted(hands, key=cmp_to_key(compare))

res = np.int64(0)
for i, hand in enumerate(hands):
    # print(i, hand)
    res += int(hand.split(' ')[1]) * (1 + i)

print(res)
# 245932138,
# 245629854, too high
# 245745061, too high
# 245540388
