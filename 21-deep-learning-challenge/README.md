# Deep Learning Challenge

## Overview
The nonprofit foundation Alphabet Soup wants a tool that can help it select the applicants for funding with the best chance of success in their ventures. With your knowledge of machine learning and neural networks, you’ll use the features in the provided dataset to create a binary classifier that can predict whether applicants will be successful if funded by Alphabet Soup.

From Alphabet Soup’s business team, you have received a CSV containing more than 34,000 organizations that have received funding from Alphabet Soup over the years. Within this dataset are a number of columns that capture metadata about each organization, such as:
 * `EIN` and `NAME`—Identification columns
 * `APPLICATION_TYPE`—Alphabet Soup application type
 * `AFFILIATION`—Affiliated sector of industry
 * `CLASSIFICATION`—Government organization classification
 * `USE_CASE`—Use case for funding
 * `ORGANIZATION`—Organization type
 * `STATUS`—Active status
 * `INCOME_AMT`—Income classification
 * `SPECIAL_CONSIDERATIONS`—Special considerations for application
 * `ASK_AMT`—Funding amount requested
 * `IS_SUCCESSFUL`—Was the money used effectively

## Methods
### Data Preprocessing
Given the nature of the data, we would like our model to be trained to generalize and predict if a business will be sucessful based on features of the business applying for the grant. Features like EIN and NAME will not contribute to our model and are removed from the featureset. First, categorical features are binned based on count, such as `APPLICATION_TYPE` and `CLASSIFICATION`. Since our labels `IS_SUCESSFUL` is already binary encoded, The features were then One-Hot-Encoded for our learning model, then split into their respective training and validaiton sets. Finally, the validation and training sets normalized using the StandardScaler class from sklearn.

### Model building
### Model 1: Feed Forward
This model's architecture follows a feed forward model with Adam as its optimizer. Given the data's simplicity, I chose to start the model with two hidden layers (8 and 4) with relu as its activation function. Since our model seeks to predict a binary classifier (is or is not successful), its output neuron is 1 with a sigmoid acivation function. Totaling 401 params. This model reached optimal performance after 250 epochs.
    
### Model 1.1: Feed forward with dropout
In this set, the cuttoff for `APPLICATION_TYPE` was increased from 150 to 500. In this model, I increased the number of neurons to 12-8 with 50% dropout, hoping the model learns to generalize better. I also increased batch size to 64 and added an early stopping function. I avoided adding a third layer as it's shown to lead to more unstable learning. This totaled to 641 params. This model reached optimal performance at about epoch 80.

### Model 1.2: Feed forward with CountVectorizer
In this set, the cuttoff for `APPLICATION_TYPE` was kept at 150. I also used CountVectorizer from sklearn to process `NAME` into a matrix, adding an additional **13513** features to the training set. This time, my first model used 16-10-8 hidden layers with 50% dropout. This model was prone to overfitting, thus modified the hidden layers 32-16-8 with a dropout of 90%, 50% and 50% respectively to penalize the learning rate with a total of 434529 params. This model reached optimal performance at about epoch 38.

### Model 1.2b: Feed forward with CountVectorizer and HPT
Building off of model 1.2's approach, HPT was deployed to improve model performance and parameters.
    
## Results
#### Model 1: Feed Forward
![FNN-8-4](https://github.com/anderoos/deep-learning-challenge/blob/main/Images/model_1_metrics/feed_forward_model1_8_4.png)
    The loss/accuracy curve shows that our model performs well. Our loss function appears to converge and our validation accuracy is higher than our training accuracy, indicating that our model generalizes well. 
``` 
215/215 - 0s - loss: 0.5418 - accuracy: 0.7402 - 85ms/epoch - 393us/step
    Loss: 0.541832447052002, Accuracy: 0.7401896715164185
```
    
#### Model 1.1: Feed forward with dropout
![FNN-12-8-dropout](https://github.com/anderoos/deep-learning-challenge/blob/main/Images/model_1_1_metrics/fnn-optimized-16do0-10do08_b64.png)
    This model shows better performance despite the 1.5% loss in accuracy. 
```
215/215 - 0s - loss: 0.5587 - accuracy: 0.7257 - 83ms/epoch - 385us/step
    Loss: 0.5587286353111267, Accuracy: 0.7257476449012756
``` 

#### Model 1.2: Feed forward with CountVectorizer
![FNN-32-16-8-NLP](https://github.com/anderoos/deep-learning-challenge/blob/main/Images/model_1_2_nlp_metrics/fnn-optimized-32do90-16do508do50_b64.png)
       This model yields a better accuracy score. Though overall, the performance of this model is lower than 1.1, This model's accuracy improved by 8%, 7.5% higher than the target 75%.
       
```
108/108 - 0s - loss: 0.4895 - accuracy: 0.8253 - 83ms/epoch - 767us/step
    Loss: 0.48946934938430786, Accuracy: 0.8252625465393066
```

#### Model 1.2b: Feed forward with CountVectorizer and HPT
![FNN-with-HPT](https://github.com/anderoos/deep-learning-challenge/blob/main/Images/model_1_2_nlp_metrics/fnn-optimized-hpt.png)
    This model yields a slightly improved accuracy and significantly improved performance over 1.2 when implementing Hyperparameter tuning from the Keras-Tuner library. This model's validation accuracy is at 82.96%, 0.04% higher than the previous of model 1.2. Additionally, model shows more stable learning and shows improved performance-- reaching ideal accuracy at just 2 epochs compared to 40 in the previous model.

```
108/108 - 0s - loss: 0.4040 - accuracy: 0.8296 - 106ms/epoch - 984us/step
    Loss: 0.4039914906024933, Accuracy: 0.8296383023262024
```
       
## Summary

Model 1.2b achieved an accuracy score of 82.9% with a loss ratio of 0.40. Using a combination of sigmoid and relu activation functions, baseline accuracy was established at 74%. Despite this large dataset, additional features such as `NAME` improved model accuracy, suggesting branding/marketing may play a role in the success of the business.

## Limitations
Model accuracy and preformance can be improved with exploring different base models and architectures. 

