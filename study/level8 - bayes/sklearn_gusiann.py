from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import pandas as pd

file_path = 'C:/Users/Administrator/Documents/conda/study/level8 - bayes/Iris.csv'
iris = pd.read_csv(file_path, index_col=0)

X = iris[iris.columns[:-1]]
y = iris[iris.columns[-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    shuffle=True,
                                                    random_state=42)

model = GaussianNB()

model.fit(X_train, y_train)
train_acc = model.score(X_train, y_train)
print("train accuracy :", train_acc)

y_pred = model.predict(X_test)

test_acc = model.score(X_test, y_test)
print("test accuracy :", test_acc)

cm = confusion_matrix(y_test, y_pred)
print(f"confusion matrix: {cm}")


# # kaggle - dataset
# # 공공데이터포털