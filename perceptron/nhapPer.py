import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
# print(data.values)

m, n = data.values.shape

X = data.values[:, 0:n-1]
X = np.insert(X, 0, 1, axis=1)
y = data.values[:, n-1:n]
print(X)
print(y)
# true_x=[]
# true_y = []
# false_x=[]
# false_y = []
# for item in data.values:
#     if item[2]==1.:
#         true_x.append(item[0])
#         true_y.append(item[1])
#     else:
#         false_x.append(item[0])
#         false_y.append(item[1])
# plt.scatter(true_x,true_y,marker = 'o',c='b')
# plt.scatter(false_x,false_y,marker = 's',c='r')
# plt.show()
# for i in range(m):
#     if (y[i,0] == 0):
#         y[i,0] = -1

def h_x(X, w):
    return np.sign(np.dot(X, w))

def has_converged(X, y, w):
    return np.array_equal(h_x(X, w), y)

def perceptron(X, y, w, loop):
    d = X.shape[0]
    N = X.shape[1]
    for iters in range(loop):
        for i in range(d):
            xi = X[i, :].reshape(1, N)
            yi = y[i, 0:1]
            print(xi)
            print(yi)
            sign = h_x(xi, w)
            if sign[0] != yi:  
                m = yi*xi
                w = w + m.T
        if has_converged(X, y, w):
            break
    return w

# plt.scatter(X,y,marker='o',c='r')
w = np.random.randn(n, 1)
# print(w)
loop = 10


w = perceptron(X, y, w, loop)

print(w)

# plt.plot(y0)
# plt.scatter(true_x,true_y,marker = 'o',c='b')
# plt.scatter(false_x,false_y,marker = 's',c='r')
# plt.show()

print(h_x([1.0, 4,3], w))

