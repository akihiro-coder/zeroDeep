import numpy as np

print('ANDゲートを実装')
#def AND(x1, x2):
#    w1, w2, theta = 0.5, 0.5, 0.7 #適当なパラメータの値をセット
#    tmp = x1*w1 + x2*w2
#    if tmp <= theta:
#        return 0
#    else:
#        return 1
#
#print(AND(0,0))
#print(AND(1,1))
#print(AND(1,0))
#print(AND(0,1))


print('重みとバイアスの総和を実装')

x = np.array([0,1])#input
w = np.array([0.5, 0.5])#weight
b = -0.7#bias

print("w*x:{}".format(w*x))
print("sum(w*x):{}".format(np.sum(w*x)))
print("sum(b + w*x):{}".format(b + np.sum(w*x)))


print('重みとバイアスによる方式でandゲートを実装')

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("nandとorゲートを実装")

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print('xorゲートの実装')
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))


