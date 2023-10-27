import pandas as pd
import glob

data_paths = glob.glob('./crawling_data_class/*') #괄호 안의 경로가 리스트에 반환
print(data_paths[:-5])

df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()
my_year = 2023
df.to_csv('./crawling_data_class/reviews_{}.csv'.format(my_year), index=False)

#컬럼명 맞추는 코드
#df = df.rename(columns={'나이':'연령'})
#ndf3 = df.reset_index()

