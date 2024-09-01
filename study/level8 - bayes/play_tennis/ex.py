import pandas as pd

data = {
    'prior' : [0.3, 0.7],
    'likelihoods' : [0.08, 0.12]
}

data_df = pd.DataFrame(data, index=['hos_X', 'hos_Y'])

data_df['joint'] = data_df['prior'] * data_df['likelihoods']
n_has_total = data_df['joint'].sum()
n_none_total = 1 - n_has_total
data_df['posterior'] = data_df['joint'] / n_has_total
print(data_df, '\n')

data_df['prior'] = data_df['posterior']
data_df['likelihoods'] = [0.85, 0.9]
data_df['likelihoods_none'] = [0.1, 0.05]

data_df['joint'] = data_df['prior'] * data_df['likelihoods']
n_has_total_positive = data_df['joint'].sum()
data_df['posterior'] = data_df['joint'] / n_has_total_positive

data_df['joint_none'] = data_df['prior'] * data_df['likelihoods_none']
data_df['posterior_none'] = data_df['joint_none'] / data_df['joint_none'].sum()
print(data_df, '\n')

print(f"양성 결과를 받은 환자가 실제로 질병을 가질 확률 : ",
      n_has_total_positive)
print(f"양성 결과를 받은 환자가 병원 X에서 진단을 받았을 확률 : ",
      data_df.loc['hos_X', 'posterior'])