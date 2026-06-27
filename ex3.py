import numpy as np

# exercice 3 : reshape et dimensions

# 1. tableau de 1 a 12
tableau = np.arange(1, 13)
print("tableau de base :", tableau)
print("forme :", tableau.shape)

# 2. transformer en matrice 3x4
m1 = tableau.reshape(3, 4)
print("matrice 3x4 :")
print(m1)
print("forme :", m1.shape)

# 3. transformer en matrice 2x6
m2 = tableau.reshape(2, 6)
print("matrice 2x6 :")
print(m2)
print("forme :", m2.shape)