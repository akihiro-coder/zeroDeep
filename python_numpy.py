import numpy as np

x = np.array([1,2,3])
print(x)
print(type(x))



a = np.array([1.0,2.0, 3.0])
b = np.array([2.0, 4.0 ,6.0])
print("a = {}".format(a))
print("b = {}".format(b))
print(a + b)
print(a - b)
print(a * b)
print(a / b)


# 2-dimentions

A = np.array([[1,2], [3,4]])
print("########################")
print(A)
print(A.shape)
print(A.dtype)
B = np.array([[3, 0], [0, 6]])


print("A = {}".format(A))
print("B = {}".format(B))
print(A + B)
print(A - B)
print(A * B)
print(A / B)



print("########################")




C = np.array([[1, 2], [3, 4]])
D = np.array([10, 20])
print("C = {}".format(C))
print("D = {}".format(D))
print("print C + D :{}".format(C + D))



for row in C:
    print(row)

C = C.flatten()
print("C_flatten = {}".format(C))


print( C > 2 )

# trueに対応する要素を取り出す
# ブロードキャスト機能
print(C[C > 2])
