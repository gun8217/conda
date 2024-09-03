import math # 단일 값 계산, 입력이 스칼라일 때 사용
import numpy as np  # 배열 로그 계산, 벡터화된 연산 지원, 데이터가 배열 형태일 때 사용

## math
# 자연 로그 (base e)
x = 10
natural_log = math.log(x)
print(f"Natural log of {x}: {natural_log}")

# 상용 로그 (base 10)
log10_value = math.log10(x)
print(f"Log base 10 of {x}: {log10_value}")

# 이진 로그 (base 2)
log2_value = math.log2(x)
print(f"Log base 2 of {x}: {log2_value}")

# 사용자 정의 base의 로그
base = 3
custom_log = math.log(x, base)
print(f"Log base {base} of {x}: {custom_log}")

## numpy
# 자연 로그 (base e)
x = np.array([1, 10, 100])
natural_log = np.log(x)
print(f"Natural log of {x}: {natural_log}")

# 상용 로그 (base 10)
log10_value = np.log10(x)
print(f"Log base 10 of {x}: {log10_value}")

# 이진 로그 (base 2)
log2_value = np.log2(x)
print(f"Log base 2 of {x}: {log2_value}")