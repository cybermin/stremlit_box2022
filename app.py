import streamlit as st
import pandas as pd
import numpy as np

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

  df = pd.DataFrame()

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

    line = pd.DataFrame(line)
    df.append(line)
      
  return df


st.write(box('2022-08-09'))

# Using "with" notation
with st.sidebar:
    dt_now = datetime.datetime.today()
    
    d = st.date_input(
     "날짜를 선택하세요.",
    datetime.date(dt_now.year, dt_now.month, dt_now.day))

    st.write('선택날짜:', d)