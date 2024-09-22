import pandas as pd

# 문자열을 datetime으로 변환
date_str = '2023-09-22'
to_datetime = pd.to_datetime(date_str)
print(f"{to_datetime = }\n")

# 날짜 범위 생성
date_range = pd.date_range(start='2023-01-01', end='2023-01-10')
print(f"{date_range = }\n")

# 문자열을 datetime으로 변환
data = {
    'date': ['2023-01-01', '2023-05-02', '2023-11-03'],
    'value': [10, 20, 30]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
print(f"{df = }\n")

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
print(f"{df = }\n")

# 7일 더하기
df['future_date'] = df['date'] + pd.Timedelta(days=7)
print(f"{df = }\n")

# 특정 날짜 이후의 데이터 필터링
filtered_df = df[df['date'] > '2023-05-02']
print(f"{filtered_df = }\n")

# 날짜 인덱스 설정
df.set_index('date', inplace=True)
print(f"{df = }\n")




dates = pd.date_range('2023-09-22 10:30:15', periods=5, freq='h')
df_datetime = pd.DataFrame({'datetime': dates})

# 1. yyyy.mm.dd HH:MM:SS
df_datetime['yyyy.mm.dd HH:MM:SS'] = df_datetime['datetime'].dt.strftime('%Y.%m.%d %H:%M:%S')
# 2. yy-mm-dd HH:MM:SS
df_datetime['yy-mm-dd HH:MM:SS'] = df_datetime['datetime'].dt.strftime('%y-%m-%d %H:%M:%S')
# 3. mm-dd-yy HH:MM:SS
df_datetime['mm-dd-yy HH:MM:SS'] = df_datetime['datetime'].dt.strftime('%m-%d-%y %H:%M:%S')
# 4. yyyy년mm월dd일 HH시MM분SS초
df_datetime['yyyy년mm월dd일 HH시MM분SS초'] = df_datetime['datetime'].dt.strftime('%Y년%m월%d일 %H시%M분%S초')
print(df_datetime[['datetime', 'yyyy.mm.dd HH:MM:SS', 'yy-mm-dd HH:MM:SS',
                   'mm-dd-yy HH:MM:SS', 'yyyy년mm월dd일 HH시MM분SS초']])