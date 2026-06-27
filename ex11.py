import numpy as np

# exercice 11 : concatenation de matrices

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 1. concatenation horizontale (cote a cote, axis=1)
horiz = np.concatenate((A, B), axis=1)
print("concatenation horizontale :", horiz)

# 2. concatenation verticale (l'un en dessous de l'autre, axis=0)
vert = np.concatenate((A, B), axis=0)
print("concatenation verticale :", vert)