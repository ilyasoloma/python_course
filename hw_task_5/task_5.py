import pandas as dp
import matplotlib.pyplot as plt

data = dp.read_csv('emojis.csv')
freq_dict = dict()
years = data['Year']
for year in years:
    if year not in freq_dict:
        freq_dict[year] = 1
    else:
        freq_dict[year] += 1

freq_dict = sorted(freq_dict.items(), key=lambda item: item[0])
print(freq_dict)
plt.plot([freq_dict[i][0] for i in range(len(freq_dict))],[freq_dict[i][1] for i in range(len(freq_dict))])
plt.show()
