# phil welsby - 5 july 2021
# script to open a dataset and perform basic tests

from os import system
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# clear screen
system('clear')

# get path to file
file = input('Copy path to Dataset file here: ')

# create dataframe
df = pd.read_csv(file)

# print instructions
print('''
NOTE, dataframe will be - df

Run this program using the -i switch if you haven't already done so!!!
''')

# print basic tests
print('''
Basic tests run are:
df.head()
df.tail()
df.shape
df.dtypes
df.isna().sum()
''')
input('Hit ENTER to continue:')

# clear screen
system('clear')


print('df.head()')
print(df.head())
print('\ndf.tail()')
print(df.tail())
print('\ndf.shape')
print(df.shape)
print('\ndf.dtypes')
print(df.dtypes)
print('\ndf.isna().sum()')
print(df.isna().sum())

