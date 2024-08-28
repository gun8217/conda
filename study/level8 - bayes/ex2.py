import pandas as pd

# 주어진 데이터
data = {
    'prior': [0.4, 0.6],  # 병원 A와 B가 각각 진단하는 환자 비율
    'special_disease': [0.05, 0.1],  # 병원 A와 B에서 질병 발견 확률
    'disease_given_special_disease': [0.5, 0.7]  # 질병을 가진 환자가 특수 질병으로 진단될 확률
}

df_data = pd.DataFrame(data, index=['hospital_A', 'hospital_B'])

# 전체 질병 발견 확률 (P(Disease)) 계산
# 각 병원에서 질병이 발견될 확률을 고려하여 전체적으로 가중 평균 계산
df_data['P(Special Disease)'] = df_data['special_disease'] * df_data['prior']
total_special_disease = df_data['P(Special Disease)'].sum()

# 질병을 가진 환자의 비율 (P(Disease))
df_data['P(Disease and Special Disease)'] = df_data['special_disease'] * df_data['disease_given_special_disease'] * df_data['prior']
total_disease = df_data['P(Disease and Special Disease)'].sum()
total_disease_probability = total_disease / total_special_disease

# 전체 질병 없음 확률
total_no_disease_probability = 1 - total_disease_probability

# 병원 B에서 질병이 발견되었을 때, 질병을 가진 확률 (P(Disease | Hospital B))
p_disease_given_hospital_B = (df_data.loc['hospital_B', 'special_disease'] * df_data.loc['hospital_B', 'disease_given_special_disease']) / total_disease_probability

# 병원 A에서 질병이 발견되었을 때, 질병을 가진 확률 (P(Disease | Hospital A))
p_disease_given_hospital_A = (df_data.loc['hospital_A', 'special_disease'] * df_data.loc['hospital_A', 'disease_given_special_disease']) / total_disease_probability

print(f"Total Disease Probability: {total_disease_probability:.2f}")
print(f"Total No Disease Probability: {total_no_disease_probability:.2f}")
print(f"P(Disease | Hospital B): {p_disease_given_hospital_B:.2f}")
print(f"P(Disease | Hospital A): {p_disease_given_hospital_A:.2f}")