import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from utils import *

iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
class_names = iris.target_names

data = np.hstack([X, y.reshape(-1, 1)])
iris_data = pd.DataFrame(data=data, columns=feature_names + ['class'])

test_data = iris_data.iloc[0]
test_data_features = test_data[:-1]
iris_data = iris_data.drop(index=0)

xmaxes = iris_data.max(axis=0)
xmins = iris_data.min(axis=0)

fig, axse = plt.subplots(len(feature_names), 1, figsize=(5, 7))

for class_idx in range(len(class_names)):
    class_data = iris_data[iris_data['class'] == class_idx].iloc[:, :-1]

    data_df = pd.DataFrame({
        'mean' : class_data.mean(axis=0),
        'std' : class_data.std(axis=0, ddof=1)
    })
    
    for ax_idx, ax in enumerate(axse):
        mean = data_df.iloc[ax_idx, 0]
        std = data_df.iloc[ax_idx, 1]

        xmax, xmin = xmaxes.iloc[ax_idx], xmins.iloc[ax_idx]
        x = np.linspace(xmin, xmax, 100)
        y = gaussian_value(x, mean, std)

        class_name = class_names[class_idx]
        ax.plot(x, y)
        ax.set_title(feature_names[ax_idx], fontsize=15)

        test_feature_value = test_data_features[ax_idx]
        test_y_value = gaussian_value(test_feature_value, mean, std)
        ax.scatter(test_feature_value, test_y_value,
                    label=f'{class_name[class_idx]} - {test_y_value:.3f}')
        ax.legend()

fig.tight_layout()
plt.show()