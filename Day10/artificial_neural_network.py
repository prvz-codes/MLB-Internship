import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from tensorflow import keras


(x_train , y_train) , (x_test , y_test) = fashion_mnist.load_data()

x_train , x_test = np.array(x_train / 255.0) , np.array(x_test/ 255.0)

# print(x_train[1])
# print(x_test[1])

# plt.imshow(x_test[50] , cmap="gray")
# plt.show()


items = [
    "T-shirt","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle Boot"
]

for i in range(25):
    plt.subplot(5 , 5 , i+1)
    plt.grid(False) , plt.axis('off')
    values = items[y_train[i]]
    plt.text(0 ,0 , values)
    plt.imshow(x_train[i])
plt.tight_layout()
plt.show()

model =  keras.Sequential([
    keras.layers.Flatten(input_shape = (28 , 28)),
    keras.layers.Dense(128 , activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.summary()


model.compile(optimizer = "SGD" , loss = "sparse_categorical_crossentropy" , metrics = ["accuracy"])


model.fit(x_train , y_train , epochs = 10)

test_loss , test_accuracy = model.evaluate(x_test , y_test , verbose = 0)

print("test  loss" + str(test_loss))
print("accuracy " + str(test_accuracy))

