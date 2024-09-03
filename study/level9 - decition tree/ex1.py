import numpy as np

P1 = np.array([3/4, 1/4])
P2 = np.array([1/2, 1/2])
P3 = np.array([1/2, 1/4, 1/4])
P4 = np.array([1/3, 1/3, 1/3])
P5 = np.array([1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12])
H1 = np.sum(-P1 * np.log2(P1))
H2 = np.sum(-P2 * np.log2(P2))
H3 = np.sum(-P3 * np.log2(P3))
H4 = np.sum(-P4 * np.log2(P4))
H5 = np.sum(-P5 * np.log2(P5))
print('\n',H1,'\n',H2,'\n',H3,'\n',H4,'\n',H5,'\n')