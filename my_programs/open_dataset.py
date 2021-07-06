# phil welsby - 5 july 2021
# script to open a dataset and perform basic tests

#from os import system
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# change directory
os.chdir('/home/phil/ufo_sightings/csv')
# clear screen function
def cls():
    os.system('clear')

# clear screen
cls()

# get path to file
file = input('Copy path to Dataset file here: ')

# clear screen
cls()

# create dataframe
df = pd.read_csv(file, low_memory=False)

# print file name
print('File name is:', file)

# print instructions
print('''
NOTE, dataframe will be - df

Run this program using the -i switch if you haven't already done so!!!
''')

print('''
Basic tests run are:
df.head()
df.tail()
df.shape
df.dtypes
df.isna().sum()
''')

# wait
input('Hit ENTER to continue:')

# clear screen
cls()

# print file name
print('File name is:', file)
print('current directory is:', os.getcwd())
print()

# main
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
print()
