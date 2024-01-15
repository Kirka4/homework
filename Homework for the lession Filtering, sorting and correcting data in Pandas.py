import pandas as pd

df =pd.read_csv(r"C:\Users\kir4i\Downloads\Telegram Desktop\2.3 clients_countries_.csv")

Countries = df.groupby('countries')

result = Countries['age'].agg(['count', 'mean'])

print(result)