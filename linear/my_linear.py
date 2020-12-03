from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('F:\TÀI LIỆU KỲ 7\TRÍ TUỆ NHÂN TẠO\linear regresson\\advertising.csv')
print(data)

X =np.array([data.values[:,0]]).T

y=  np.array([data.values[:,3]]).T

# # Visualize data 

plt.plot(X, y, 'ro')
plt.axis([0, 300, 0, 30])
plt.xlabel('TV (h)')
plt.ylabel('Sales (produces)')
plt.show()

# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)


print('w = ', w)
# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(20,280, 20)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([0, 300, 0, 30])
plt.xlabel('TV(h)')
plt.ylabel('Sales (produces)')
plt.show()

