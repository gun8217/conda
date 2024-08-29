import pandas as pd

data = {
    'prior': [0.3, 0.7],
    'likelihoos': [0.9, 0.3]
}

df_data = pd.DataFrame(data, index=['buy', 'no_buy'])

df_data['joint'] = df_data['prior'] * df_data['likelihoos']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()
print(df_data)

df_data['prior'] = df_data['post']
df_data['likelihoos'] = [0.7, 0.4]
print(df_data)

df_data['joint'] = df_data['prior'] * df_data['likelihoos']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()
print(df_data)

print(df_data.shape[0], '\n')
print(df_data.columns[0], '\n')
print(df_data.values[0], '\n')
print(df_data[['joint', 'post']], '\n')
print(df_data['post'].sum(), '\n')
print(df_data['post'].unique())