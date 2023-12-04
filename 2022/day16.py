import numpy as np

with open('day1X', 'r') as f:
    file = f.read()

report = [line.split(':') for line in file.split('\n')]
