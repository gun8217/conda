import pandas as pd

customer_data = {
    'prior_probs' : [0.3, 0.7],
    'likelihoods' : [0.7, 0.4]
}

customer_df = pd.DataFrame(customer_data,
                           index=['buying', 'not_buying'])
# # 사전 확률
# print(customer_df['prior_probs'])
# # 현상
# print(customer_df['likelihoods'])
# # joint prob(교집합)
# print(customer_df['prior_probs'] * customer_df['prior_probs'])

customer_df['joint'] = customer_df['prior_probs'] * customer_df['prior_probs']
customer_df['post'] = customer_df['joint'] / customer_df['joint'].sum()
print(customer_df)

print(f"buying : ", customer_df.loc['buying', 'post'])
print(f"not_buying : ", customer_df.loc['not_buying', 'post'])