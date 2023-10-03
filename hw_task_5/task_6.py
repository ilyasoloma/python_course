import pandas as dp

def find_category(name_category, data):
    if len(data[data['Category'] == name_category]) > 0:
        return len(data[data['Category'] == name_category])/len(data) * 100
    else:
        return "Такой категории не существует"

input_data = dp.read_csv('emojis.csv')
print(find_category('People & Body', input_data))