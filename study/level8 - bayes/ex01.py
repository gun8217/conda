import pandas as pd


def updata_bayes_table(table, likelihood):
    table['joint'] = table['prior'] * likelihood
    table['post'] = table['joint'] / table['joint'].sum()
    
    table['prior'] = table['post']
    
    table['joint'] = table['prior'] * likelihood
    table['post'] = table['joint'] / table['joint'].sum()
    return table


data = {'prior': [0.3, 0.7]}
bayes_table = pd.DataFrame(data, index=['buy', 'no_buy'])

bayes_table = updata_bayes_table(bayes_table, [0.9, 0.3])
print(f"First Info: \n{bayes_table}\n")

bayes_table = updata_bayes_table(bayes_table, [0.7, 0.4])
print(f"Second Info: \n{bayes_table}\n")