# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 02:00:26 2026

@author: Heet
"""

import pandas as pd

# Reading data from csv
cars_data = pd.read_csv("Datasets/Toyota.csv", index_col=0) #index_col overrides default index

def main():
    # Row labels
    print(cars_data.index)
    
    # Column labels
    print(cars_data.columns)
    
    # Size
    print(cars_data.size) # 1436 rows * 10 columns = 14360
    
    # Shape
    print(cars_data.shape) # (1436 rows, 10 columns)
    
    # Memory Usage
    print(cars_data.memory_usage())
    
    # Dimensions
    print(f"Dimensions: {cars_data.ndim}")
    
if __name__ == "__main__":
    main()