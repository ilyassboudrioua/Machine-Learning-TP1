import numpy as np

# exercice 14 : simulation de temperatures sur 365 jours

np.random.seed(14)

# distribution normale : moyenne=25, ecart-type=5
temperatures = np.random.normal(loc=25, scale=5, size=365)

# 1. temperature moyenne annuelle
print("moyenne annuelle :", round(np.mean(temperatures), 2), "C")

# 2. jours ou la temp depasse 30
jours_chauds = np.sum(temperatures > 30)
print("nombre de jours > 30 C :", jours_chauds)

# 3. jours ou la temp est en dessous de 15
jours_froids = np.sum(temperatures < 15)
print("nombre de jours < 15 C :", jours_froids)