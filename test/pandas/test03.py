import pandas as pd

data = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    '점수': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)

# 주어진 데이터프레임에서 점수가 90 이상인 학생의 이름과 점수를 출력하세요.
print(df[df['점수'] >= 90], '\n')
print(df.loc[df['점수'] >= 90], '\n')

# 주어진 데이터프레임에서 세 번째 학생의 이름과 첫 번째 학생의 점수를 출력하세요.
print(df.iloc[2, 0], df.iloc[0, 1], '\n')

# 주어진 데이터프레임을 점수를 기준으로 내림차순으로 정렬하세요.
print(df.sort_values(by='점수', ascending=False), '\n')

# 주어진 데이터프레임에서 점수가 85 이하인 학생을 삭제한 후 결과를 출력하세요.
df_drop = df.drop(df[df['점수'] <= 85].index)
print(df_drop, '\n')

# 각 학생의 점수에 대해 'A', 'B', 'C', 'D', 'F'로 학점을 매긴 새로운 열을 추가하세요.
# (A: 90 이상, B: 80-89, C: 70-79, D: 60-69, F: 60 이하)
df['학점'] = df['점수'].apply(
    lambda x: 'A' if x >= 90
    else 'B' if x >= 80
    else 'C' if x >= 70
    else 'D' if x >= 60
    else 'F')
print(df, '\n')

# 학생들의 점수에 대해 순위를 매기고, 동점일 경우 평균 순위를 부여하세요.
df['순위'] = df['점수'].rank(method='average', ascending=False)
print(df, '\n')

# 다음 데이터프레임을 사용하여 각 팀별 점수의 평균을 계산하세요.
data7 = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    '팀': ['A', 'A', 'B', 'B', 'A', 'B'],
    '점수': [85, 92, 78, 88, 95, 70]
}
df7 = pd.DataFrame(data7)
print(df7.groupby('팀')['점수'].mean(), '\n')

# 2024년 1월 1일부터 30일까지의 날짜를 생성하고, 해당 날짜의 주차(주 번호)를 출력하세요.
date = pd.to_datetime('2024년 1월 1일', format='%Y년 %m월 %d일')
date = pd.date_range(date, periods=30)
print(date)
week_numbers = date.isocalendar().week  # 주 번호 가져오기
print(date, week_numbers, '\n')