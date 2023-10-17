from keras.models import Sequential
from keras.layers import Dense
import numpy as np

dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

X = dataset[:, :8]
Y = dataset[:, -1]
pass
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=15, batch_size=10, verbose=2)
X = np.expand_dims(X, axis=1)
print('Предсказание')
for i in range(3):
    print(model.predict(X[i]))
