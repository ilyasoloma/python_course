from keras.models import Sequential
from keras.layers import Dense
import numpy as np


class Neural:
    def __init__(self, layer_1, layer_2, layer_3, input_dim, epochs, batch_size, verbose):
        self.X = None
        self.Y = None
        self.dataset = None
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose
        self.layer_1 = layer_1
        self.layer_2 = layer_2
        self.layer_3 = layer_3
        self.input_dim = input_dim
        self.model = Sequential()

    def prepare_data(self):
        self.dataset = np.genfromtxt('data.txt', delimiter=',', dtype=float)
        self.X = self.dataset[:, :8]
        self.Y = self.dataset[:, -1]

    def learn_network(self):
        self.model.add(Dense(self.layer_1, input_dim=self.input_dim, activation='relu'))
        self.model.add(Dense(self.layer_2, activation='relu'))
        self.model.add(Dense(self.layer_3, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X, self.Y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)

    def inference(self, X):
        return self.model.predict(X)
