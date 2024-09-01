# 바 차트 (Bar Chart)

import matplotlib.pyplot as plt

# 데이터 생성
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

# 바 차트 그리기
plt.bar(categories, values, color='purple', edgecolor='black')
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True)
plt.show()