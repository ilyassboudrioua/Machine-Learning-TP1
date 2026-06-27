import numpy as np

# exercice 4 : indexation et slicing

A = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])
print("matrice A :")
print(A)

# 1. afficher la premiere ligne (index 0)
print("premiere ligne :", A[0])

# 2. afficher la deuxieme colonne (index 1)
# le : veut dire toutes les lignes
print("deuxieme colonne :", A[:, 1])

# 3. elements centraux : lignes 0 et 1, colonnes 1 et 2
print("elements centraux :")
print(A[0:2, 1:3])

# 4. modifier la valeur 7 par 100
# 7 est en ligne 1, colonne 2
A[1, 2] = 100
print("matrice apres modification :")
print(A)