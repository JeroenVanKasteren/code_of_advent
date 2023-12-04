import numpy as np

with open('day19', 'r') as f:
    file = f.read()

numbers = np.array([int(number) for number in file.split('\n')])
