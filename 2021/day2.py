# Advent of Code 2021
# Day 2

import pandas as pd

df = pd.read_csv('day2_input.txt', header=None, sep=' ')
df.columns = ['direction', 'value']

# Using dataframe filtering
df_horz_position = df.loc[df['direction'] == 'forward', 'value'].sum()
df_down = df.loc[df['direction'] == 'down', 'value'].sum()
df_up = df.loc[df['direction'] == 'up', 'value'].sum()

df_depth = df_down - df_up

print('Dataframe filtering answer =', df_horz_position * df_depth)

# Using iteration
iter_horz_position = 0
iter_down = 0
iter_up = 0
for row in df.itertuples():
    if row.direction == 'forward':
        iter_horz_position += row.value
    if row.direction == 'down':
        iter_down += row.value
    if row.direction == 'up':
        iter_up += row.value
iter_depth = iter_down - iter_up

print('Iteration answer =', iter_horz_position * iter_depth)