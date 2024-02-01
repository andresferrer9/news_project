import pandas as pd

df = pd.read_csv("../data/raw/news_dataset.csv")

print(df.head(10))
print(df.tail(10))
print(df.shape)