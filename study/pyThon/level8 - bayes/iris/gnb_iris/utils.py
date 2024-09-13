import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

from gaussian_distribution import gaussian_value


def make_iris_dataset():
    iris = load_iris()
    X, y = iris.data, iris.target
    feature_names = iris.feature_names
    class_names = iris.target_names

    data = np.hstack([X, y.reshape(-1, 1)])
    iris_df = pd.DataFrame(data=data, columns=feature_names + ['class'])

    test_data_idx = 0
    test_data = iris_df.iloc[test_data_idx]
    test_x, test_y = test_data.iloc[:-1], test_data.iloc[-1]

    iris_df = iris_df.drop(test_data_idx, axis=0)

    xmaxes = iris_df.max(axis=0)
    xmins = iris_df.min(axis=0)
    return iris_df, (test_x, test_y), (xmaxes, xmins), (feature_names, class_names)


def cal_class_mean_std(iris_df, class_idx):
    class_df = iris_df[iris_df['class'] == class_idx].iloc[:, :-1]

    means = class_df.mean(axis=0)
    stds = class_df.std(axis=0)

    df_ = pd.DataFrame({
        'mean': means,
        'std': stds
    })
    return df_


def draw_gaussian(axes, df_, xmaxes, xmins, class_names, class_idx):
    for ax_idx, ax in enumerate(axes):
        mean = df_.iloc[ax_idx, 0]
        std = df_.iloc[ax_idx, 1]

        xmax, xmin = xmaxes.iloc[ax_idx], xmins.iloc[ax_idx]
        x = np.linspace(xmin, xmax, 100)
        y = gaussian_value(x, mean, std)

        class_name = class_names[class_idx]
        ax.plot(x, y) ##### label 지움


def draw_sample(test_x, feature_likelihood, class_names, class_idx, axes):

    for ax_idx, ax in enumerate(axes):
        class_name = class_names[class_idx]
        li = feature_likelihood.iloc[ax_idx]
        x_ = test_x.iloc[ax_idx]
        ax.scatter(x_, li, s=100, label=f'{class_name} = {li:.3f}')
