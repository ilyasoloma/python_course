import numpy as np
matrix_1 = np.random.randint(0, 100, 32).reshape((8,4))
matrix_2 = np.random.randint(0, 100, 32).reshape((4,8))
answ = np.dot(matrix_1,matrix_2)
print(answ)