import pandas as dp

data = dp.read_csv('emojis.csv')
print(data['Subcategory'][len(data)-1])