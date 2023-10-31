import pandas as pd
from wordcloud import WordCloud #워드클라우드 : 단어의 상대적 빈도를 사용하여 단어를 그래픽으로 나타내는 기술
import collections #단어 빈도를 계산하기 위해 사용됩니다.
import matplotlib.pyplot as plt
from matplotlib import font_manager #사용할 폰트를 설정하는데 사용

font_path = './malgun.ttf' # 사용할 한국어 폰트 경로 설정
font_name = font_manager.FontProperties(fname=font_path).get_name() # 설정한 폰트의 이름을 가져오기
plt.rc('font', family='NanumBarunGothic') #나눔글꼴은 저작권 신경 안 써도 됨.

df = pd.read_csv('./crawling_data_class/cleaned_one_review.csv')
words = df.iloc[1044, 1].split() #특정 행(1044번 행)의 두 번째 열 데이터를 가져와서 공백을 기준으로 단어로 분리
print(words)

worddict = collections.Counter(words) # 단어의 빈도를 계산
worddict = dict(worddict) # 빈도 딕셔너리를 일반 딕셔너리로 변환
print(worddict)

# 워드클라우드 이미지 생성
wordcloud_img = WordCloud(
    background_color='white', # 배경 색상 설정
    max_words=2000, # 표시할 최대 단어 수
    font_path=font_path # 사용할 한국어 폰트 경로 설정
    ).generate_from_frequencies(worddict)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud_img, interpolation='bilinear') # 'bilinear'은 이미지를 부드럽게 표시하는 보간 방법 중 하나
plt.axis('off') # 축을 비활성화하여 불필요한 테두리를 제거
plt.show() # 워드클라우드 표시