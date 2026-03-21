# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 01:10:36 2026

@author: Heet
"""

import pandas as pd

# Reading data from csv
cars_data = pd.read_csv("Datasets/Toyota.csv", index_col=0) # index_col overrides default index

def main():    
    # Shallow Copy Methods    
    shallow_copy = cars_data.copy(deep=False)
    shallow_copy1 = cars_data
    
    # Deep Copy Methods
    deep_copy = cars_data.copy(deep=True) # by default deep = True
    
    del shallow_copy
    del shallow_copy1
    del deep_copy

if __name__ == "__main__":
    main()