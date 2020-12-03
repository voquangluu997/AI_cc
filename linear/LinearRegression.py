
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataCsv = pd.read_csv("advertising.csv")
print(dataCsv)

X = dataCsv.values[:, 1]
y = dataCsv.values[:, 3]
# print(X)
# ham du doan theo gia tri duoc cung cap la new_x
def predict(new_x, weight, bias):
    return new_x*weight + bias

# ham tinh loi trung binh 
def compute_cost(X, y, weight, bias):
    n = len(X)
    sum_err = 0

    for i in range(n):
        sum_err += (y[i] - (X[i]*weight + bias))**2
    return sum_err/n

def update_weight(X, y, weight, bias, learning_rate):
    n = len(X)
    weight_diff = 0
    bias_diff = 0.0
    for i in range(n):
        # dao ham theo weight
        weight_diff += -2*X[i]*(y[i] - (weight*X[i] + bias))

#         # dao ham theo bias
        bias_diff += -2*(y[i] - (weight*X[i] + bias))

    weight -= (weight_diff/n)*learning_rate
    bias -= (bias_diff/n)*learning_rate

    return weight, bias


def train(X, y, weight, bias, learning_rate, iter):
    
    for i in range(iter):
        weight, bias = update_weight(X, y, weight, bias, learning_rate)
        cost = compute_cost(X, y, weight, bias)
        print(cost)
    
    return weight, bias




weight, bias = train(X, y, 0.001, 0.001, 0.001, 100)

print(weight)
print(bias)

predict_X = [np.min(X), np.max(X)]
predict_Y = [predict(predict_X[0], weight, bias), predict(predict_X[1], weight, bias)]


plt.scatter(X, y, marker="o",c="r")
plt.plot(predict_X, predict_Y)
plt.show()
