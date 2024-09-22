# axis: 순위를 매길 축. 기본값은 0(행 방향)
# method: 순위를 매기는 방법
# 'average': 동점인 값의 평균 순위
# 'min': 동점인 값에 작은 순위
# 'max': 동점인 값에 큰 순위
# 'first': 동점인 값에 먼저 순위
# 'dense': 동점인 값에 같은 순위, 다음 순위 건너뜀
# ascending: False(랭킹 1 = 큰 값)

import pandas as pd

data = {
    # 'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [88, 92, 88, 90, 95],
    'Science': [90, 85, 85, 92, 87],
    'English': [85, 80, 88, 91, 89]
}
df = pd.DataFrame(data, index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
# df = pd.DataFrame(data)
# df.set_index('Student', inplace=True)
print(df)
print()

# 각 과목별로 순위 매기기
min_math_ = df['Math'].rank(method='min', ascending=False)
print(f"{min_math_ = }\n")
max_science = df['Science'].rank(method='max', ascending=False)
print(f"{max_science = }\n")

# 동점 처리 방법을 'average'로 설정하여 순위 매기기
average = df[['Math', 'Science', 'English']].rank(method='average', ascending=False)
print(average)