# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:15:52 2024

@author: lavig
"""

from sklearn import KMeans
import pandas as pd


hf = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(hf.head())
