import streamlit as st
import pandas as pd
import numpy as np
#from datetime import datetime
import datetime

# Using "with" notation
with st.sidebar:
    #dt_now = datetime.today()
    
    d = st.date_input(
     "날짜를 선택하세요.",
     datetime.date(2022, 8, 9))

    st.write('선택날짜:', d)