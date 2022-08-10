import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

from urllib.request import Request, urlopen
import json  
 
import datetime


#박스오피스 함수
def box(targetDt) :
  apikey = 'f5eef3421c602c6cb7ea224104795888'  
  targetDt = targetDt.replace('-', '')

  url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
  url = url + 'key=' + apikey 
  url = url + '&targetDt=' + targetDt

  data =  urlopen(url).read().decode()
  data = json.loads(data) 

  dailyBoxOfficeList = data['boxOfficeResult']['dailyBoxOfficeList']
  
  showRange = data['boxOfficeResult']['showRange'][:8]

  df = pd.DataFrame(columns={'일자','순위','영화제목','매출액','관객수'})

  for item in dailyBoxOfficeList :
    
    line = []
    #일자,순위,영화제목,매출액,관객수
    #showRange,rank,movieNm,salesAmt,audiCnt
    rank = item['rank']
    movieNm = item['movieNm']
    salesAmt = item['salesAmt']
    audiCnt = item['audiCnt']

    line.append(showRange)
    line.append(rank)
    line.append(movieNm)
    line.append(salesAmt)
    line.append(audiCnt)

    idx = df.index.max()
    if np.isnan(idx): idx = 0
    else : idx = idx + 1

    df.loc[idx] = line
      
  df.columns = ['일자','순위','영화제목','매출액','관객수']
  df['매출액'] = df['매출액'].astype('int')
  df['관객수'] = df['관객수'].astype('int')

  return df


# Using "with" notation
with st.sidebar:
    dt_now = datetime.datetime.today()
    
    d = st.date_input(
     "날짜를 선택하세요.",
    datetime.date(dt_now.year, dt_now.month, dt_now.day))

    st.write('선택날짜:', d)


df_box = box(str(d))
df_box = df_box[['순위','영화제목','매출액','관객수']]

st.dataframe(df_box)

df1 = df_box[['영화제목', '매출액']].set_index('영화제목')

st.bar_chart(df1, width=500, height=500)


#fig, ax = plt.subplots()
#ax.barh(df_box['매출액'])

#st.pyplot(fig)