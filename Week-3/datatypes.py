# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 03:09:28 2026

@author: Heet
"""

import pandas as pd
import numpy as np

# Reading data from csv
cars_data = pd.read_csv("Datasets/Toyota.csv", index_col=0) #index_col overrides default index

def main():
    # Lists data types
    print(cars_data.dtypes, '\n')
    
    # Lists each unique data type and its count
    print(cars_data.dtypes.value_counts(), '\n')
    
    # Selects data types based on data type
    print(cars_data.select_dtypes(exclude=[object]), '\n')
    
    # Concise summary of the dataframe
    print(cars_data.info(), '\n')
    
    # Unique elements in a column
    print(np.unique(cars_data['KM']), '\n')
    
if __name__ == "__main__":
    main()
    
