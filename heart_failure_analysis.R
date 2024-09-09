library(readr)
library(tidyverse)
library(ggplot2)

heart <- read_csv('heart_failure_clinical_records_dataset.csv')

print(head(heart))


#EDA pt. 1 for heart dataset: descriptive statistics
View(summary(heart))



