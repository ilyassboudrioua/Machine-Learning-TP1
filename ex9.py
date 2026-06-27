import numpy as np

# exercice 9 : statistiques de base

# tableau aleatoire de 100 valeurs entre 0 et 100
np.random.seed(42)
tableau = np.random.randint(0, 101, 100)
print("tableau :", tableau)

print("moyenne :",  np.mean(tableau))
print("mediane :",  np.median(tableau))
print("variance :", np.var(tableau))
print("ecart-type :", np.std(tableau))
print("minimum :",  np.min(tableau))
print("maximum :",  np.max(tableau))