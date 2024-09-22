import pandas as pd

data = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    '점수': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)

# 1. 점수가 90 이상인 학생의 이름과 점수를 출력하세요.
print(df.loc[[1, 4]], '\n')
print(df.loc[df['점수'] >= 90], '\n')

# 2. 첫 번째 학생의 이름과 세 번째 학생의 점수를 출력하세요.
print(df.iloc[0, 0], df.iloc[2, 1], '\n')

# 3. 점수를 기준으로 데이터프레임을 내림차순으로 정렬하세요.
print(df.sort_values(by='점수', ascending=False), '\n')

# 4. '점수' 열을 삭제한 데이터프레임을 출력하세요.
df_drop = df.drop(labels='점수', axis=1)
print(df_drop, '\n')

# 5. 각 학생의 점수에 10을 더한 '점수_10더하기' 열을 추가하세요.
df['더하기'] = df['점수'].apply(lambda x: x + 10)
print(df, '\n')

# 6. 학생들의 점수를 기준으로 순위를 매긴 새로운 열 '순위'를 추가하세요.
df['순위'] = df['점수'].rank(ascending=False)
print(df, '\n')

# 7. 팀별 평균 점수를 계산하세요.
data7 = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    '팀': ['A', 'A', 'B', 'B', 'A', 'B'],
    '점수': [85, 92, 78, 88, 95, 70]
}
df7 = pd.DataFrame(data7)
df7_mean = df7.groupby('팀')['점수'].mean()
print(df7_mean, '\n')

# 8. 2023년 9월 22일부터 5일간의 날짜를 생성하고 'yyyy-mm-dd' 형식으로 출력하세요.
date = pd.to_datetime('2023년 9월 22일', format='%Y년 %m월 %d일').strftime('%Y-%m-%d')
date = pd.date_range(date, periods=5)
print(date)