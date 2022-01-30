# Advent of Code 2021
# Day 3 Part 2

import pandas as pd

widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
df = pd.read_fwf('day3p2_input.txt', widths=widths, header=None)

#widths = [1, 1, 1, 1, 1]
#df = pd.read_fwf('day3p2_test_input.txt', widths=widths, header=None)

# calculate oxygen binary value
oxygen_df = df
oxygen = ''
col = 0

# loop until only 1 row remains
while len(oxygen_df.index) > 1:
    # determine least common bit for current column
    # if equal 1s and 0s, use 0 as least common bit
    if oxygen_df[col].sum() >= len(oxygen_df.index) - oxygen_df[col].sum():
        least_bit = 0
    else:
        least_bit = 1

    # drop rows where value in column col equals least common bit
    oxygen_df = oxygen_df[oxygen_df[col] != least_bit]

    # move to next col in remaining df
    col += 1

# convert remaining df row to binary string
for i in range(len(oxygen_df.columns)):
    oxygen += str(oxygen_df[i].values[0])

# calculate carbon binary value
carbon_df = df
carbon = ''
col = 0

# loop until only 1 row remains
while len(carbon_df.index) > 1:
    # determine least common bit for current column
    # if equal 1s and 0s, use 0 as least common bit
    if carbon_df[col].sum() >= len(carbon_df.index) - carbon_df[col].sum():
        least_bit = 1
    else:
        least_bit = 0

    # drop rows where value in column col equals least common bit
    carbon_df = carbon_df[carbon_df[col] != least_bit]

    # move to next col in remaining df
    col += 1

# convert remaining df row to binary string
for i in range(len(carbon_df.columns)):
    carbon += str(carbon_df[i].values[0])

print("Answer = ", int(oxygen, 2) * int(carbon, 2))