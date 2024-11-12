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

#calculating the Coefficient of Variance for the following two columns in the hf dataset.
ss_cp = hf[["serum_sodium", "creatinine_phosphokinase"]]

cv = lambda x: np.std(x, ddof=1)/np.mean(x)*100

print(hf.apply(cv))


x = hf.iloc[:, 4]
y = hf.iloc[:,-6]

plt.scatter(x, y, alpha=0.75)
plt.show()


model = KMeans(n_clusters=2)
