# Advent of Code 2021
# Day 1

import pandas as pd

df = pd.read_csv("day1_input.txt", header=None)

increase = 0

for i in range(len(df.index) - 1):
    current = df[0][i]
    next = df[0][i+1]
    if next > current:
        increase += 1

print("Number of increases = ", increase)