# Advent of Code 2021
# Day 4

import pandas as pd
from progress.bar import Bar

# Read bingo number row, first line only
numbers = pd.read_csv('day4_input.txt', header=None, nrows=1)

# Read bingo card data (blank rows automatically ignored)
colspecs=[(0,2),(3,5),(6,8),(9,11),(12,14)]
cards_df = pd.read_fwf('day4_input.txt', header=None, colspecs=colspecs)

# Drop the number row
cards_df.drop([0],inplace=True)

line_df = pd.DataFrame(['X','X','X','X','X'])

# Provide progress bar for fun
with Bar('Processing') as bar:
    # Iterate over bingo numbers
    for i in range(len(numbers.columns)):
        # Mark X for numbers on cards matching bingo number
        num = numbers.iloc[0,i]
        cards_df.replace(num, 'X', inplace=True)

        # Search for completed bingo rows
        for index, row in cards_df.iterrows():
            if line_df.equals(row):
                print("Match at line: ", index)

        # Search for completed bingo columns
        bar.next()