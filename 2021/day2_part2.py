# Advent of Code 2021
# Day 2 Part 2

import pandas as pd

df = pd.read_csv('day2_input.txt', header=None, sep=' ')
df.columns = ['direction', 'value']

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.

position = 0
depth = 0
aim = 0

# Using iteration
for row in df.itertuples():
    if row.direction == 'forward':
        position += row.value
        depth += aim * row.value
    if row.direction == 'down':
        aim += row.value
    if row.direction == 'up':
        aim -= row.value

print('Answer =', position * depth)