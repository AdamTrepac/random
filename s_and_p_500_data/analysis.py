from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SandP500.csv")
df = df.iloc[::-1].reset_index(drop=True)

print(df.head(5))
print(df.describe())
print(df.info())
df['Date'] = pd.to_datetime(df['Date']) # convert the data to dateTime to make plotting much faster
print(df.info())
# print(df.corr())

# roll_avg = df['Close/Last']mavg = close.

# close_df = df["Close/Last"].to_frame()
# print(close_df.head(5))
# close_df["roll_avg"] = close_df["Close/Last"].rolling(4).mean()
# print(close_df)

df["roll_avg"] = df["Close/Last"].rolling(365).mean()
# df.dropna(inplace=True)
print(df)

# df.plot(x='Date', y='Close/Last', kind='line', color='blue')
# df.plot(x='Date', y='roll_avg', kind='line', color='red')
# plt.figure(figsize=(10, 6))

plt.plot(df['Date'], df['Close/Last'], label='Close', color='blue')
plt.plot(df['Date'], df['roll_avg'], label="Rolling Avg", color='red')
plt.title('S & P 500 over time')
plt.xlabel('Date')
plt.ylabel('Price $')
plt.legend()
plt.show()