import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('logicsticdata.csv')
print(data.values);
true_x=[]
true_y = []
false_x=[]
false_y = []
for item in data.values:
    if item[2]==1.:
        true_x.append(item[0])
        true_y.append(item[1])
    else:
        false_x.append(item[0])
        false_y.append(item[1])

plt.scatter(true_x,true_y,marker = 'o',c='b')
plt.scatter(false_x,false_y,marker = 's',c='r')

plt.show()

# def sigmoid(z):
#     return 1.0 /(1+np.exp(-z))
# def phan_chia(p):
#     if  p>=0.5:
#          return 1
#     else:
#         return 0;
# def predict(feature,weights):
#     z= np.dot(feature,weights)
#     return sigmoid(z)
# def cost_function(feature, labels,weight) : 
#     n = len(labels)
#     predictions = predict(feature,weights)
#     cost_class1 = -labels*np.log(predictions)
#     cost_class2 = -(1-labels)*np.log(1-predictions)
#     cost = cost_class1+cost_class2
#     return cost.sum()/n

# def update_weight(feature, labels,weight,learning_rate):


# df = data.values

# m, n = data.values.shape

# X = data.values[:, 0:n-1]
# X = np.insert(X, 0, values=1, axis=1)
# y = data.values[:, n-1:n]

# def sigmoid(x):
#     return 1.0 / (1.0 + np.exp(-x))

# def compute_cost(X, y, w):
#     m = len(y)
#     z = sigmoid(np.dot(X, w))
#     J = np.sum(y * np.log(z) + (1 - y) * np.log(1 - z)) / m
#     return J

# def gradient_desc(X, y, w, alpha, loop):
#     m = len(y)
#     for i in range(loop):
#         w = w - alpha * np.dot(X.T, sigmoid(np.dot(X, w)) - y) / m
#         print(compute_cost(X, y, w))
#         mix_id = np.random.permutation(m)
#         X = X[mix_id]
#         y = y[mix_id]
#     return w


# w = np.random.randn(n, 1)
# loop = 1000
# alpha = 0.0001

# w = gradient_desc(X, y, w, alpha, loop)

# print(w)
