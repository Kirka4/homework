import pandas as pd

df_Icecream = pd.read_csv(r"C:\Users\kir4i\Downloads\Telegram Desktop\2.4 sales.csv")

df_Weather = pd.read_csv(r"C:\Users\kir4i\Downloads\Telegram Desktop\2.4 weather.csv")

result = pd.merge(df_Weather, df_Icecream, on='date')

result = result.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y'])

print(result)