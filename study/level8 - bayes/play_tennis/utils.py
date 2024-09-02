import numpy as np
import pandas as pd


def bayesian_update(table, likelihood):
    if 'posterior' in table.columns:
        table['prior'] = table['posterior']
            
    table['likelihoods'] = likelihood    
    table['joint'] = table['prior'] * table['likelihoods']
    table['posterior'] = table['joint'] / table['joint'].sum()
    
    return table


def feature_likelihoods(dataset, feature_name):
    data = dataset[[feature_name, 'play']]
    states = data[feature_name].unique()
    
    n_total_yes = (data['play'] == 'Yes').sum()
    n_total_no = (data['play'] == 'No').sum()
    
    likelihoods_df = pd.DataFrame(index=['Yes', 'No'])
    
    for state in states:
        state_data = data[data[feature_name] == state]
        
        n_yes = (state_data['play'] == 'Yes').sum()
        n_no = (state_data['play'] == 'No').sum()
        
        likelihoods_yes = n_yes / n_total_yes
        likelihoods_no = n_no / n_total_no
        likelihoods_df[state] = [likelihoods_yes, likelihoods_no]
        
    return likelihoods_df


# if __name__ == '__main__':
#     file_path = 'C:/Users/user/Documents/conda/study/level8 - bayes/play_tennis/play_tennis.csv'
#     dataset = pd.read_csv(file_path, index_col=0)
    
#     likelihoods = feature_likelihoods(dataset, feature_names=['outlook', 'temp', 'humidity', 'wind'], play_col='play')
#     for feature, df in likelihoods.items():
#         print(f"Feature: {feature}")
#         print(df)
#         print()