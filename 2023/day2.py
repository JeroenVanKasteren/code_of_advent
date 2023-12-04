import numpy as np

with open('day2', 'r') as f:
    s = f.read()

games = [game.strip().split(":")[1] for game in s.strip().split("\n")]
games = [[draw.strip().split(', ') for draw in draws.strip().split(';')]
         for draws in games]

limit = {'red': 12, 'green': 13, 'blue': 14}
res = 0
for i, game in enumerate(games):
    game_possible = True
    for draw in game:
        for balls in draw:
            n, color = balls.strip().split(' ')
            if int(n) > limit[color]:
                game_possible = False
    if game_possible:
        res += i + 1
print(res)

res = 0
for i, game in enumerate(games):
    power_per_color = {'red': 0, 'green': 0, 'blue': 0}
    for draw in game:
        for balls in draw:
            n, color = balls.strip().split(' ')
            if int(n) > power_per_color[color]:
                power_per_color[color] = int(n)
    res += np.array(list(power_per_color.values())).prod()
print(res)
