import numpy as np

# exercice 2 : creation de differentes matrices

# 1. matrice 3x3 remplie de zeros
m1 = np.zeros((3, 3))
print("matrice de zeros 3x3 :")
print(m1)

# 2. matrice 4x4 remplie de uns
m2 = np.ones((4, 4))
print("matrice de uns 4x4 :")
print(m2)

# 3. matrice identite 5x5 (diagonale = 1, reste = 0)
m3 = np.eye(5)
print("matrice identite 5x5 :")
print(m3)

# 4. matrice avec les nombres de 1 a 20
# j'utilise arange puis reshape pour avoir une matrice
m4 = np.arange(1, 21).reshape(4, 5)
print("matrice 1 a 20 (4x5) :")
print(m4)