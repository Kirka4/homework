import pandas as pd

df = pd.read_csv("C:\Users\kir4i\Downloads\Telegram Desktop/2 intermediate attestation titanic.csv")

df = df[df['Age'] >= 0]

df['Last Name'] = df['Name'].str.split(',').str[0]

df = df.sort_values('Last Name')

print(df)