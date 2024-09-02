import matplotlib.pyplot as plt

from gaussian_distribution import gaussian_value
from utils import make_iris_dataset, cal_class_mean_std, draw_gaussian, draw_sample

n_classes = 3
iris_df, (test_x, test_y), (xmaxes, xmins), (feature_names, class_names) = make_iris_dataset()

fig, axes = plt.subplots(len(feature_names), 1, figsize=(10, 15))
for class_idx in range(n_classes):
    df_ = cal_class_mean_std(iris_df, class_idx)
    draw_gaussian(axes, df_, xmaxes, xmins, class_names, class_idx)
    feature_likelihood = gaussian_value(test_x, df_['mean'], df_['std'])
    draw_sample(test_x, feature_likelihood, class_names, class_idx, axes)



for ax_idx, ax in enumerate(axes):
    ax.set_title(feature_names[ax_idx], fontsize=20)
    ax.legend(fontsize=15)
fig.tight_layout()
plt.show()