# manhattan distance
import random

vec_dim = 5
u = [random.randint(-5, 5) for _ in range(vec_dim)]
v = [random.randint(-5, 5) for _ in range(vec_dim)]
print(f"{u = }")
print(f"{v = }\n")

m_dist = 0
for u_el, v_el in zip(u, v):
    diff = u_el - v_el
    if diff > 0:
        m_dist += diff
    else:
        m_dist += -diff

print(f"{m_dist = }")