import numpy as np
def func(n):
    factor_list = [x for x in range(2, n) if n % x == 0]
    if factor_list:
        for row in range(len(factor_list)):
            for column in range(len(factor_list)):
                if row != column:
                    print(np.zeros((factor_list[row], factor_list[column])))
    else:
        print('Нет множителей')
func(28)