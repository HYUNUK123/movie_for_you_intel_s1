import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data_class/reviews_2023.csv')
df.info()

okt = Okt() #한국어 형태소 분석기

df_stopwords = pd.read_csv('./stopwords.csv') #불용어
stopwords = list(df_stopwords['stopword'])

count = 0
cleaned_sentences = []
for review in df.review[179000:]:
    count += 1
    if count % 100 == 0:
        print('.', end='')
    if count % 1000 == 0:
        print()
    if count % 10000 == 0:
        print(count / 1000, end='')
    review = re.sub('[^가-힣]', ' ', review) #가~힣 제외하고는 ' '로 대체
    tokened_review = okt.pos(review, stem=True) #pos 메서드를 사용하여 단어가 어떤 품사인지 식별하는 작업을 수행, Stem :단어의 기본 형태를 추출하는지 여부를 결정, True:기본 형태 추출, False:기본 형태 미추출

    df_token = pd.DataFrame(tokened_review, columns=['word', 'class']) #word에는 단어, class에는 명사인지 형용사인지가 들어감

    df_token = df_token[(df_token['class']=='Noun') |
                        (df_token['class']=='Verb') |
                        (df_token['class']=='Adjective')]
    words = []
    for word in df_token.word:
        if 1 < len(word):
            if word not in stopwords:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
# df_test = df.iloc[:10, :]
df['cleaned_sentences'] = cleaned_sentences
df = df[['title', 'cleaned_sentences']]
print(df.head(10))

df.to_csv('./crawling_data/cleaned_review.csv', index=False)