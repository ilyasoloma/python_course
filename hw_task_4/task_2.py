import numpy as np
matrix = np.array([1 if (i % 2 == 0  and (i//8) % 2 == 0 ) or ((i//8) % 2 != 0 and i % 2 !=0 ) else 0 for i in range(64)], int).reshape((8, 8))
print(matrix)