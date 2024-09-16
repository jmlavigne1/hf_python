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


##EDA 


print(hfpy.head())

print(hfpy.dtypes)

print(hfpy.describe())


print(hfpy.info())
#This reveals that there are no missing data in the dataset.





# scatterplots of various features

plt.plot(hfpy.creatinine_phosphokinase)
plt.clf()
plt.scatter(hfpy.platelets, hfpy.creatinine_phosphokinase)
plt.show()

plt.scatter(hfpy.serum_sodium, hfpy.creatinine_phosphokinase)
plt.show()
plt.clf()

plt.scatter(hfpy.serum_sodium, hfpy.serum_creatinine)
plt.show()
plt.clf()

plt.scatter(hfpy.creatinine_phosphokinase, hfpy.serum_creatinine)
plt.show()
plt.clf()
plt.scatter(hfpy.serum_creatinine, hfpy.creatinine_phosphokinase)
plt.show()


##creating scatterplots individually is helpful, however, it is helpful to produce a pair plot to visualize the total dataset

#pair plot for the heart failure dataset

import seaborn as sns

sns.pairplot(hfpy)





## a correlation heat map is also a useful tool

#correlation heat map




##testing for an association: a two sample T-Test
#one binary categorical variable and one quantitative variable










##testing for an association: ANOVA + Tukey
#one non-binary categorical variable and one quantitative variable










##testing for an association: chi-squared test
#two categorical variables














