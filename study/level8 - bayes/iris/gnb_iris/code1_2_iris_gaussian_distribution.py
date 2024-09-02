import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

from gaussian_distribution import gaussian_value

n_classes = 3

# 데이터 불러와서 정리
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
class_names = iris.target_names
# print(f"Shape X / y: {X.shape} / {y.shape}")
# print(f"feature names: {feature_names}\n")

data = np.hstack([X, y.reshape(-1, 1)])
iris_df = pd.DataFrame(data=data, columns=feature_names + ['class'])

xmaxes = iris_df.max(axis=0)
xmins = iris_df.min(axis=0)

# print(iris_df)

fig, axes = plt.subplots(len(feature_names), 1, figsize=(10, 15))

for class_idx in range(n_classes):
    class_df = iris_df[iris_df['class'] == class_idx].iloc[:, :-1]
    # print(class_df)
    means = class_df.mean(axis=0)
    stds = class_df.std(axis=0)

    df_ = pd.DataFrame({
        'mean': means,
        'std': stds
    })
    # print(df_)


    for ax_idx, ax in enumerate(axes):
        mean = df_.iloc[ax_idx, 0]
        std = df_.iloc[ax_idx, 1]

        xmax, xmin = xmaxes.iloc[ax_idx], xmins.iloc[ax_idx]
        x = np.linspace(xmin, xmax, 100)
        y = gaussian_value(x, mean, std)

        class_name = class_names[class_idx]
        ax.plot(x, y, label=f'{class_name}')



for ax_idx, ax in enumerate(axes):
    ax.set_title(feature_names[ax_idx], fontsize=20)
    ax.legend(fontsize=15)
fig.tight_layout()
plt.show()