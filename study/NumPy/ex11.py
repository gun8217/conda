import numpy as np

n_student, n_class = 3, 4
m_score, M_score = 0, 100
scores = np.random.randint(low=m_score,
                           high=M_score,
                           size=(n_student, n_class))

# mean_class = np.sum(scores, axis=0, keepdims=True) / n_student
# mean_student = np.sum(scores, axis=1, keepdims=True) / n_class

mean_class = np.mean(scores, axis=0)
class_subt = scores - mean_class

mean_student = np.mean(scores, axis=1, keepdims=True)
student_subt = scores - mean_student

print(mean_class, class_subt)
print(class_subt.sum())
print()
print(mean_student, student_subt)
print(student_subt.sum())