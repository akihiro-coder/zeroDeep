import numpy as np 

a = np.array([[1,2],[3,4]])
b = np.array([10,20])
print("a+b:{}".format(a + b))
print("a*b:{}".format(a * b))

c = np.array([[10,20], [10,20]])
print("a+c:{}".format(a + c))
print("a*c:{}".format(a * c))

# このように形状の異なる配列同士の演算を行うことが出来る 「ブロードキャスト機能」

print("###########################")

x = np.array([[1,2],[3,4],[5,6]])

print("x:{}".format(x))
print("各要素へアクセス")
print("x[0]:{}".format(x[0]))
print("x[0][1]:{}".format(x[0][1]))
print("x[0, 1]:{}".format(x[0, 1]))

print("各要素を並べる")
for row in x:
    print(row)

print("ある条件を満たす要素を取得")
y = x.flatten()
print("y:{}".format(y))
print("0,2,4番目の要素を取得")
z = y[np.array([0,2,4])]
print(z)
z2 = y[[0,2,4]]
print(z2)

print('yから３以上の要素を取得')
print("y >= 3:{}".format(y>=3))
print("３以上の要素:{}".format(y[y>=3]))
# とりあえずブーリアン配列を作って要素へアクセスすることだけ覚えておく

