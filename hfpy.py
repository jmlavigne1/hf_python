# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 06:45:47 2024

@author: lavig
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hfpy = pd.read_csv('heart_failure_clinical_records_dataset.csv')

print(hfpy)


# EDA 


print(hfpy.head())

print(hfpy.dtypes)

# scatterplots of various features

plt.plot(hfpy.creatinine_phosphokinase)
plt.clf()
plt.scatter(hfpy.platelets, hfpy.creatinine_phosphokinase)
plt.show()

plt.scatter(hfpy.serum_sodium, hfpy.creatinine_phosphokinase)
plt.show()

plt.scatter(hfpy.serum_sodium, hfpy.serum_creatinine)

# chi-squared test to test for association 