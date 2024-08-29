import pandas as pd

data = {
    'prior': [0.3, 0.7],
    'defect': [0.08, 0.12],
    'positive': [0.08, 0.12]
}

df_data = pd.DataFrame(data, index=['company_A', 'company_B', 'company_C'])

df_data['joint'] = df_data['prior'] * df_data['defect']
total_defect = df_data['joint'].sum()
df_data['post'] = df_data['joint'] / total_defect

print(f"전체 결함이 있을 확률", total_defect)
print(f"결함 판명시 C 업체일 확률", df_data.loc['company_C', 'post'])