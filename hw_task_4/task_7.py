import numpy as np

def func(A, S, last = False):
    X = len(A)
    B = np.random.randint(0, 10, S*X).reshape((S, X))
    C = A * B
    S = []
    for line in C:
        tmp = 0
        for num in line:
            tmp += num
        S.append(tmp)
    if last:
        np.maximum(S, 0)
    else:
        np.sin(S)
    return (S, B)

vect1 = np.random.randint(0, 30, 5)
vect2, B1 = func(vect1, 10)
vect3, B2 = func(vect2, 10)
vect4, B3 = func(vect3, 5, last=True)
print(vect4)