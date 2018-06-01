# Project 2

Abstract/Intro

## 2.2: Project Realization (Practical Part I)

### Q1
The following plots shows the ozone as a function of time and the reference data as a function of time respectively.

![ozone_time](plots/ozone_time.png)
![reference_time](plots/reference_time.png)

We see that there is a significant resemblance between the two plots, however with some considerable differences.

### Q2
The attached file *calculations.Rmd* calculates the mean and standard deviation for each of the properties, and displays it in the output console.

### Q3
The following scatter-plot shows the linear dependence between the reference data and the sensor data.
![normalized_reference_ozone](plots/normalized_reference_ozone.png)

As we see, there is clearly a dependence amongst the two, but the error of the sensor contributes to spread the data.

### Q4
By performing multiple linear regression using the built-in method of RStudio, the following betas are obtained:

- **β<sub>0</sub>** ~ 0.00
- **β<sub>1</sub>** ~ 0.43
- **β<sub>2</sub>** ~ 0.67
- **β<sub>3</sub>** ~ 0.05

The obtained statistical properties yield:
- **R<sup>2</sup>**: 0.8813
- **RMSE**: 14.75

These values reveals that the linear regression is a good prediction of the actual data.

### Q5
When prediciting the test data, the obtained statistical properties yield:
- **R<sup>2</sup>**: 0.9143
- **RMSE**: 11.777

This is in fact an even better prediction for the test data compared to the training data.

### Q6
The following plots shows the predicted data in the same plot as the actual reference data. The black line represents the actual data, while the red line represents the predicted data.


**Training predicted vs. training reference data**
![training_predicted_reference](plots/training_predicted_reference.png)

**Test predicted vs. test reference data**
![test_predicted_reference](plots/test_predicted_reference.png)

**All predicted vs. all reference data**
![all_predicted_reference](plots/all_predicted_reference.png)

**Scatter-plot of predicted data vs reference data**
![scatter_predicted_reference](plots/scatter_predicted_reference.png)



## 2.3: Project Realization (Practical Part II)


## 2.4: Project Realization (Practical Part II)
![svm_training_predicted_reference](plots/svm_training_predicted_reference.png)
![svm_test_predicted_reference](plots/svm_test_predicted_reference.png)
![svm_all_predicted_reference](plots/svm_all_predicted_reference.png)
