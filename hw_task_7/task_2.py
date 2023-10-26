from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
_data = pd.read_csv('titanic.csv')
dataset = np.array(_data)

for i, row in enumerate(dataset):
    row[2] = int((row[2])[0])

dataset = dataset[:, [2, 3, 5, 6]]
dataset = dataset.astype(float)  # Преобразование строк в числа с плавающей точкой
for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:, i])]
pass

X_train = dataset[:, [0, 1, 3]]
Y_train = dataset[:, 2]

X_train, _, Y_train, _ = train_test_split(X_train, Y_train, shuffle=True)

model = svm.SVC()
model.fit(X_train, Y_train)

predicted  = model.predict(X_train[:10])
print(f'Предсказания\n{predicted}')
print(f'Ответы\n{Y_train[:10]}')