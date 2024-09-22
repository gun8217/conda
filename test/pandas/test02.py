import pandas as pd

data = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    '점수': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)

# 문제1. 주어진 데이터프레임에서 점수가 85 이상인 학생의 이름과 점수를 출력하세요.
print(df.loc[df['점수'] >= 85], '\n')

# 문제2. 주어진 데이터프레임에서 두 번째 학생의 이름과 네 번째 학생의 점수를 출력하세요.
print(df.iloc[1, 0], df.iloc[3, 1], '\n')

# 문제3. 주어진 데이터프레임을 점수를 기준으로 오름차순으로 정렬하세요.
print(df.sort_values(by='점수'), '\n')

# 문제4. 주어진 데이터프레임에서 점수가 80 이하인 학생을 삭제한 후 결과를 출력하세요.
df_drop = df.drop(df[df['점수'] <= 80].index)
print(df_drop, '\n')

# 문제5. 각 학생의 점수를 제곱한 새로운 열을 추가하세요.
df['제곱'] = df['점수'].apply(lambda x: x**2)
print(df, '\n')

# 문제6. 학생들의 점수에 대해 순위를 매기고, 같은 점수일 경우 동점을 부여하세요.
print(df['점수'].rank(method='dense', ascending=False), '\n')

# 문제7. 다음 데이터프레임을 사용하여 각 팀별 점수의 최대값을 계산하세요.
data7 = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    '팀': ['A', 'A', 'B', 'B', 'A', 'B'],
    '점수': [85, 92, 78, 88, 95, 70]
}
df7 = pd.DataFrame(data7)
print(df7.groupby('팀')['점수'].max())

# 문제8. 2023년 10월 1일부터 10일까지의 날짜를 생성하고, 주말 날짜(토요일, 일요일)를 필터링하여 출력하세요.
date = pd.to_datetime('2023년 10월 1일', format='%Y년 %m월 %d일')
date = pd.date_range(date, periods=10)
print(date)
weekends = date[date.dayofweek >= 5]  # 5는 토요일, 6은 일요일
print(weekends)