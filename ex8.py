import numpy as np

# exercice 8 : broadcasting numpy

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([10, 20, 30])

# numpy ajoute B a chaque ligne de A automatiquement
resultat = A + B

print("matrice A :")
print(A)
print("vecteur B :", B)
print("resultat A + B :")
print(resultat)