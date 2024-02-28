# Credit Risk Classification Report

## Overview of the Analysis

The goal of this analysis is to build a classification model using logistic regression algorithm to predict high risk lenders and healthy low risk lenders. This model was trained using historical peer to peer lending activity. This data contains loan information like loan size, interest rate, borrower income, debt, account and derogatory marks on credit.

## Methods
### Exploratory Analysis
Dataset provided contains 7 features: loan information like loan size, interest rate, borrower income, debt, account and derogatory marks on credit. Additionally, contains our labeled data 'loan_status' with a binary classifier: 1 for high risk and 0 for healthy or low risk. Balance of the labels were previewed using .value_counts() passing in the normalize parameter. It appears that 97% of loan applications are classified low risk, while 3% are classified as high-risk.

### Model building
In this model, logisitic regression was used as our primary classification algorithm. Due to the skewed nature of the dataset, the Random Oversampler algorithm from imblearn was used to balance the dataset.
Using scikit-learn, the dataset was split 80-20 into train and test set. Logisitic regression algorithm (LR) was then trained using the unsampled and post-sampled dataset. Validation was performed using the test set.
    The model was then validated and assessed using a series of metrics:
        * Accuracy for true value score
        * Precision for positive value score
        * Balanced Accuracy Score for true value score
        * Recall for true positive rate
        * F1 Score for harmonic mean for recall and precision
        * Reciever Operating Characteristic (ROC) for classification strength
    
## Results
* Machine Learning Model 1 with unsampled data:
  * Balanced Accuracy Score: 0.952
  * Accuracy Score: Not applicable
  * Precision Score: 0.860
  * Recall Score: 0.909
  * F1 Score: 0.884
  * ROC Area Under the Curve: 0.995
    
![ROC-curve](https://github.com/anderoos/credit-risk-classification/blob/main/Images/ROC_curve.png)

* Machine Learning Model 2 with sampled data:
  * Balanced Accuracy Score: 0.994
  * Accuracy Score: 0.994
  * Precision Score: 0.854
  * Recall Score: 0.994 
  * F1 Score: 0.919
  * ROC Area Under the Curve: 0.994
    
![ROC-curve-with-sampling](https://github.com/anderoos/credit-risk-classification/blob/main/Images/ROC_curve_w_ros.png)

  
## Summary

Both models display high classification power based on the ROC-AUC curve. Random oversampling algorithm was successful in improving classification prediction and yielded more favorable results when compared to classify imbalanced labels. In our second model when we employed random oversampling algorithm from imblearn (here called ros) we achieved balanced_accuracy_score and accuracy score of 99%. Although this model experienced a modest reduction in precision, this model overall improved recall and F1 by 9% and 3% respectively. Its worth noting lowered precision is probably acceptable within this context. As a bank attempting to assess the creditworthiness of borrowers, misidentifying high-risk borrowers is is more judicious than identifying low-risk borrowers to help mitigate lending risk.

## Limitations
Despite the near perfect accuracy of this model, This is just one classification model. Other classificaiton methods include support vector machines, gradient descent, random forests and so on. We can also deploy hyperparameter tuning to improve the performance of these models.
Additionally, the context of this training dataset is required to assess the performance of this model. For instance, financial records from 2008 may not be represenative of financial and lending data in 2024.
