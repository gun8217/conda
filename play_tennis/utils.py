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


# def feature_likelihoods(dataset, feature_names, play_col='play', index_values=None):
#     if play_col not in dataset.columns:
#         raise KeyError(f"Column '{play_col}' does not exist in the dataset.")
    
#     if index_values is None:
#         index_values = dataset[play_col].unique()
    
#     likelihoods_dict = {}
    
#     for feature_name in feature_names:
#         if feature_name not in dataset.columns:
#             raise KeyError(f"Feature column '{feature_name}' does not exist in the dataset.")
        
#         data = dataset[[feature_name, play_col]]
#         states = data[feature_name].unique()
        
#         total_counts = {val: (data[play_col] == val).sum() for val in index_values}
        
#         feature_likelihoods = {}
        
#         for state in states:
#             state_data = data[data[feature_name] == state]
            
#             likelihoods = []
#             for val in index_values:
#                 n_class = (state_data[play_col] == val).sum()
#                 total_count = total_counts[val]
#                 likelihood = n_class / total_count if total_count > 0 else 0
#                 likelihoods.append(likelihood)
            
#             feature_likelihoods[state] = likelihoods
        
#         feature_df = pd.DataFrame(feature_likelihoods, index=index_values)
#         feature_df.columns.name = feature_name
#         likelihoods_dict[feature_name] = feature_df
    
#     return likelihoods_dict


if __name__ == '__main__':
    file_path = 'C:/Users/Administrator/Documents/conda/play_tennis/play_tennis.csv'
    dataset = pd.read_csv(file_path, index_col=0)
    
    # likelihoods = feature_likelihoods(dataset, feature_names=['outlook', 'temp', 'humidity', 'wind'], play_col='play')
    # for feature, df in likelihoods.items():
    #     print(f"Feature: {feature}")
    #     print(df)
    #     print()