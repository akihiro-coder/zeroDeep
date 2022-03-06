import numpy as np


# 1D array
A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

# 2D array
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print("np.ndim(B):{}".format(np.ndim(B)))
print("B.shape:{}".format(B.shape))


C = np.array([[1, 2], [3, 4]])
D = np.array([[5, 6], [7, 8]])
E = np.dot(C, D)
print("dot of c and d:{}".format(E))


F = np.array([[1, 2, 3], [4, 5, 6]])
print("f shape:{}".format(F.shape))
G = np.array([[1, 2], [3, 4], [5, 6]])
print("g shape: {}".format(G.shape))
print("dot of f and g:{}".format(np.dot(F, G)))


# print("dot of b and g:{}".format(np.dot(B, G)))

H = np.array([1, 2, 3])
print("H shape:{}".format(H.shape))
print("shape of F matrix:{}".format(F.shape))
print("dot of f and h:{}".format(np.dot(F, H)))


