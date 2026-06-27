import numpy as np
# exercice 10 : operations matricielles
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
# 1. addition matricielle
print("addition :", A + B)
# 2. produit matriciel (pas element par element)
print("produit matriciel :", np.dot(A, B))
# 3. transposee de A
print("transposee de A :", A.T)
# 4. determinant de A
print("determinant de A :", np.linalg.det(A))
# 5. valeurs propres de A
valeurs, vecteurs = np.linalg.eig(A)
print("valeurs propres :", valeurs)
# 6. inverse de A
print("inverse de A :", np.linalg.inv(A))