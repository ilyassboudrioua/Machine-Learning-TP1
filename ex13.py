import numpy as np

# exercice 13 : normalisation min-max

# notes des etudiants
notes = np.array([12, 8, 15, 6, 18, 10, 14, 9, 17, 11])
print("notes originales :", notes)

# formule min-max : (x - min) / (max - min)
notes_norm = (notes - notes.min()) / (notes.max() - notes.min())

print("notes normalisees :", notes_norm.round(2))
print("min apres normalisation :", notes_norm.min())
print("max apres normalisation :", notes_norm.max())