from datetime import datetime


# Using "with" notation
with st.sidebar:
    dt_now = datetime.today()
    
    d = st.date_input(
     "날짜를 선택하세요.",
     datetime.date(dt_now.year, dt_now.month, dt_now.day - 1))

    st.write('선택날짜:', d)