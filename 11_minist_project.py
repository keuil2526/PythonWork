import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#Load_MNIST_Dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#View_Dataset_Shape
print(f"x_train shape : {x_train.shape}")
print(f"y_train shape : {y_train.shape}")
print(f"x_test shape : {x_test.shape}")
print(f"y_test shape : {y_test.shape}")

#View_First_Image
plt.figure(figsize=(5,5))
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Label : {y_train[0]}")
plt.axis('off')
plt.show()

print(x_train[0][:, :])
print()

#Data_Regularization
x_train = x_train / 255.0
x_test = x_test / 255.0
print(x_train[0][:, :])
print()