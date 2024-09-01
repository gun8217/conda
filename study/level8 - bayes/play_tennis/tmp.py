import pandas as pd
import numpy as np
from utils import bayesian_update, feature_likelihoods
file_path = 'C:/Users/Administrator/Documents/conda/study/level8 - bayes/play_tennis/play_tennis.csv'
dataset = pd.read_csv(file_path, index_col=0)
# print(dataset)

n_total_data = dataset.shape[0]
# unique = np.unique(dataset['play'], return_counts=True)
# n_total_yes = unique[1][1]
# n_total_no = unique[1][0]
n_total_yes = (dataset['play'] == 'Yes').sum()
n_total_no = (dataset['play'] == 'No').sum()

bayes_df = pd.DataFrame(
    {'prior': [n_total_yes / n_total_data,
               n_total_no / n_total_data]},
    index=['Yes', 'No']
)

outlook_likelihoods = feature_likelihoods(dataset, 'outlook')
temp_likelihoods = feature_likelihoods(dataset, 'temp')
humidity_likelihoods = feature_likelihoods(dataset, 'humidity')
wind_likelihoods = feature_likelihoods(dataset, 'wind')

# print(outlook_likelihoods)
# print(temp_likelihoods)
# print(humidity_likelihoods)
# print(wind_likelihoods)

print(bayesian_update(bayes_df, humidity_likelihoods['Normal']))
print(bayesian_update(bayes_df, temp_likelihoods['Mild']))
print(bayesian_update(bayes_df, wind_likelihoods['Weak']))
print(bayesian_update(bayes_df, outlook_likelihoods['Sunny']))