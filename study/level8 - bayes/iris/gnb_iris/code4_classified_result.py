import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from gaussian_distribution import gaussian_value
from utils import make_iris_dataset, cal_class_mean_std, draw_gaussian, draw_sample

n_classes = 3
iris_df, (test_x, test_y), (xmaxes, xmins), (feature_names, class_names) = make_iris_dataset()

likelihoods = []
fig, axes = plt.subplots(len(feature_names), 1, figsize=(10, 15))
for class_idx in range(n_classes):
    df_ = cal_class_mean_std(iris_df, class_idx)
    draw_gaussian(axes, df_, xmaxes, xmins, class_names, class_idx)
    feature_likelihood = gaussian_value(test_x, df_['mean'], df_['std'])
    draw_sample(test_x, feature_likelihood, class_names, class_idx, axes)

    likelihood = feature_likelihood.prod()  ## feature들의 likelihood를 모두 곱함 -> 해당 클래스에서 데이터가 나올 likelihood
    likelihoods.append(likelihood)
# print(f"{feature_likelihood}")
# print(likelihoods)


# for ax, feature_name in zip(axes, feature_names):
#     ax.set_title(feature_name, fontsize=20)
# for ax in axes:
#     ax.legend()
#     ax.tick_params(labelsize=15)
#
#
#
classified_as = np.argmax(likelihoods)
result_df = pd.DataFrame(data=np.array(likelihoods).reshape(1, -1),
                         columns=list(class_names),
                         index=['likelihood'])
fig.suptitle(f"classified as {class_names[classified_as]}", fontsize=30)
fig.tight_layout()
plt.show()

print("RESULTS")
print(result_df)
print(f"---> classified as {class_names[classified_as]}")
