#Final Project Python Class

import numpy

numpy.loadtxt('proj_data/merged_foraging_data.csv', delimiter=',')

import pandas as pd

df = pd.read_csv('proj_data/merged_foraging_data.csv')
print(df)