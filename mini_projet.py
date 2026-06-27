import numpy as np

# mini projet : analyse des notes des etudiants

# etape 1 : creation de la matrice
# 10 etudiants, 5 modules, notes entre 0 et 20
np.random.seed(42)
notes = np.random.randint(0, 21, (10, 5))

print("matrice des notes (10 etudiants x 5 modules) :")
print(notes)

# etape 2 : statistiques 
# 1. moyenne de chaque etudiant (axis=1 : sur les colonnes)
moy_etudiants = np.mean(notes, axis=1)
print("moyenne par etudiant :")
for i, m in enumerate(moy_etudiants):
    print(f"  etudiant {i+1} : {round(m, 2)}")

# 2. moyenne de chaque module (axis=0 : sur les lignes)
moy_modules = np.mean(notes, axis=0)
print("moyenne par module :")
for i, m in enumerate(moy_modules):
    print(f"  module {i+1} : {round(m, 2)}")

# 3. meilleure note dans toute la matrice
print("meilleure note :", np.max(notes))

# 4. note la plus faible
print("note la plus faible :", np.min(notes))

# 5. etudiants admis (moyenne >= 10)
admis = np.where(moy_etudiants >= 10)[0] + 1
print("etudiants admis :", admis)

# 6. etudiants ajournes (moyenne < 10)
ajournes = np.where(moy_etudiants < 10)[0] + 1
print("etudiants ajournes :", ajournes)

# etape 3 : etudiants avec moyenne > 16
print("etudiants avec moyenne > 16 :")
for i, m in enumerate(moy_etudiants):
    if m > 16:
        print(f"  etudiant {i+1} : {round(m, 2)}")