# Advent of Code 2021
# Day 4 Part 2

import pandas as pd

# Read bingo number row, first line only
numbers = pd.read_csv('day4_input.txt', header=None, nrows=1)

# Read bingo card data (blank rows automatically ignored)
colspecs=[(0,2),(3,5),(6,8),(9,11),(12,14)]
df = pd.read_fwf('day4_input.txt', header=None, colspecs=colspecs)

# Drop the number row
df.drop([0],inplace=True)

# Convert dtype (read_fwf read last column as object, not int64)
cards_df = df.astype('int64')
original_df = cards_df

"""
Unsure how to do this the "Pythonic" way of using Pandas functions,
will therefore iterate over rows/cols.

"""
winning_card = 0
winning_number = 0
last_number = numbers.iloc[0,-1]

# Iterate over numbers
for num in range(len(numbers.columns)):
   
    # Replace next number with X if present on cards
    cards_df.replace(numbers.iloc[0,num], 'X', inplace=True)  

# Iterate over each bingo card
for i in range(0,len(cards_df.index),5):

    # For each row in card, look for presence of last number
    for j in range(5):
        for k in range(5):
            if original_df.iloc[i+j,k] == last_number:
            # TO DO: compare row to original_df to see if it's part of a bingo 

    # For each column in card, look for presence of last number
    # TO DO: as above

    # # Iterate over each bingo card
    # for i in range(0,len(cards_df.index),5):
    #     row_x = 0
    #     col_x = 0
    #     # Scan card's rows for 5 concurrent Xs
    #     for j in range(5):
    #         row_x = 0
    #         for k in range(5):
    #             if cards_df.iloc[i+j,k] == "X":
    #                 row_x += 1
        
    #     # Scan card's columns for 5 concurrent Xs
    #     for j in range(5):
    #         col_x = 0
    #         for k in range(5):
    #             if cards_df.iloc[i+k,j] == "X":
    #                 col_x += 1

    #     # Check to see if a row or column is all X
    #     if row_x == 5 or col_x == 5:
    #         winning_number = numbers.iloc[0,num]
    #         winning_card = i
    #         break

    # if winning_card != 0:
    #     break

# Sum unmarked numbers on winning card
winning_sum = 0
for i in range(5):
    for j in range(5):
        if cards_df.iloc[winning_card+i,j] != "X":
            winning_sum += cards_df.iloc[winning_card+i,j]

print("Answer :", winning_sum * winning_number)