import pandas as pd

df = pd.read_csv('BCT-USD.csv')

# Создание нового столбца 'Месяц' на основе столбца 'Дата'
df['Date'] = pd.to_datetime(df['Date']).dt.month

# Фильтрация данных для месяцев, где цена при закрытии была выше цены открытия
filtered_df = df[df['Close'] > df['Open']]

# Получение уникальных значений месяцев
months = filtered_df['Date'].unique()

# Проверка, есть ли месяцы, удовлетворяющие условию
if len(months) > 0:
    for month in months:
        print(month)
else:
    print("Таких месяцев нет")
