# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:15:52 2024

@author: lavig
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


hf = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(hf.head())

print(hf.columns)

x = hf.iloc[:, 4]
y = hf.iloc[:,-1]

plt.scatter(x, y, alpha=0.5)
plt.show()


model = KMeans(n_clusters=2)
