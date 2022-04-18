import sys
import os
import numpy as np
import pickle
sys.path.append("../")
from deep_learning_from_scratch.dataset.mnist import load_mnist
from PIL import Image
from deep_learning_from_scratch.common.functions import sigmoid, softmax




(x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, one_hot_label=True) 
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
print(batch_mask)
print(type(batch_mask))

# numpy配列に配列を渡せる
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]



# original cross_entropy_error
def cross_entrpy_error(y, t):
    delta = 10**(-7)
    return -np.sum(t * np.log(y * delta))

# mini-batch cross_entropy_error one-hot
def cross_entorpy_erro(y, t):
    if y.ndim == 1:
        t = t
# mini-batch cross_entropy_error non one-hot

