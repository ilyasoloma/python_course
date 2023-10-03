import pandas as pd
from random import randint

answer = pd.DataFrame([randint(1, 10) for j in range(10)] for i in range(10))