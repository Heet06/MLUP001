# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:36:08 2026

@author: Heet
"""

import pandas as pd
import numpy as np

tips_data = pd.read_csv('Datasets/Tips.csv')

x = tips_data['TotalBill']
y = tips_data['Tips']

diff_x = x - np.nanmean(x)
diff_y = y - np.nanmean(y)

std_x = np.nanstd(x)
std_y = np.nanstd(y)

corr = ((diff_x * diff_y).sum() / len(x - 1))/(std_x * std_y) 

print(corr)

print(max(tips_data['TotalBill']) - min(tips_data['TotalBill']))

print(tips_data.isna().sum())

print(max(tips_data['TotalBill']))

print(tips_data['TotalBill'][int(3*(len(tips_data)/4))])