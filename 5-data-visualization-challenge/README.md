# CU-05-Data-Visualization-Challenge
## Description
In this fictional dataset, we are screening for potential treatment candidates for squamous cell carcinoma (SCC). We are given a dataset containing the most recent animal study in mice. 
In this dataset, researchers have identified 249 mice with SCC tumors and received treatment regimens. Over the course of 45 days, weight, tumor volume and metastatic sites were recorded in 5 day intervals. 
The purpose of this study is to compare the drug of interest Capomulin, against other treatment regimens.

## Approaches and Resources
This set was broken down into the following:
* Data preparation
* Summary statistics in long format
* Bar charts and Pie charts 
* Observing quartiles, outliers, and creating a box plot for such.
* Creating a line plot and scatter plot for drug of interest
* Calculating correlation and regression for drug of interest

## Conclusions
* Capomulin & Ramicane have the most observations.
* Study design has a near equal amount of male and female subjects.
* Capomulin & Ramicane is the most effective in reducing tumor volume in mouse models over a 45 day period.
* Capomulin is effective in reducing tumor volume when compared to mouse weight over a 45 day period.
* In the Capomulin cohort, there is a strong correlation between Mouse weight and final tumor volume, suggesting that tumor size correlates with the weight of the mouse, pvalues shows that it is statistically significant.

![alt text](https://github.com/anderoos/CU-5-data-visualization-challenge/blob/main/Pymaceuticals/Images/total_timepoints.png)
![alt text](https://github.com/anderoos/CU-5-data-visualization-challenge/blob/main/Pymaceuticals/Images/sex-distribution.png)
![alt text](https://github.com/anderoos/CU-5-data-visualization-challenge/blob/main/Pymaceuticals/Images/final-tumor-vols.png)
![alt text](https://github.com/anderoos/CU-5-data-visualization-challenge/blob/main/Pymaceuticals/Images/b128-progression.png)
![alt text](https://github.com/anderoos/CU-5-data-visualization-challenge/blob/main/Pymaceuticals/Images/Capomulin-cohort-progression.png)
![alt text](https://github.com/anderoos/CU-5-data-visualization-challenge/blob/main/Pymaceuticals/Images/Capomulin-cohort-avg-endpoints-regression.png)

## Limitations and recommendations
- There is no control (untreated) sample. Depending on the mouse line they use, this type of SCC can regress without drug intervention.
- We can conclude that Capomulin is effective in reducing tumor volume in mice models over a 45 day period but demonstrates some level of drug resistance around the 35-40 day period when we see tumor volume increasing.
## Licensing 
This code has no license restrictions. Challenge materials are provided by the Columbia School of Engineering.