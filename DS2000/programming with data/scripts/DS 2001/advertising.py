"""
    DS2001 Week 11
    solution

"""

import matplotlib.pyplot as plt
# We use the LinearRegression class defined in the sklearn library.
from sklearn.linear_model import LinearRegression


def read_data(filename):
    ''' name: read_data
        input: filename (string)
        returns: header is a list
                 ad_data is list of lists
    '''
    ad_data = []
    file = open(filename, encoding="utf8")
    header = file.readline().strip().split(",")
    for row in file:
        pieces = row.strip().split(",")
        ad_data.append(pieces)
    
    return header, ad_data



def get_y(colname, header, data):
    ''' name: get_y
        input: colname (a string), header (list), data (list of lists)
        returns: y is a list of floats
    '''
    y_index = header.index(colname)
    y = []
    for row in data:
        y.append(float(row[y_index]))
    return y



def get_X(colnames, header, data):
    ''' name: get_X
        input: colnames (list of strings), header (list), data (list of lists)
        returns: X is a list of lists
    '''
    X = []
    for row in data:
        small_list = []
        for colname in colnames:
            col_index = header.index(colname)
            small_list.append(float(row[col_index]))
        X.append(small_list)
    return X
    
    

def main():
   
    header, ad_data = read_data("advertising.csv")
    
    # Create the y and X variables
    y = get_y("Daily Time Spent on Site", header, ad_data)
    X = get_X(["Age"], header, ad_data)
    
    # We use the LinearRegression object defined in the sklearn library.
    lr = LinearRegression()
    # Training Linear Regression
    model = lr.fit(X, y)
    print("Coefficients: ",  model.coef_)  # interpretation?

    # in-sample prediction  (see the comment below for out-of-sample prediction)
    insample_pred = model.predict(X)
    
    # Plot outputs
    plt.scatter(X, y, color="black")
    plt.plot(X, insample_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.xlabel("Age")
    plt.ylabel("Daily Time Spent on Site")
        
    
    # Bonus
    
    ''' 1. Important Notes about Prediction'''
    
    ''' In a typical prediction task, the goal is to train a model that can make 
    accurate predictions of an outcome variable of interest e.g., TimeSpent. 
    Machine learning models are very good at finding patterns in a data set. 
    However, the data set that we use for training an model can be quite 
    different from other data sets that we might encounter in the future. 
    Therefore, it is helpful to evaluate how well our model performs on an 
    'unseen' data set because it can give us a sense of our model performance 
    when used to predict future, unseen data.
    
    To achieve this, the most common approach is to randomly split our dataset 
    into a training set and a test data. We will only use the training set to 
    train our model. And we will then use the trained model to predict the 
    outcome variable in the test set. The model performance on the test set 
    provides an objective estimate of how well our model performs on future 
    unseen data. Note that if the data is a time-series data (e.g. stock prices), 
    however, we will use earlier data for training and later data for test. 
    
    In other words, when we train the model (e.g., linear regression), we 
    should only use the training set; when we evaluate the model performance 
    we should only use the test set.
    
    The sklearn package allows us to randomly split the data into training and
    test very easily. Below, we call the train_test_split function, which is
    part of sklearn package's model_selection utility. The way this function
    works is that we will provide the predictors (X) and the outcome (Y), 
    a random_state that ensures the random split can be replicated, and the 
    proportion of data that we want to designate as test set 
    (e.g., 0.33 in this case). '''
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, 
                                                        test_size=.33)
    model2 = lr.fit(X_train, y_train)
    print("Coefficients: ",  model2.coef_)

    # out-of-sample prediction
    outofsample_pred = model2.predict(X_test)
    
    # Plot outputs
    plt.figure()
    plt.scatter(X_test, y_test, color="black")
    plt.plot(X_test, outofsample_pred, color="blue", linewidth=3)
    plt.xlabel("Age")
    plt.ylabel("Daily Time Spent on Site")
    
    
    
    ''' 2. Model Evaluation'''
    
    ''' Most of the times we want to use an objective metric to measure the 
    prediction performance. One such measures, perhaps the most commonly used 
    one, is called the root mean squared error (RMSE). What it does is that it 
    takes the difference between the actual and prediction for each observation 
    (this is the prediction error for each observation), squares it, then takes
    the mean of the squared difference across all observations. Then it finally
    takes the square root of that mean squared difference.

    Since the RMSE represents some sort of error, the smaller the better.

    This sounds quite complicated, but to compute this metric we can just call
    a pre-defined mean squared error in sklearn and take the square root of it:
    '''
    
    from sklearn.metrics import mean_squared_error
    # compute the RMSE: this represents the average error for a given observation
    print ('RMSE is: \n', mean_squared_error(y_test, outofsample_pred, squared=False))
    
    
    
    ''' 3. Using Pandas'''
    
    import pandas as pd
    data = pd.read_csv("advertising.csv")
    y_p = data["Daily Time Spent on Site"]
    X_p = data[["Age"]]
    
    # The rest is the same
    lr = LinearRegression()
    model_p = lr.fit(X_p, y_p)
    print("Coefficients: ",  model_p.coef_)
    
    
main()









