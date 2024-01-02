import numpy as np
import re

np.set_printoptions(linewidth=150)

with open('day22', 'r') as f:
    file = f.read()

# Day 22
#
# bricks = np.array([line.split([',', '~']) for line in file.split \n], dtype=int)
# # x, y, z, x, y, z
# max_x, max_y = max(bricks[, [0, 3]]), max(bricks[:, [1, 4]])
# assume
# min_x, min_y = 0, 0
# heights = np.zeros((max_x, max_y))
#
# z_mins = np.min(bricks[:, [2, 5]], axis=1?)
# np.argsort(z_mins)
# for i in np.argsort(z_mins):
# # Fall
# x1, y1, z1, x2, y2, z2 = bricks[i]
# # assume sorted that w1 < w2
# fall = z1 - (max(heights[x1:x2+1, y1:y2+1]) + 1)
# z1, z2 = z1 - fall, z2 - fall
# heights[x1:x2+1, y1:y2+1] = z2
# bricks[[2, 5]] = z1, z2
#
# Create tower = numpy zeros for maxx, maxy, maxz
#
# # after fall
# tower[x1:x2+1, y1:y2+1, z1:z2+1] = i. # ith brick, some ID
#
# Afterwards, for every brick, check who it supports, if every leaning brick has more than 1 supporter, res += 1
# leaning = set(tower[x1:x2+1, y1:y2+1, z2+1]).difference([0]))
# if safe(leaning):
# res +=1
#
# def safe(leaning):
# for x1, x2, ... in leaning
# supporters = set(tower[x1:x2+1, y1:y2+1, z1-1]).difference([0]))
# if supporters == 1
# return false
# end for
# return true
