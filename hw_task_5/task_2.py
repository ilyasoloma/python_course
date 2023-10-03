import pandas as pd
from random import randint


index_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
answer = pd.DataFrame([[randint(1, 10) for j in range(10)] for i in range(10)], index=index_name)

for index in index_name:
    row = answer.loc[index]
    flag = True
    for num in row:
        if num <= 5:
            flag = False
            break
    if flag:
        print(row)
