import pandas as pd

data = {
    'prior': [0.3, 0.7],
    'likeli': [0.5, 0.5],
    'likeli2': [0.7, 0.3],
    'likeli3': [0.7, 0.3]
}

df_data = pd.DataFrame(data, index=['buy', 'no_buy'])

n_likelis = len([key for key in data.keys() if key.startswith('likeli')])

df_data['joint'] = df_data['prior'] * df_data['likeli']
df_data['post'] = df_data['joint'] / df_data['joint'].sum()

for i in range(2, n_likelis + 1):
    likeli_col = f'likeli{i}'
    if likeli_col in df_data.columns:
        df_data[f'joint{i}'] = df_data['post'] * df_data[likeli_col]
        df_data[f'post{i}'] = df_data[f'joint{i}'] / df_data[f'joint{i}'].sum()
print(df_data, '\n')

final_post_col = f'post{n_likelis}'
print(f"buying to bought : {df_data.loc['buy', final_post_col]:.4f}")