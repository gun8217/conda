# groupby: 특정 기준에 따라 데이터 그룹화
# 집계: 그룹별 평균, 합계, 개수 등의 통계 계산
# 다양한 연산: 여러 집계 함수를 동시에 적용 가능

import pandas as pd

data = {
    '팀': ['A', 'A', 'B', 'B', 'C', 'C'],
    '점수': [90, 80, 70, 60, 50, 40],
}
df = pd.DataFrame(data)
print(df)
print()

groupby_mean = df.groupby('팀')['점수'].mean()
print(f"{groupby_mean = }\n")

groupby_sum = df.groupby('팀')['점수'].sum()
print(f"{groupby_sum = }\n")

groupby_agg = df.groupby('팀')['점수'].agg(['mean', 'sum', 'count', 'median'])
print(f"{groupby_agg = }\n")