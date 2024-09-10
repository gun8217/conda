import requests
import pandas as pd

# 기상청 기후 데이터 API URL
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
params = {
    'serviceKey': 'YOUR_API_KEY',  # API 키를 여기에 입력하세요.
    'numOfRows': '10',
    'pageNo': '1',
    'dataType': 'JSON',
    'base_date': '20220901',  # YYYYMMDD 형식의 시작 날짜
    'base_time': '0600',
    'nx': '60',  # X 좌표
    'ny': '127'  # Y 좌표
}

response = requests.get(url, params=params)
data = response.json()

# JSON 데이터를 DataFrame으로 변환
df = pd.json_normalize(data['response']['body']['items']['item'])

print(df.head())