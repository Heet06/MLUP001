# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 12:31:16 2026

@author: Heet
"""

import pandas as pd
import numpy as np

# Replaces missing/incorrect values with 'nan'
cars_data = pd.read_csv('datasets/Toyota.csv', index_col=0, na_values=['??', '????'])

print(cars_data['FuelType'], '\n')
print(cars_data.info(), '\n')

# Changes datatype of columns
cars_data['Automatic'] = cars_data['Automatic'].astype('object')
cars_data['MetColor'] = cars_data['MetColor'].astype('object')

print(cars_data.info(), '\n')


# Memory usage by different data types
print("Data Consumed by FuelType: ", cars_data['FuelType'].nbytes)

print("Data Consumed by FuelType (category): ", cars_data['FuelType']\
      .astype('category').nbytes, '\n')

print(cars_data.info(), '\n')

# Unique values in a column
print(np.unique(cars_data['Doors']), "\n")

# replace ambigous values with correct values
cars_data['Doors'] = cars_data['Doors'].replace({'three': 3, 'four': 4, 'five': 5})

# converts column type from object to int64
cars_data['Doors'] = pd.to_numeric(cars_data['Doors'], errors='coerce').astype('Int64')

print(np.unique(cars_data['Doors']), '\n')

# Counting null values for each column
print(cars_data.isna().sum(), '\n')

