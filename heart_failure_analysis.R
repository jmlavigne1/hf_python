library(readr)
library(tidyverse)
library(ggplot2)

heart <- read_csv('heart_failure_clinical_records_dataset.csv')

print(head(heart))


#EDA pt. 1 for heart dataset: descriptive statistics
View(summary(heart))
print(mean(heart$age))
print(IQR(heart$age))
print(min(heart$age))


#EDA pt. 2 for heart dataset: dataset visualizations 

plate_vs_cp <- ggplot(heart, aes(heart$platelets, heart$creatinine_phosphokinase)) + geom_point() + ggtitle("Platelets vs. Creatinine phosphokinase Scatterplot") + labs( x="Platelets", y="Creatinine Phosphokinase")
plate_vs_cp


age_hist <- ggplot(heart, aes(heart$age)) + geom_histogram() + ggplot("Age Histogram")
age_hist

ef_hist <- ggplot(heart, aes(heart$ejection_fraction)) + geom_histogram() + ggtitle("Ejection Fraction Histogram")
ef_hist

dev.off()
plot(rnorm(50), rnorm(50))

smoking_SC_box <- ggplot(heart, aes(y=heart$serum_creatinine, x=heart$smoking == 1)) + geom_boxplot() + ggtitle("Smoking vs. Serum Creatinine Boxplot") + labs( x="smoking status", y="Serum Creatinine")
smoking_SC_box


smoking_plates_box <- ggplot(heart, aes(y=heart$platelets, x=heart$smoking == 1)) + geom_boxplot() + ggtitle("Smoking vs. Platelets Boxplot") + labs( x="smoking status", y="Platelets")
smoking_plates_box

sc_hist <- ggplot(heart, aes(heart$serum_creatinine)) + geom_histogram() +ggtitle("Serum Creatinine Histogram")
sc_hist




