from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = ChromeOptions()
user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument('user-agent=' + user_agent)
options.add_argument("lang=ko_KR")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)  # <- options로 변경
years = ['2019','2020']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']

for y in years:
    df_crawlings = pd.DataFrame(columns=['titles', 'reviews'])
    for m in months:
        url1= 'https://movie.daum.net/ranking/boxoffice/monthly?date={}{}'.format(y, m)
        for k in range(1,31):
            try:
                df_titles = pd.DataFrame()
                titles = []
                df_reviews = pd.DataFrame()
                reviews = []
                
                #중복 제거
                crawled_titles = [] #중복 제거
                
                driver.get(url1)

                driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[2]/ol/li[{}]/div/div[2]/strong/a'.format(k)).click() #영화 제목 클릭
                time.sleep(1)
                driver.find_element(By.XPATH,'/html/body/div[2]/main/article/div/div[2]/div[1]/ul/li[4]/a/span').click() #영화 리뷰 클릭
                title = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[1]/div[2]/div[1]/h3/span[1]').text #영화 제목 읽기
                title = re.compile('[^가-힣]').sub(' ', title)
                
                #중복 제거
                if title in crawled_titles: #중복 있으면 다시 처음으로 돌아가라
                    continue
                
                titles.append(title)
                print(titles)

                # 최대 2초 기다리기(더보기)
                for j in range(5):
                    try:
                        wait = WebDriverWait(driver, 2)
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button'))).click() #더보기 클릭
                    except:
                        pass

                for i in range(1,161):
                    try:
                        review = driver.find_element(By.XPATH,'/html/body/div[2]/main/article/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/ul[2]/li[{}]/div/p'.format(i)).text
                        review = re.compile('[^가-힣]').sub(' ', review)
                        reviews.append(review)
                    except:
                        review = ''
                        reviews.append(review)
                print(reviews)

                all_reviews = ','.join(reviews)
                df_crawlings = df_crawlings.append({'titles': title, 'reviews': all_reviews}, ignore_index=True)
            except:
                pass

        df_crawlings.to_csv('./crawling_data/crawling_movies_{}.csv'.format(y),index=False)