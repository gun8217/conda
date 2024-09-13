import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 준비
file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/disaster/natural.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')

# 데이터 전처리
datas = dataset.copy()
datas = datas.drop(columns=['시작시간', '종료기간', '데이터기준일자'])

# 고유 중심기압 값과 클래스 개수 정의
class_unique = np.unique(datas['중심기압(hPa)'])
n_class = len(class_unique)
cmap = plt.get_cmap('tab10')  # 명확한 색상을 제공하는 컬러맵
colors = [cmap(i) for i in range(min(n_class, 25))]  # 최대 10개의 색상

# 입력 데이터 설정
test_data = datas[['순간최대풍속', '일최대강우량(mm)']].iloc[0].values  # 테스트 데이터는 첫 번째 행을 사용

# 각 클래스별 데이터 수집
X_list = []
y_list = []
for i in range(n_class):
    X_ = datas[['순간최대풍속', '일최대강우량(mm)']].values
    X_list.append(X_)
    y_list.append(np.full(len(X_), i))

# 배열 변환
X = np.vstack(X_list)
y = np.hstack(y_list)

# 유클리드 거리 계산
euc_dist = np.sqrt(np.sum((X - test_data)**2, axis=1))
argsort = np.argsort(euc_dist)
select_dist = argsort[:1]
class_ = y[select_dist]
class_xs = X[select_dist]
class_m = np.unique(class_, return_counts=True)
argmax_idx = np.argmax(class_m[1])
final_idx = class_m[0][argmax_idx]

# 시각화
fig, ax = plt.subplots(figsize=(8, 8))
for i in range(n_class):
    ax.scatter(X[y == i][:, 0], X[y == i][:, 1],
               color=colors[i % len(colors)], alpha=0.6, s=50)  # 색상 지정

# 테스트 데이터 플롯
ax.scatter(test_data[0], test_data[1],
           color=colors[final_idx % len(colors)], marker='*', linewidth=2, s=150)

# K개의 이웃에 대한 선 그리기
for i in range(1):
    ax.plot([test_data[0], class_xs[i][0]],
            [test_data[1], class_xs[i][1]],
            color='gray', linestyle='--')

# 메쉬그리드 생성
x_lim, y_lim = ax.get_xlim(), ax.get_ylim()
x1 = np.linspace(x_lim[0], x_lim[1], 100)
y1 = np.linspace(y_lim[0], y_lim[1], 100)
X1, Y1 = np.meshgrid(x1, y1)
X_db = np.hstack([X1.reshape(-1, 1), Y1.reshape(-1, 1)])

# 예측 클래스 계산
preds = []
for x_db in X_db:
    dist = np.sqrt(np.sum((X - x_db)**2, axis=1))  # 유클리드 거리 계산
    dist_sort = np.argsort(dist)
    near_idx = dist_sort[:1]
    near_class = y[near_idx]
    
    unique, count = np.unique(near_class, return_counts=True)
    pred = unique[np.argmax(count)]
    preds.append(pred)

preds = np.array(preds)

# 메쉬그리드 시각화
for idx in range(n_class):
    X_ = X_db[preds == idx]
    ax.scatter(X_[:, 0], X_[:, 1], color=colors[idx % len(colors)], alpha=0.1)  # 색상 지정

fig.tight_layout()
plt.show()
