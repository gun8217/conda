import numpy as np

# Binary Cross Entropy 손실을 계산하기 위한 클래스
class BCELoss:
    # 손실 값 계산 : y는 실제 값 (0 또는 1)이고, pred는 모델이 예측한 확률 값
    def forward(self, y, pred):
        # 입력값 저장
        self.y, self.pred = y, pred
        # BCE 손실 계산
        J = -(y * np.log(pred) + (1 - y)*np.log(1 - pred))
        return J
    
    # 손실 변화율(그라디언트) 계산
    def backward(self):
        # 손실 함수의 그라디언트 계산
        # BCE 그라디언트 : (pred - y) / (pred * (1 - pred))
        # 이 때 pred는 예측 확률, y는 실제값
        dJ_dpred = (self.pred - self.y) / (self.pred * (1 - self.pred))
        return dJ_dpred


# 예제 데이터
y_true = np.array([1, 0, 1, 0]) # 실제 값 (0 또는 1)
y_pred = np.array([0.9, 0.1, 0.8, 0.3]) # 모델의 예측 값 (0과 1 사이의 확률)

# BCELoss 클래스 인스턴스 생성
loss = BCELoss()

# Forward 계산 (손실 값 계산)
loss_value = loss.forward(y_true, y_pred)
print("BCE 손실:", loss_value)

# Backward 계산 (손실 변화율/그라디언트 계산)
gradient = loss.backward()
print("BCE 손실 변화율:", gradient)