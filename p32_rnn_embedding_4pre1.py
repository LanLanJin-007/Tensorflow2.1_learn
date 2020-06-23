import numpy as np 
import tensorflow as tf 
from tensorflow.keras.layers import Dense, SimpleRNN, Embedding
import matplotlib.pyplot as plt 
import os 

input_word = 'abcdefghijklmnopqrstuvwxyz'
w_to_id = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
training_set_scaled = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                        21, 22, 23, 24, 25]

x_train = []
y_train = []

for i in range(4, 26):
    x_train.append(training_set_scaled[i-4: i])
    y_train.append(training_set_scaled[i])

np.random.seed(7)
np.random.shuffle(x_train)
np.random.seed(7)
np.random.shuffle(y_train)
tf.random.set_seed(7)

x_train = np.reshape(x_train, (len(x_train), 4))
y_train = np.array(y_train)

model = tf.keras.Sequential([
    Embedding(26, 2),
    SimpleRNN(3),
    Dense(26, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
            metrics=['sparse_categorical_accuracy'])

checkpoint_save_path = './checkpoint/rnn_onehot_1pre1.ckpt'

if os.path.exists(checkpoint_save_path+'.index'):
    print('---------------- load the model --------------------')
    model.load_weights(checkpoint_save_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                save_weights_only=True,
                                                save_best_only=True,
                                                monitor='loss')

history = model.fit(x_train, y_train, batch_size=32, epochs=100, callbacks=[cp_callback])

model.summary()

file = open('./weights.txt', 'w')
for v in model.trainable_variables:
    file.write(str(v.name) + '\n')
    file.write(str(v.shape) + '\n')
    file.write(str(v.numpy()) + '\n')
file.close()


acc = history.history['sparse_categorical_accuracy']
loss = history.history['loss']

plt.subplot(1, 2, 1)
plt.plot(acc, label= 'Training Accuracy')
plt.title('Training Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(loss, label='Training Loss')
plt.title('Training Loss')
plt.legend()
plt.show()

preNum = int(input('input the number of test alphabet:'))
for i in range(preNum):
    alphabet1 = input('input test alphabet:')
    alphabet = [w_to_id[a] for a in alphabet1]
    # print(np.reshape(alphabet, (1, 1, 5))
    alphabet = np.reshape(alphabet, (1, 4))
    result = model.predict([alphabet])
    pred = tf.argmax(result, axis=1)
    pred = int(pred)
    tf.print(alphabet1 + ' -> ' + input_word[pred])
