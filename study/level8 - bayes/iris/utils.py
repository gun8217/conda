import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    test_feature_value = test_data[:-1]
    iris_df = iris_df.drop(index=test_data_idx)
    
    xmaxes = iris_df.max(axis=0)
    xmins = iris_df.min(axis=0)
    
    return (feature_names, class_names), iris_df, test_feature_value, (xmaxes, xmins)


def cal_class_mean_std(iris_df, class_idx):
    class_data = iris_df[iris_df['class'] == class_idx].iloc[:, :-1]
    
    df_ = pd.DataFrame({
        'mean': class_data.mean(axis=0),
        'std': class_data.std(axis=0)
    })
    
    return df_
    

def draw_gaussian(axes, df_, xmaxes, xmins, feature_names):    
    for ax_idx, ax in enumerate(axes):
        mean = df_.iloc[ax_idx, 0]
        std = df_.iloc[ax_idx, 1]

        xmax, xmin = xmaxes.iloc[ax_idx], xmins.iloc[ax_idx]
        x = np.linspace(xmin, xmax, 100)
        y = gaussian_value(x, mean, std)
        
        ax.plot(x, y)
        ax.set_title(feature_names[ax_idx], fontsize=15)


def draw_sample(test_feature_value, axes, means, stds, class_names, class_idx):
    for ax_idx, ax in enumerate(axes):
        test_y_value = gaussian_value(test_feature_value.iloc[ax_idx], means.iloc[ax_idx], stds.iloc[ax_idx])
        ax.scatter(test_feature_value.iloc[ax_idx], test_y_value,
                    s=50, label=f'{class_names[class_idx]} - {test_y_value:.3f}')
        ax.legend()
        

def calculate_likelihoods(test_features, means, stds):
    likelihoods = np.ones(len(means))
    
    for i in range(len(means)):
        for j in range(len(test_features)):
            mean = means[i][j]
            std = stds[i][j]
            x = test_features[j]
            likelihoods[i] *= gaussian_value(x, mean, std)
    
    return likelihoods


if __name__ == '__main__':
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