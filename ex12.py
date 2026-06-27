import numpy as np

# exercice 12 : tri et filtrage

np.random.seed(10)
arr = np.random.randint(0, 101, 20)
print("tableau original :", arr)

# 1. trier le tableau
trie = np.sort(arr)
print("tableau trie :", trie)

# 2. valeurs superieures a 50
sup50 = arr[arr > 50]
print("valeurs > 50 :", sup50)

# 3. indices des valeurs paires
# modulo 2 == 0 veut dire que c'est pair
indices_pairs = np.where(arr % 2 == 0)[0]
print("indices des valeurs paires :", indices_pairs)