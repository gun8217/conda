###### 스칼라 곱
vector = [1, 2, 3]
scalar = 5
result = [scalar * v for v in vector]
print(f"{result = }")


###### Dot Product & Hadamard Product
vector_a, vector_b = [1, 2, 3], [4, 5, 6]

# Dot Product(내적) : 곱해서 더한다(유사도 측정시 사용)
dot_prod = sum(a * b for a, b in zip(vector_a, vector_b))
print(f"{dot_prod = }")

# Hadamard Product : 요소별 곱
hadamard_prod = [a * b for a, b in zip(vector_a, vector_b)]
print(f"{hadamard_prod = }")