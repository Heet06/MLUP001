# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 02:25:16 2026

@author: Heet
"""

import pandas as pd

# Reading data from csv
cars_data = pd.read_csv("Datasets/Toyota.csv", index_col=0) #index_col overrides default index

def main():
    # Head and tails functions
    print(cars_data.head(6), '\n') # reads first six rows from the dataframe
    print(cars_data.tail(5), '\n') # reads last five rows from the  dataframe
    
    # Lookup Methods
    print(cars_data.at[4, 'FuelType'], '\n')
    
    print(cars_data.iat[5, 6], '\n')
    
    # To access group of rows and columns
    print(cars_data.loc[:   , 'FuelType'], "\n")
    
if __name__ == "__main__":
    main()
    