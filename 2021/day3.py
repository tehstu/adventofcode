# Advent of Code 2021
# Day 3

import pandas as pd

widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
df = pd.read_fwf('day3_input.txt', widths=widths, header=None)

gamma = ''
epsilon = ''

col_sum = df.sum()
#print(col_sum)

for row in col_sum:
    # sum of column > half # rows means 1 is most significant bit
    if row > len(df.index) / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Answer is: ", int(gamma, 2) * int(epsilon, 2))