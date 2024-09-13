from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    shuffle=True,
                                                    random_state=42)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)
train_acc = model.score(X_train, y_train)
print("train accuracy :", train_acc)

y_pred = model.predict(X_test)

test_acc = model.score(X_test, y_test)
print("test accuracy :", test_acc)

cm = confusion_matrix(y_test, y_pred)
print("confusion matrix :\n", cm)