from tensorflow import keras

model = keras.Sequential([
    keras.layers.Input(shape=(4,)),
    keras.layers.Dense(8 , activation="relu"),
    keras.layers.Dense(1 , activation="sigmoid")
])

model.summary()