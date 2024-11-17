# 𝑓(𝑥)=1/10𝑥**2 함수 정의
def f(x): return 1/10 * x**2

# 𝑑𝑓/𝑑𝑥=(1/5)𝑥 도함수 정의
def df_dx(x): return 1/5 * x

# 초깃값 x를 3으로 설정
x = 3

# 총 20번의 update를 할 것
ITERATIONS = 20

print(f"Initial x: {x}")

# ITERATIONS 변수에 설정된 값(20회)만큼 반복
for iter in range(ITERATIONS):
    # 현재 𝑥 값에서 함수 𝑓(𝑥)의 도함수 𝑑𝑓/𝑑𝑥 값 계산 : 현재 위치 기울기(변화율)
    dy_dx = df_dx(x)
    # 경사 하강법의 핵심 부분 : 현재 기울기 값을 빼서 𝑥 값을 업데이트
    x = x - dy_dx
    print(f"{iter + 1}-th x: {x:.4f}")