library(readr)
library(tidyverse)
library(ggplot2)
library(modelr)

heart <- read_csv('heart_failure_clinical_records_dataset.csv')

print(head(heart))


#EDA pt. 1 for heart dataset: descriptive statistics
View(summary(heart))
print(mean(heart$age))
print(IQR(heart$age))
print(min(heart$age))


#variance calculation

View(var(heart))

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

ss_hist <- ggplot(heart, aes(heart$serum_sodium)) + geom_histogram() + ggtitle("Serum Sodium Histogram") + labs(x='Serum Sodium')
ss_hist

ss_quant_25 <- quantile(heart$serum_sodium, 0.25)
print(ss_quant_25)
ss_quant_50 <- quantile(heart$serum_sodium, 0.50)
print(ss_quant_50)
ss_quant_75 <- quantile(heart$serum_sodium, 0.75)
print(ss_quant_75)


#Generating a Random Sample of serum sodium values from the heart dataset

ss_sample<- sample(heart$serum_sodium, 25)
print(ss_sample)

#Based on the size of the dataset, is it important to consider how many groups to divide the random sample sets into?

ss_sample_hist <- hist(ss_sample)
ss_sample_hist


cp_p <- ggplot(heart, aes(heart$creatinine_phosphokinase, heart$platelets)) + geom_point()

cp_p


#generate barcharts for categorical variables

heights <- tapply(heart$creatinine_phosphokinase, heart$anaemia, mean)
#heights <- as.data.frame(heights)

barplot(heights, main=("CP (mean) vs anaemia status"), names.arg=c("Not Anaemic", "Anaemic"), col=c("red",'maroon'))

# Function to set numbers with marks and without scientific notation
marks_no_sci <- function(x) format(x, big.mark = ",", decimal.mark = ".", scientific = FALSE)

labels <- c("Not Anaemic", "Anaemic")
cp_anaemia <- ggplot(heart, aes(y=heart$creatinine_phosphokinase, x=heart$anaemia), mean()) + geom_bar(stat="identity", fill = "maroon") + labs(x="Anaemia Status", y="Creatinine Phosphokinase") + ggtitle("CP (mean) vs Anaemia Status") + scale_x_discrete(label=labels) + scale_y_continuous(labels = marks_no_sci) 
cp_anaemia

heights_1 <- tapply(heart$platelets, heart$diabetes, mean)
barplot(heights_1, main=("Platelet Level in Diabetes Status"), names.arg=c("Not Diabetic", "Diabetic"), col=c("darkgreen", "orange"))

#evaluate if there is a significant difference in platelet levels between patients with diabetes and without diabetes. 


##evaluate if there is a significant difference in creatinine phosphokinase and anaemia. 

#First I will subset the data into anaemic and non-anaemic patients.

non_anaemic <- heart%>%filter(anaemia ==FALSE)
View(non_anaemic)

non_anaemic_cp <- non_anaemic$creatinine_phosphokinase
View(non_anaemic_cp)
anaemic <- heart%>%filter(anaemia ==TRUE)
View(anaemic)

anaemic_cp <- anaemic$creatinine_phosphokinase
View(anaemic_cp)




#calculate the z-scores (normalize) the data for the cp in the non-anaemic and anaemic subsets

scaled_nacp <- scale(non_anaemic$creatinine_phosphokinase)
print(scaled_nacp)


scaled_acp <- scale(anaemic$creatinine_phosphokinase)
print(scaled_acp)

#generate random samples from the populations

non_a_sample <- sample(scaled_nacp,50)
hist(non_a_sample)


a_sample <- sample(scaled_acp,50)
hist(a_sample)

#test the mean of the samples with a t-Test


t.test(anaemic_cp,mu=95)

t.test(non_anaemic_cp, mu=95)



heart_count <- heart%>%group_by(anaemia)%>%summarize(count=n())
print(heart_count)

cp_na <- non_anaemic$creatinine_phosphokinase
print(cp_na)
print(summary(cp_na))

cp_a <- anaemic$creatinine_phosphokinase
print(cp_a)
print(summary(cp_a))

