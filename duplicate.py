import pandas as pd

df=pd.read_csv('./crawling_data/crawling_movies_2020.csv')
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
#
df.drop_duplicates(subset='titles', keep='first', inplace=True)
# df.duplicated()
df.to_csv('./crawling_data/crawling_movies_2020_duplicate.csv',index=False)