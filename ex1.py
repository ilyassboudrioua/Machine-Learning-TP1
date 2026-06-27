import numpy as np

# exercice 1 : creer un tableau numpy simple

tableau = np.array([1, 2, 3, 4, 5])

# afficher le tableau d'abord pour verifier
print("mon tableau :", tableau)

# le type (c'est ndarray et pas list)
print("type :", type(tableau))

# ndim = combien de dimensions, ici c'est 1
print("dimension :", tableau.ndim)

# size = nombre total des elements dans le tableau
print("taille :", tableau.size)

# dtype = le type des valeurs (int64 par defaut)
print("type des donnees :", tableau.dtype)