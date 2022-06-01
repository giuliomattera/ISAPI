import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#Prepare data
x = np.linspace(0, 360/57.3, 1000)
y = np.sin(x)

#Create network architecture

inp = tf.keras.layers.Input((1,1))
h = tf.keras.layers.Dense(100, activation = tf.nn.tanh)(inp)
h = tf.keras.layers.Dense(100, activation = tf.nn.tanh)(h)
out = tf.keras.layers.Dense(1, activation = tf.nn.tanh)(h)

model = tf.keras.Model(inp, out)

#Compile model with loss function and optimizer

model.compile(optimizer = tf.keras.optimizers.RMSprop(3e-4),
              loss = "mse",
              metrics = "accuracy")

#Train
history = model.fit(x, y, epochs = 500)

#Plot results
print("[INFO] plotting resume of training...")

yn = model.predict(x)
yn = yn.reshape((yn.shape[0], 1))

plt.plot(x, yn, label = "NN prediction")
plt.plot(x,y, label = "Ground truth")
plt.xlabel("Angle [rad]")
plt.ylabel("Sine")
plt.legend()
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.title('Loss trend')
plt.ylabel('MSE')
plt.xlabel('Epochs')
plt.legend(['Training'], loc='upper right')
plt.show()
