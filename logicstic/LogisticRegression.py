import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('logicsticdata.csv')
df = data.values

m, n = data.values.shape

X = data.values[:, 0:n-1]
X = np.insert(X, 0, values=1, axis=1)
y = data.values[:, n-1:n]

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def compute_cost(X, y, w):
    m = len(y)
    z = sigmoid(np.dot(X, w))
    J = np.sum(y * np.log(z) + (1 - y) * np.log(1 - z)) / m
    return J

def gradient_desc(X, y, w, alpha, loop):
    m = len(y)
    for i in range(loop):
        w = w - alpha * np.dot(X.T, sigmoid(np.dot(X, w)) - y) / m
        print(compute_cost(X, y, w))
        mix_id = np.random.permutation(m)
        X = X[mix_id]
        y = y[mix_id]
    return w

w = np.random.randn(n, 1)
loop = 1000
alpha = 0.0001
threshold = 0.5

w = gradient_desc(X, y, w, alpha, loop)

print(w)
# print('Evaluate:')



# for i in range(m):
#     pred_v = sigmoid(np.dot(X_test[i], w))[0]
#     if (pred_v > threshold):
#         pred_v = 1
#     else:
#         pred_v = 0
#     print('Predict:', pred_v, ' ---- result: ', y_test[i][0])