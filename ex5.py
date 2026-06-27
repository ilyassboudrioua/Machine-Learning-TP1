import numpy as np

# exercice 5 : operations de base entre deux tableaux

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# 1. addition
print("addition :", A + B)

# 2. soustraction
print("soustraction :", A - B)

# 3. multiplication element par element
print("multiplication :", A * B)

# 4. division
print("division :", A / B)

# 5. produit scalaire (dot product)
print("produit scalaire :", np.dot(A, B))