import pandas as pd

df = pd.read_csv("SandP500.csv")

print(df.head(5))
# print(df.corr())

# roll_avg = df['Close/Last']mavg = close.
close_df = df["Close/Last"].to_frame()
print(close_df.head(5))
close_df["roll_avg"] = close_df["Close/Last"].rolling(4).mean()
print(close_df)