import pandas as pd
import matplotlib as plt

df = pd.read_csv("SandP500.csv")

print(df.head(5))
print(df.describe())
# print(df.corr())

# roll_avg = df['Close/Last']mavg = close.

# close_df = df["Close/Last"].to_frame()
# print(close_df.head(5))
# close_df["roll_avg"] = close_df["Close/Last"].rolling(4).mean()
# print(close_df)

df["roll_avg"] = df["Close/Last"].rolling(4).mean()
print(df)
