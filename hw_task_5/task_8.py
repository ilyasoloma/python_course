import pandas as pd

data = pd.read_csv('BCT-USD.csv')
filtered_df = data.sort_values(by='Volume')
print(str(filtered_df['Date'][0])[5:7])