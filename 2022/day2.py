# 1 for rock (A/X), 2 for paper (B/Y), 3 for scissors (C/Z)
# 0 for loss, 3 for draw, 6 for win

with open('day2', 'r') as f:
    s = f.read()
rounds = [x.split(" ") for x in s.split("\n")]

outcomes = [ord(play) - ord(opp) - (ord('X') - ord('A')) for opp, play in rounds]
res = (outcomes.count(1) + outcomes.count(-2)) * 6 + outcomes.count(0) * 3
res += sum([ord(play) - ord("X") + 1 for opp, play in rounds])
print(res)  # 13565

# x lose, y draw, z win
res = sum([(ord(play) - ord('X')) * 3 for opp, play in rounds])
# draws
res += sum([(ord(opp) - ord('A') + 1) * (play == 'Y') for opp, play in rounds])
# wins
res += sum([((ord(opp) - ord('A') + 2) % 3 + 1) * (play == 'Z') for opp, play in rounds])
# res += sum([(play == 'Z' and opp == 'C') for opp,play in rounds])
# loses
res += sum([((ord(opp) - ord('A')) % 3 + 1) * (play == 'X') for opp, play in rounds])
# res += 3*sum([(play == 'X' and opp == 'A') for opp, play in rounds])
print(res)  # 12424

[(ord(x) - ord('A') + 2) % 3 + 1 for x in ['A', 'B', 'C']]
[(ord(x) - ord('A')) % 3 + 1 for x in ['A', 'B', 'C']]

import numpy as np

rounds_array = np.array(rounds)
numbers = np.array([[ord(x[0]) for x in row] for row in rounds])
numbers[:, 0] += -ord('A') + 1
numbers[:, 1] += -ord('X') + 1
diff = numbers[:, 1] - numbers[:, 0]
sum(((diff == 1) | (diff == -2))*6 + (diff == 0)*3 + (numbers[:, 1]))

res = sum((numbers[:, 1]-1) * 3 +
          numbers[:, 0]*(numbers[:, 1] == 2) +
          (numbers[:, 0] % 3 + 1) * (numbers[:, 1] == 3) +
          ((numbers[:, 0] + 1) % 3 + 1) * (numbers[:, 1] == 1))
