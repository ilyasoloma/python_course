import pandas as pd
import matplotlib.pyplot as plt

def create_plots(start_date, end_date):
    data = pd.read_csv('BCT-USD.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    filtered_df = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
    plt.plot(filtered_df['Date'], filtered_df['Open'], label='Open')
    plt.plot(filtered_df['Date'], filtered_df['Close'], label='Close')
    plt.show()

create_plots('2021-11-11', '2021-12-29')