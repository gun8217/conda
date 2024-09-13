from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gaussian_value(x, mean, std):
    const = 1/np.sqrt(2*np.pi*std**2)

    numerator = (x - mean)**2
    denominator = (2 * std**2)
    exp_term = np.exp(-numerator/denominator)

    y = const * exp_term
    return y


iris = load_iris()
# print(type(iris))
# print([attr for attr in dir(iris) if not attr.startswith('__')], '\n')

# ['DESCR', 'data', 'data_module', 'feature_names', 'filename', 'frame', 'target', 'target_names']
# print("===============iris.data===============")
# print(f"type: {type(iris.data)}")
# print(iris.data[:10, :])
# print(f"shape: {iris.data.shape}")
# print(f"dtype: {iris.data.dtype}")
# print("===============iris.feature_names===============")
# print(f"type: {type(iris.feature_names)}")
# print(f"len: {len(iris.feature_names)}")
# print(iris.feature_names)
# print("===============iris.target===============")
# print(f"type: {type(iris.target)}")
# print(f"shape: {iris.target.shape}")
# print("head:", iris.target[:10])
# print("tail:", iris.target[-10:])
# print(f"dtype: {iris.target.dtype}")
# print("===============iris.target_names===============")
# print(f"type: {type(iris.target_names)}")
# print(f"type: {iris.target_names}")
# print(f"shape: {iris.target_names.shape}")
# print(f"dtype: {iris.target_names.dtype}")

X = iris.data; y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

data = np.hstack([X, y.reshape(-1, 1)])
iris_df = pd.DataFrame(data, columns=feature_names + ['class'])

xmaxes = iris_df.max(axis=0)
xmins = iris_df.min(axis=0)

test_data = iris_df.iloc[0]
test_data_features = test_data[:-1]
test_x, test_y = test_data.iloc[:-1], test_data.iloc[-1]
iris_df = iris_df.drop(index=0)
print(test_data_features)

fig, axes = plt.subplots(len(feature_names), 1, figsize=(7, 10))

for class_idx in range(len(class_names)):
    class_df = iris_df[iris_df['class'] == class_idx].iloc[:, :-1]
    
    data_df = pd.DataFrame({
        'mean' : class_df.mean(axis=0),
        'std' : class_df.std(axis=0)
    })

    for ax_idx, ax in enumerate(axes):
        x_range = np.linspace(xmins[feature_names[ax_idx]], xmaxes[feature_names[ax_idx]], 100)

        mean = data_df.loc[feature_names[ax_idx], 'mean']
        std = data_df.loc[feature_names[ax_idx], 'std']

        y_values = gaussian_value(x_range, mean, std)

        ax.plot(x_range, y_values)
        ax.set_title(feature_names[ax_idx])
        
        # # 1번째 data를 test data로 만들고,
        # # 해당 data는 기존 data에서 삭제 해 주고
        # # 해당 test data를 scatter으로 찍기
        # test_feature_value = test_data_features[ax_idx]
        # test_y_value = gaussian_value(test_feature_value, mean, std)
        # ax.scatter(test_feature_value, test_y_value,
        #            label=f'{class_names[class_idx]} - {test_y_value:.3f}')
        # ax.legend()

    feature_likelihood = gaussian_value(test_x, data_df['mean'],  data_df['std'])
    for ax_idx, ax in enumerate(axes):
        class_name = class_names[class_idx]
        li = feature_likelihood.iloc[ax_idx]
        x_ = test_x.iloc[ax_idx]
        ax.scatter(x_, li, s=100, label=f'{class_name} = {li:.3f}')
        ax.legend()
        
fig.tight_layout()
plt.show()