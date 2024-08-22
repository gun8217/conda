import numpy as np

n_test_time, n_student, n_class = 4, 3, 4
m_score, M_score = 0, 100
scores = np.random.randint(low=m_score,
                           high=M_score,
                           size=(n_test_time,
                                 n_student,
                                 n_class))

mean_time = np.mean(scores, axis=0) #(n_student, n_class)
mean_student = np.mean(scores, axis=1) #(n_test_time, n_class)
mean_class = np.mean(scores, axis=2) #(n_test_time, n_student)

print("각 회차의 학급별 학생 평균: {}\n{}".format(mean_time.shape, mean_time), '\n')
print("각 학생의 회차별 학급 평균: {}\n{}".format(mean_student.shape, mean_student), '\n')
print("각 학급의 회차별 학생 평균: {}\n{}".format(mean_class.shape, mean_class))