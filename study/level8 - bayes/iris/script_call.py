import matplotlib.pyplot as plt

from utils import *


(feature_names, class_names), iris_df, test_feature_value, (xmaxes, xmins) = make_iris_dataset()

means = [cal_class_mean_std(iris_df, i)['mean'].values for i in range(len(class_names))]
stds = [cal_class_mean_std(iris_df, i)['std'].values for i in range(len(class_names))]

likelihoods = calculate_likelihoods(test_feature_value, means, stds)
print("Likelihoods:", likelihoods)

fig, axes = plt.subplots(len(feature_names), 1, figsize=(7, 9))

for class_idx in range(len(class_names)):
    df_ = cal_class_mean_std(iris_df, class_idx)
    
    draw_gaussian(axes, df_, xmaxes, xmins, feature_names)
    draw_sample(test_feature_value, axes, df_['mean'], df_['std'], class_names, class_idx)

fig.tight_layout()
plt.show()