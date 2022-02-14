# クラス 講座
class Man:
    def __init__(self, name):
        self.name = name #インスタンス変数の作成
        print('Initialized!')
    def hello(self):
        print('Hello ' + self.name + '!') # インスタンス変数へのアクセス
    def goodbye(self):
        print('GoodBye ' + self.name + '!')


man = Man('Ken')
man.hello()
man.goodbye()




# numpy 講座
import numpy as np
x = np.array([1., 2. ,3.])
print(x)

y = np.array([2., 4., 6.])
print('x+y{}'.format(x + y))
print('x-y{}'.format(x - y))
print('x*y{}'.format(x * y))
print('x/y{}'.format(x / y))
# 要素数が同じなので算術計算が出来る


print('x/2{}'.format(x / 2))
# numpy配列とスカラーの間でも計算が可能 ＝ ブロードキャスト



# 多次元配列
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)
# 多次元配列の算術計算
B = np.array([[3, 0],[0, 6]])
print('A + B{}'.format(A + B))
print('A * B{}'.format(A * B))
# 行列が同じ形状であれば計算可能
print('A * 10{}'.format(A * 10))# ブロードキャスト


# ブロードキャスト
C = np.array([10, 20])
print('A * C:{}'.format(A * C))



# 要素へのアクセス
X = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(X)
# 指定してアクセス
print("X[0]:{}".format(X[0]))
print("X[0][2]:{}".format(X[0][2]))

# for文でアクセス
for row in X:
    print(row)

X = X.flatten() # 一次元配列に変換
print(X)
print(X[np.array([0,2,4])])
print(X > 4)
# print(type(X > 4))
print(X[X > 4])



# matplotlib 講座
import matplotlib.pyplot as plt 
x = np.arange(0, 6, 0.1)
y = np.sin(X)
plt.plot(x, y)
plt.show()
