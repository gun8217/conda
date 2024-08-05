datas = [10, 20, 30, 40, 50]
predictions = [12, 18, 33, 37, 45]


###### 제곱 오차 : 통계와 기계 학습에서 모델의 성능 평가(정량적 평가)
# Squared Error 계산 : 실제값과 예측값의 오차를 제곱한다.(양수를 얻기 위해)
squared_errors = [(d - p)**2 for d, p in zip(datas, predictions)]
print(f"{squared_errors = }")


###### 제곱 오차의 평균(MSE) : Squared Error의 평균값(모델 성능 평가)
mse = sum(squared_errors) / len(datas)
print(f"{mse = }")