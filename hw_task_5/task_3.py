import pandas as pd
from random import randint


index_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
answer = pd.DataFrame([[randint(1, 10) for j in range(10)] for i in range(10)], index=index_name, columns=index_name)
print(answer.size, answer.columns, (answer.mean()).mean())
answer.to_csv('answer.csv')