import pandas as pd
from gensim.models import Word2Vec #단어 임베딩(Word Embedding)을 학습하는데 사용
#Word Embedding : 단어를 고차원 벡터로 나타내는 방법 : 컴퓨터가 텍스트 데이터를 이해하고 처리하는데 도움

df_review = pd.read_csv('./crawling_data_class/cleaned_one_review.csv')
df_review.info()

reviews = list(df_review['reviews'])
print(reviews[0])

tokens = []
for sentence in reviews:
    token = sentence.split()
    tokens.append(token)
print(tokens[0])

embedding_model = Word2Vec(tokens, vector_size = 100, window=4, min_count=20,
                           workers=16, epochs=100, sg=1)
#vector_size = 100: 워드 임베딩 벡터의 크기를 나타냅니다.
# 각 단어는 100차원의 벡터로 표현됩니다. 이 벡터는 단어의 의미적 특성을 포함합니다.

#window=4 : 주변 단어의 창 크기를 나타냅니다. Word2Vec 모델은 각 단어 주변의 일정한 범위 내에 있는 단어를 고려하여
# 단어의 벡터 표현을 학습합니다. 이 값은 주변 문맥을 얼마나 넓게 고려할지 결정합니다.

#min_count=20 : 단어의 최소 등장 횟수를 나타냅니다. 이 값보다 적게 나타난 단어는 모델 학습에서 무시됩니다.
#즉, 희귀한 단어는 무시되고, 자주 등장하는 단어만을 학습에 활용합니다.

#workers = 16: 학습에 사용할 CPU 코어 수

#sg = 1: Skip-Gram 모델을 사용하도록 설정합니다.
# Skip-Gram은 Word2Vec 모델의 하나로, 주어진 단어 주변의 단어를 예측하는 방식으로 학습합니다.

embedding_model.save('./models/word2vec_movie_review.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))
