#!/usr/bin/env python
# coding: utf-8

# # DS 2500 HW 6

# # Part 1.1: Car weight & power (15 points)

# In[1]:


import seaborn as sns

df_car = sns.load_dataset('mpg')
df_car.head()


# In[2]:


from sklearn.linear_model import LinearRegression
import pandas as pd

# obtain, reshape data
df_car = df_car.dropna()
x = df_car.loc[:, "horsepower"].values
y = df_car.loc[:, "weight"].values

x = x.reshape((-1, 1))
y = y.reshape((-1, 1))

# intialize regression model, fit, predict
reg = LinearRegression()
reg.fit(x, y)
y_pred = reg.predict(x)


# In[3]:


import matplotlib.pyplot as plt

sns.set(font = "serif", font_scale = 1.4)

# plot data
plt.scatter(x, y, label = "observed", color = "k")
plt.plot(x, y_pred, label = "regression model", color = "g", alpha = .7)
plt.title("car weight and power")

# plot labels
plt.xlabel("horsepower")
plt.ylabel("weight")
plt.legend()
plt.gcf().set_size_inches(10, 7)


# # Part 1.2: Interpretting Regressions (20 points, 10 each)
# 
# 1. Compute and interpret a quantification of how good the model in part 1.1 is.  How helpful is horsepower in explaining differences in the weight of a car for this particular set of cars?
# 1. One car has 50 more horsepower than another.  Using the model from part 1.1, whats our best guess as to how much heavier the more powerful car is?

# In[4]:


from sklearn.metrics import mean_squared_error, r2_score

print(f"mse = {mean_squared_error(y, y_pred)}, r2 = {r2_score(y, y_pred)}")


# a high value for mean squared error shows that model's line is far from the observations. similarly, the r2 coefficient shows that **horsepower accounts for around 75% of the variance in the weight of cars.** while there's a positive correlation, the mse value indicates the model doesn't truly fit the data.

# looking at the visualization above, an increase in 50 horsepower is correlated with an increase in weight of just under 1000 lbs.

# # Part 2: Polynomial Fitting (35 points)

# In[16]:


import pickle

# loads arrays x and y from file
with open('xy_hw6.p', 'rb') as f:
    x, y = pickle.load(f)

plt.scatter(x, y);


# In[21]:


from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def fit_plot_poly(x, y, degree):
    """ fits and plots a polynomial of given degree
    
    Args:
        x (np.array): (n_samples, 1) array of x inputs
        y (np.array): (n_sample, 1) array of target values
        degree (int): max degree of polynomial
    """
    # project x to polynomial
    poly_project = PolynomialFeatures(degree = degree)
    x_poly = poly_project.fit_transform(x)
    
    # fit via linear regression
    reg = LinearRegression(fit_intercept = False)
    reg.fit(x_poly, y)
    
    x_fine = np.linspace(x.min(), x.max(), 101).reshape(-1, 1)
    x_fine_poly = poly_project.fit_transform(x_fine)
    y_pred_fine = reg.predict(x_fine_poly)
    
    # compute r2
    y_pred = reg.predict(x_poly)
    r2 = r2_score(y_true=y, y_pred=y_pred)
    
    # plot polynomial / observations
    plt.plot(x_fine, y_pred_fine, label = f"r2 = {r2:.9f}", color="k", linewidth = 2)
    plt.scatter(x, y, label = "observed", color = "r", alpha = .8)
    plt.legend()  
    
    print(f"poly. coefficients: {reg.coef_}")


# In[22]:


fit_plot_poly(x, y, 3)


# **y = .89 - 1.08x + 2.11x^2 - .52x^3**
# 
# three seems to be the best choice for the polynomial degree - with degree two, the model is understated. with higher degrees, the model fits similarly to degree three making it the smallest choice with the best fit.

# # Part 3: Clustering States by Driving Habits  (15 points)

# In[8]:


df_car = sns.load_dataset('car_crashes')
df_car.head()


# In[9]:


from sklearn.cluster import KMeans

# extract features
x_feat_list =  ["speeding", "alcohol", "not_distracted", "no_previous", "ins_premium", "ins_losses"]  
x = df_car.loc[:, x_feat_list].values

n_clusters = 3

mean_dict = dict()
for n_clusters in range(3, 8):
    # fit kmeans
    kmeans = KMeans(n_clusters = n_clusters)
    kmeans.fit(x)
    y = kmeans.predict(x)    
        
    # compute & store mean distance
    mean_d = -kmeans.score(x)
    mean_dict[n_clusters] = mean_d

    # plot clustering
    plt.figure()
    sns.scatterplot(x=x[:, 0], y=x[:, 1], s=100, hue=y, palette='Set2')
    plt.suptitle(f'{n_clusters} clusters with mean distance: {mean_d:.0f}')
    plt.gca().get_legend().remove()
    plt.gcf().set_size_inches(6, 3)


# In[10]:


plt.plot(mean_dict.keys(), mean_dict.values())

plt.xlabel('number of clusters')
plt.ylabel('mean distance to centroid')


# the optimal number of clusters, according to the visualization, will be six. this is where the marginal gain drops and hence where the "elbow" appears.

# # Part 4: Iris PCA (15 points)

# In[11]:


df_iris = sns.load_dataset('iris')

df_iris.head()


# In[12]:


from sklearn.decomposition import PCA

# obtain data
df_iris.dropna(inplace = True)
x_feat = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
x = df_iris.loc[:, x_feat].values

# compress
pca = PCA(whiten = True)
x_compress = pca.fit_transform(x)

# append to dataframe
df_iris["pca0"] = x_compress[:, 0]
df_iris["pca1"] = x_compress[:, 1]


# In[13]:


import plotly.express as px

fig = px.scatter(df_iris, x = "pca0", y = "pca1", hover_data = df_iris.columns, color = "species")
fig.show()

