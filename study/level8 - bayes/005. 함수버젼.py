import pandas as pd

def update_bayes_table(table, likelihood):
    if 'posterior' in table.columns:
        table['prior'] = table['posterior']
            
    table['likelihoods'] = likelihood    
    table['joint'] = table['prior'] * table['likelihoods']
    table['posterior'] = table['joint'] / table['joint'].sum()
    
    return table

data = {'prior': [0.3, 0.7]}
bayes_table = pd.DataFrame(data, index=['buy', 'no_buy'])

bayes_table = update_bayes_table(bayes_table, [0.9, 0.3])
print(f"First Update: \n{bayes_table}\n")

bayes_table = update_bayes_table(bayes_table, [0.7, 0.4])
print(f"Second Update: \n{bayes_table}")