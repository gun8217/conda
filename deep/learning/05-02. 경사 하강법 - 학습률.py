# 𝑓(𝑥)=2𝑥**2 함수 정의
def f(x): return 2 * x ** 2

# 𝑑𝑓/𝑑𝑥=4𝑥 도함수 정의
def df_dx(x): return 4 * x

x = 3
ITERATIONS = 5
# 학습률(Learning Rate)을 0.1로 설정
LR = 0.1

# 각각의 반복 단계에서 𝑥 값과 함수 값을 추적하기 위해 초기 값을 설정
x_track, y_track = [x], [f(x)]

print(f"Initial x: {x}")

for iter in range(ITERATIONS):
    dy_dx = df_dx(x)
    
    # 학습률 𝐿𝑅을 곱한 기울기를 현재 𝑥 값에서 빼서 𝑥 값을 업데이트
    x = x - LR * dy_dx
    
    x_track.append(x)
    y_track.append(f(x))
    print(f"{iter + 1}-th Iteration")
    print(f"adjusted dy_dx{LR * dy_dx:.4f}")
    print(f"next x: {x:.4f}\n")