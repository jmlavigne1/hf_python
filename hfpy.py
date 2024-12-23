# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 06:45:47 2024

@author: lavig
"""

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hfpy = pd.read_csv('heart_failure_clinical_records_dataset.csv')

print(hfpy)


# EDA

print(hfpy.head())

print(hfpy.dtypes)

print(hfpy.describe())


print(hfpy.info())
# This reveals that there are no missing data in the dataset.


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


# creating scatterplots individually is helpful, however, it is helpful to produce a pair plot to visualize the total dataset

# pair plot for the heart failure dataset


sns.pairplot(hfpy)

# a correlation heat map is also a useful tool

# correlation heat map

corr = hfpy.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()


# testing for an association: a two sample T-Test
# one binary categorical variable and one quantitative variable
# based upon the correlation heatmap depicted in the previous section, it would be worth investigating the association between serum creatinine(quantitative value) and the death event (binary categorical value)

hfpy_DE = hfpy["DEATH_EVENT"]
print(hfpy_DE)
# I chose to print the hfpy_DE to make sure that the DEATH_EVENT column was a true binary categorical variable.


# Seperate out data based on whether the death occurred or not

hfpy_no_death = hfpy.serum_creatinine[hfpy.DEATH_EVENT == 0]
hfpy_death = hfpy.serum_creatinine[hfpy.DEATH_EVENT == 1]

ttest, pval = ttest_ind(hfpy_no_death, hfpy_death)
print(pval)

# the pval is much lower than the 0.05 threshold, therefore for the purpose of this demostration I will determine different to be statistically significantly different between death event and no death event for serum creatinine.

plt.hist(hfpy_death, alpha=0.4, label="death occurred")
plt.hist(hfpy_no_death, alpha=0.8, label="No death occurred")
plt.legend()
plt.show()


# testing for an association: ANOVA + Tukey
# one non-binary categorical variable and one quantitative variable. I will break the age feature up into 3 categories to produce a non-binary category in the dataset.

hfpy_age_min = hfpy['age'].min()
print(hfpy_age_min)

hfpy_age_max = hfpy['age'].max()
print(hfpy_age_max)

# Age ranges from 40 yo to 95 yo. Age column will be broken into 40 yo - 56 yo, 57 yo - 73 yo, and 74 yo - 95 yo

age_young = hfpy[hfpy['age'] < 56]
age_med = hfpy[(hfpy['age'] >= 57) & (hfpy['age'] <= 73)]
age_old = hfpy[hfpy['age'] >= 74]

fig, ax = plt.subplots()
labels = ["Young 45 - 56 years", "Middle 57 - 73 years", "Old 74 - 95 years"]
ax.boxplot([age_young['serum_creatinine'],
           age_med['serum_creatinine'], age_old['serum_creatinine']])
plt.xlabel('Age Groups')
plt.ylabel('Serum Creatinine Values')
plt.title('Age Groups (years) vs. Serum Creatinine')
ax.legend(loc="upper left")
ax.get_xaxis().set_visible(False)
plt.show()



plt.hist(age_med["serum_creatinine"], alpha=0.8, normed=True)
plt.show()
plt.clf()

plt.hist(age_young["serum_creatinine"], alpha=0.8, normed=True)
plt.show()
plt.clf()

plt.hist(age_old["serum_creatinine"], alpha=0.8, normed=True)
plt.show()
plt.clf()

##I don't think this is normally distributed


# perform ANOVA with the three age groups and serum creatinine


f_oneway(age_young, age_med, age_old)


# perform Tukey test to determine which of the three groups

tukey = pairwise_tukeyhsd(hfpy.age, hfpy.serum_creatinine, alpha=0.05)
print(tukey)


# testing for an association: chi-squared test
# two categorical variables

table = pd.crosstab(hfpy.age, hfpy.diabetes)

from scipy.stats import chi2_contingency
chi2, pval, dof,expected = chi2_contingency(table)
print(pval)


#the two variables are not associated, therefore, it is not statistically significant.

