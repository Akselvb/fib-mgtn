# Project 2: Calibration of an air pollution sensor in Wireles Sensor Network

## Abstract

This report aims to show the results obtained in the second project of the MGTN subject. The project's main objective is to learn how to calibrate an air pollution sensor in a Wireless Sensor Network.

Given the fact that the calibration architecture is collocated, the authors have used a multiple linear regression with off-line training data used to predict new values that could be used to calibrate new sensors. Data generated has been compared against test data to check whether the model used is capable of making accurate predictions.

Additionally, a model has been generated with Support Vector Regression in order to learn about both solutions.

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

### Support Vector Machines

Support Vector Machines are normally used for **classification problems**, dividing data into 2 classes. To do that, SVM projects the data into higher dimensions and then figures out **the best hyperplane** which separates the data into both classes using **kernels**.

![SVM](https://i.imgur.com/WuxyO.png)

In other words, it finds the particular hyperplane which separates these two classes with **minimum error** while also making sure that the perpendicular distance between the two closest points from either of these two classes is maximized.

![SVR](https://upload.wikimedia.org/wikipedia/commons/f/fe/Kernel_Machine.svg)

### Support Vector Regression

Super Vector Machines can be adapted to be used for **regression problems (SVR)** maintaining the main features that characterize the algorithm but using a tolerated error. This tolerated margin (**epsilon**) is set in approximation to the SVM, so the higher the epsilon the more tolerated error. The main idea is the same: minimize the error, individualizing the hyperplane which maximizes the margin but keeping in mind that some part of the error is tolerated:

![wikiSVR](https://upload.wikimedia.org/wikipedia/commons/7/7a/Svr_epsilons_demo.svg)

For Non-linear SVR, kernel functions are used to transform the data into a higher dimensional feature space to make it possible to perform the linear separation.

![SVRnl](http://www.saedsayad.com/images/SVR_5.png)

## 2.4: Project Realization (Practical Part II)

In this part the team used support vector machines regression for the calibration of the sensor. The process was repeated and a SVM with epsilon=0.1 was used (default value). The following charts show that the model produced data that fits the training and test data even better than with a multiple linear regression:

![svm_training_predicted_reference](plots/svm_training_predicted_reference.png)
![svm_test_predicted_reference](plots/svm_test_predicted_reference.png)
![svm_all_predicted_reference](plots/svm_all_predicted_reference.png)
