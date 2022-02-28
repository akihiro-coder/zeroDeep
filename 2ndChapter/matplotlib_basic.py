import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.arange(0, 6, 0.1)
print("x:{}".format(x))
print("x.shape:{}".format(x.shape))
print("type of x:{}".format(type(x)))
y = np.sin(x)
print("type of y:{}".format(type(y)))
print("y:{}".format(y))
plt.plot(x, y)
plt.show()


# cosのグラフを追記してみる
y2 = np.cos(x)
plt.plot(x, y, label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()


# 画像を表示してみる

img = imread(fname='cat_image.png')
print(type(img))
print(img.shape)
plt.imshow(X=img)
plt.show()



