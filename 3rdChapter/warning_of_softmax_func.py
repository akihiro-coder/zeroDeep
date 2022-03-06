import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([[1010, 1000, 990]])
b = np.exp(a) / np.sum(np.exp(a))
print(b)


# calculate using maximum value of array
c = np.max(a)
d = a - c
e = np.exp(d) / np.sum(np.exp(d))
print(e)
