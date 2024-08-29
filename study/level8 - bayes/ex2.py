import pandas as pd

data = {
    'prior': [0.05, 0.95],
    'positive': [0.9, 0.15]
}

df_data = pd.DataFrame(data, index=['has_virus', 'none_virus'])

df_data['joint'] = df_data['prior'] * df_data['positive']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()

negative = 1 - df_data['joint'].sum()
df_data['post_negative'] = 1 - df_data['joint'] / negative

print(f"양성 반응의 감염되었을 확률", df_data.loc['has_virus', 'post'])
print(f"음성 반응의 감염되지 않았을 확률", df_data.loc['none_virus', 'post_negative'])