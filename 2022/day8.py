import numpy as np

with open('day8', 'r') as f:
    file = f.read()

# file = """40352101405502025
# 32200320040431303
# 30022333120202211
# 32313340131230131
# 10110440304012304
# 02334320031232134
# 32313340131230131"""

# file = """30373
# 25512
# 65332
# 33549
# 35390"""

input = np.array([list(row) for row in file.split('\n')]).astype(int)
input_copy = input.copy()

visible = 2*len(input)+2*(len(input[0])-2)
for i in range(1, len(input)-1):
    for j in range(1, len(input[i])-1):
        current = input[i, j]
        # up, left, down, right
        visible += np.all(input[:i, j] < current) + np.all(input[i, :j] < current) + \
        np.all(input[i + 1:, j] < current) + np.all(input[i, j + 1:] < current) > 0
print(visible)

max_score = 0
for i in range(1, len(input)-1):
    for j in range(1, len(input[i])-1):
        current = input[i, j]
        # up
        score_up = 0
        for k in range(i-1, -1, -1):
            if input[k, j] >= current:
                score_up += 1
                break
            if k == i - 1:  # first tree
                score_up += 1
            # elif not np.any(input[range(i-1, k, -1), j] > input[k, j]):
            else:
                score_up += 1
        # left
        score_left = 0
        k = 1
        for k in range(j - 1, -1, -1):
            if input[i, k] >= current:
                score_left += 1
                break
            if k == j - 1:  # first tree
                score_left += 1
            # elif not np.any(input[i, range(j-1, k, -1)] > input[i, k]):
            else:
                score_left += 1
        # down
        score_down = 0
        for k in range(i+1, len(input)):
            if input[k, j] >= current:
                score_down += 1
                break
            if k == i+1:  # first tree
                score_down += 1
            # elif not np.any(input[range(i+1, k), j] > input[k, j]):
            else:
                score_down += 1
        # right
        score_right = 0
        for k in range(j+1, len(input[i])):
            if input[i, k] >= current:
                score_right += 1
                break
            if k == j + 1:  # first tree
                score_right += 1
            # elif not np.any(input[i, range(j+1, k)] > input[i, k]):
            else:
                score_right += 1
        score = score_up * score_left * score_down * score_right
        input_copy[i, j] = score
        max_score = max(score, max_score)

input_copy[0, :] = 0
input_copy[-1, :] = 0
input_copy[:, 0] = 0
input_copy[:, -1] = 0
print(input)
print(input_copy)
print(max_score)


with open('day8', 'r') as f:
    file = f.read()
grid = [[int(c) for c in line.rstrip('\n')] for line in file.split('\n')]
R, C = len(grid), len(grid[0])
grid_copy = np.array(grid.copy())

ans2 = 0
for r in range(R):
    for c in range(C):
        score = abs(c - next((cc for cc in range(c - 1, -1, -1) if grid[r][cc] >= grid[r][c]), 0))
        score *= abs(c - next((cc for cc in range(c + 1, C) if grid[r][cc] >= grid[r][c]), C - 1))
        score *= abs(r - next((rr for rr in range(r - 1, -1, -1) if grid[rr][c] >= grid[r][c]), 0))
        score *= abs(r - next((rr for rr in range(r + 1, R) if grid[rr][c] >= grid[r][c]), R - 1))
        grid_copy[r, c] = score
        ans2 = max(ans2, score)
print(f"part 2: {ans2}")
print(grid_copy)
