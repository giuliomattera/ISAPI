#Importa le librerie necessarie
import library as lib
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#Definizione dell'architettura di rete
initializer = tf.keras.initializers.GlorotNormal()
initial_learning_rate = 1e-2
EPOCHS = 300
BATCH = 64
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=6000,
    decay_rate=0.96,
    staircase=True)

model = tf.keras.Sequential()
model._name = 'WeldingClassifier'
model.add(tf.keras.Input(shape=(4), name = 'InputLayer'))
model.add(tf.keras.layers.Dense(300, name = 'DenseLayer', 
                                activation = 'tanh',
                                kernel_initializer=initializer))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(100, name = 'DenseLayer3', 
                                activation = 'tanh', 
                                kernel_initializer=initializer))
model.add(tf.keras.layers.Dense(1, activation = 'sigmoid',
                                name = 'ClassificationLayer'))

optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
model.compile(optimizer=optimizer, 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

#Importa dataset
PATH = R'~/Scrivania/PhD/Paper/DNN semi-automatic GMAW inspection/DataPython.ods'
x, y, x_val, y_val, x_t, y_t = lib.xslx_2_numpy(PATH, 0.15, 0.3)
e, e_val = lib.error_values(x, x_val)
#Inizia fase di addestramento 
print ('[INFO] Training the networks....')
HistoryTrain = model.fit(e, y, 
                         validation_data = (e_val, y_val),
                         verbose = 1, epochs = EPOCHS, 
                         batch_size = BATCH)

print ('[INFO] Results plotting....')
#Plot dei risultati
plt.plot(HistoryTrain.history['accuracy'])
plt.plot(HistoryTrain.history['val_accuracy'])
plt.title('Accuracy trend')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['Training', 'Validation'], loc='lower right')
plt.show()

plt.plot(HistoryTrain.history['loss'])
plt.plot(HistoryTrain.history['val_loss'])
plt.title('Loss trend')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['Training', 'Validation'], loc='upper right')
plt.show()

lib.testing(model, x_t, y_t)

#Salvataggio del modello
SAVE_PATH = r'C:\Users\giuli\OneDrive\Desktop\Nuova cartella'
SAVE = False
if SAVE == True:
    tf.saved_model.save(model, SAVE_PATH)
    
