import pandas as pd

data = {
    'prior': [1/3, 2/3],
    'likelihoods': [0.1, 0.15]
}

df_data = pd.DataFrame(data, index=['fac_a', 'fac_b'])

df_data['joint'] = df_data['prior'] * df_data['likelihoods']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()
print(df_data, '\n')

print(f"fac_a 불량품 확률 = {df_data.loc['fac_a', 'post']}")
print(f"fac_b 불량품 확률 = {df_data.loc['fac_b', 'post']}")