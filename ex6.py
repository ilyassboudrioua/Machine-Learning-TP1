import numpy as np

# exercice 6 : fonctions math numpy

# tableau entre 0 et 10, 5 valeurs
tableau = np.linspace(0, 10, 5)
print("tableau :", tableau)

# sinus
print("sinus :", np.sin(tableau))

# cosinus
print("cosinus :", np.cos(tableau))

# exponentielle
print("exponentielle :", np.exp(tableau))

# logarithme (attention : log(0) donne -inf)
tableau2 = np.linspace(1, 10, 5)
print("logarithme :", np.log(tableau2))

# racine carree
print("racine carree :", np.sqrt(tableau))