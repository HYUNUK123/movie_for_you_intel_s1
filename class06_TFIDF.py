# TF-IDF (Term Frequency-Inverse Document Frequency)는 자연어 처리와 정보 검색 분야에서 사용되는
# 텍스트 데이터의 특성을 나타내는 수치입니다. 이것은 주로 텍스트 데이터에서 각 단어의 중요성을 평가하는 데 사용됩니다.

#TF (Term Frequency): 단어의 상대적 빈도를 나타내는 값으로, 특정 문서 내에서 어떤 단어가 얼마나 자주 나타나는지를 측정합니다.
# 보통 문서 내에서 단어의 빈도가 높을수록 그 단어의 중요도가 높다고 간주합니다.
# 하지만 이 값은 단어가 얼마나 자주 나타나는지만 고려하기 때문에 모든 단어를 동등하게 취급합니다.

#IDF (Inverse Document Frequency): 역문서 빈도는 단어의 전체 문서 집합 내에서의 등장 빈도에 대한 역수를 의미합니다.
#이 값은 단어의 희귀성을 측정하며, 전체 문서에서 자주 나타나는 단어의 중요도를 감소시킵니다.
#희귀한 단어는 상대적으로 높은 IDF 값을 갖습니다.
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #TF-IDF 변환을 수행하는 데 사용
from scipy.io import mmwrite, mmread #희소 행렬(Sparse Matrix)을 저장하고 로드하기 위한 기능을 제공
# mmwrite 함수를 사용하여 희소 행렬을 파일로 저장하고, mmread 함수를 사용하여 저장된 희소 행렬을 다시 로드할 수 있습니다.
import pickle #pickle : Python 객체(리스트, 딕셔너리, 클래스 인스턴스 등)를 이진 형식으로 직렬화하고, 이러한 직렬화된 객체를 다시 역직렬화하여 Python 객체로 복원할 수 있게 해줍

df_reviews = pd.read_csv('./crawling_data_class/cleaned_one_review.csv')
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['reviews'])
print(Tfidf_matrix.shape)

with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

mmwrite('./models/Tfidf_movie_review.mtx', Tfidf_matrix)
