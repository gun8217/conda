import streamlit as st
import pandas as pd
import numpy as np

st.title('내 첫 번째 Streamlit 앱')

st.write("안녕하세요! 여기에 데이터를 확인해보세요:")

# 데이터 생성
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

# 데이터프레임 표시
st.write(data)

# 차트 표시
st.line_chart(data)