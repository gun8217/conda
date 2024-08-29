import pandas as pd

# 다음은 병원의 진단 데이터입니다. 특정 질병에 대한 진단 결과를 평가하기 위해 다음과 같은 정보를 가지고 있습니다:

# 병원 A는 전체 환자의 40%를 진단하며, 이 병원에서 특정 질병이 발견될 확률은 5%입니다.
# 병원 B는 전체 환자의 60%를 진단하며, 이 병원에서 특정 질병이 발견될 확률은 10%입니다.
# 만약 환자가 병원 B에서 진단을 받았다면, 그 환자가 실제로 질병을 가질 확률이 70%입니다.
# 만약 환자가 병원 A에서 진단을 받았다면, 그 환자가 실제로 질병을 가질 확률이 50%입니다.

# 위 정보를 바탕으로 다음 질문에 답하십시오:

# 1. 환자가 질병을 가지고 있을 확률과 질병이 없는 확률을 구하십시오.
# 2. 환자가 질병을 가졌을 때, 병원 B에서 진단을 받을 확률을 구하십시오.
# 3. 병원 A에서 질병이 발견되었을 때, 환자가 실제로 질병을 가지고 있을 확률을 구하십시오.

data = {
    'prior': [0.4, 0.6],
    'disease': [0.5, 0.7],
    'special_disease': [0.05, 0.1]
}

df_data = pd.DataFrame(data, index=['hospital_A', 'hospital_B'])

df_data['joint'] = df_data['prior'] * df_data['disease']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()
print(df_data, '\n')

total_disease = df_data['post'].sum() / len(data['disease'])
total_no_disease = 1 - total_disease

print(f"total disease", total_disease)
print(f"total no disease", total_no_disease)
print(f"disease_B = ", df_data.loc['hospital_B', 'post'])
print(f"disease_A = ", df_data.loc['hospital_A', 'post'])