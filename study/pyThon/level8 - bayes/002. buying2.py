import pandas as pd

data = {
    'prior': [0.56, 0.44],
    'likelihoods': [0.7, 0.4]
}

df_data = pd.DataFrame(data, index=['buy', 'no_buy'])

df_data['joint'] = df_data['prior'] * df_data['likelihoods']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()
print(df_data, '\n')

print(f"buy = {df_data.loc['buy', 'post']}")
print(f"no_buy = {df_data.loc['no_buy', 'post']}")