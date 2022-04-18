import numpy as np


def cross_entropy_error(y, t):
    delta = 10**(-7)
    return -np.sum(t * np.log(y+delta))


# ground truth 
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
t = np.array(t)
# predict result
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
y = np.array(y)

a = cross_entropy_error(y, t)
print(a)
