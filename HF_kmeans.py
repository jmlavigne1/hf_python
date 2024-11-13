# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:15:52 2024

@author: lavig
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.environ["OMP_NUM_THREADS"] = '4'

hf = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(hf.head())

print(hf.columns)

#calculating the Coefficient of Variance for the following two columns in the hf dataset.
ss_cp = hf[["serum_sodium", "creatinine_phosphokinase"]]

cv = lambda x: np.std(x, ddof=1)/np.mean(x)*100

print(hf.apply(cv))


x = hf.iloc[:,2] #creatinine_phosphokinase
y = hf.iloc[:,8] #serum_sodium

plt.scatter(x, y, alpha=0.50)
plt.title("Creatinine Phosphokinase vs. Serum Sodium")
plt.xlabel("Serum Creatinine")
plt.ylabel("Serum Sodium")
plt.show()



model = KMeans(n_clusters=4)
model.fit(hf)
labels = model.predict(hf)
print(labels)


x = hf.iloc[:,2]
y = hf.iloc[:,8]


plt.scatter(x, y, c=labels, alpha=0.5)
plt.show()
