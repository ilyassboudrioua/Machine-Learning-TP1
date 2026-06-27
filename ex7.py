import numpy as np
import time as ti

# exercice 7 : comparaison python vs numpy

# version python avec boucle
liste1 = list(range(1000000))
liste2 = list(range(1000000))

debut = ti.time()
resultat = [liste1[i] + liste2[i] for i in range(len(liste1))]
fin = ti.time()
print("temps python (boucle) :", round(fin - debut, 4), "sec")

# version numpy
arr1 = np.arange(1000000)
arr2 = np.arange(1000000)
debut2 = ti.time()
resultat2 = arr1 + arr2
fin2 = ti.time()
print("temps numpy :", round(fin2 - debut2, 4), "sec")
# numpy est beaucoup plus rapide car il utilise du C en interne