import pandas as pd

df1 = pd.read_csv('./crawling_data/crawling_movies_20190.csv')
df2 = pd.read_csv('./crawling_data/crawling_movies_20191.csv')

df=df1.append(df2)
df.to_csv('./crawling_data/crawling_movies_2019.csv',index=False)