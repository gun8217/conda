from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

from utils import *


# 데이터 준비
natural, data, le_disaster, le_damage = dataLoad()

# 데이터 분할
X, X_train, X_test, y_train, y_test = dataSplit(data)

# 모델 훈련 학습 및 결과
desition_gini = modelAccPred(DecisionTreeClassifier(random_state=42), data)


# 폰트 경로 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()

# 피처 이름과 클래스 이름을 문자열로 변환
feature_names = [str(name) for name in X.columns]
class_names = [str(label) for label in le_damage.classes_]

# 결정 트리 시각화
plt.figure(figsize=(7, 4), dpi=300)
plot_tree(desition_gini, feature_names=feature_names, class_names=class_names, filled=True)
plt.savefig('C:/Users/Administrator/Documents/conda/test/modeling/dicition_gini.png')
plt.tight_layout()
plt.show()