import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
print(data.values.shape)

m, n = data.values.shape

X = data.values[:, 0:n-1]
X = np.insert(X, 0, 1, axis=1)
y = data.values[:, n-1:n]

for i in range(m):
    if (y[i,0] == 0):
        y[i,0] = -1
# plt.scatter(X[:,1],
#             X[:,2],
#             s=50)

# plt.title(title)
# plt.legend()
# plt.grid()
# plt.show()


def h_x(X, w):
    return np.sign(np.dot(X, w))


def has_converged(X, y, w):
    return np.array_equal(h_x(X, w), y)

def perceptron(X, y, w, loop):
    d = X.shape[0]
    N = X.shape[1]
    print("xi = ",d)
    print("yi = ",N)
    for iters in range(loop):
        for i in range(d):
            xi = X[i, :].reshape(1, N)
            yi = y[i, 0:1]
            sign = h_x(xi, w)
            if sign[0] != yi:  
                m = yi*xi
                w = w + m.T
        if has_converged(X, y, w):
            break
    return w

w = np.random.randn(n, 1)
print(w)
loop = 1000

w = perceptron(X, y, w, loop)

print(w)

print(h_x([1.0, 30.28671076822607,43.89499752400101], w))
