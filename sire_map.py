import cProfile
import io


# s = 'a' * 10_000
# def f():
#     buffer = io.StringIO()
#     for _ in range(100_000):
#         buffer.write(s)
#     return buffer

# cProfile.run('f()')

def generer_sitemap_arbre(relations: dict[int, int]):
    buffer = io.StringIO()
    # stri = ''
    # buffer = []
    dp = {}
    for key in sorted(relations):
        parent = relations.get(key)
        if not parent:
            dp[key] = str(key)
        else:
            dp[key] = f'{dp[parent]} -> {key}'
        # stri += f'[{key}] {dp[key]}\n'
        buffer.write(f'[{key}] {dp[key]}\n')
        # buffer.append(f'[{key}] {dp[key]}\n')
    return buffer.getvalue()
    # return stri
    # return ''.join(buffer)

import time
import sys

# Augmentation de la limite de récursion au cas où tu choisis une approche récursive mémoïsée
sys.setrecursionlimit(1000)

print("Démarrage du test de haute performance...")

# Configuration du test lourd
NB_PAGES = 10000
gros_arbre = {}

# 1. On crée une branche ultra profonde (pire cas pour la remontée)
for i in range(1, 2000):
    gros_arbre[i] = i - 1  # 19999 -> 19998 -> ... -> 1 -> 0

# 2. On crée le reste de manière plus éclatée
for i in range(2000, NB_PAGES + 1):
    gros_arbre[i] = (i % 1000) + 1 # Parents dispatchés

print(f"Calcul sur {NB_PAGES} pages en cours...")

start = time.time()
mapping_final = generer_sitemap_arbre(gros_arbre)
end = time.time()

execution_time = end - start
print(f"Temps d'exécution : {execution_time:.4f} secondes.")

# Vérifications de sécurité
lines = mapping_final.strip().split('\n')
assert len(lines) == NB_PAGES, f"Nombre de lignes incorrect : {len(lines)}"
assert lines[0] == "[1] 1", f"Première ligne fausse : {lines[0]}"
assert lines[9] == "[10] 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10", "Le chemin profond est faux"

# Barrière de performance
assert execution_time < 0.5, f"Trop lent ({execution_time:.2f}s) ! Tu as un goulot d'étranglement dans ta logique d'arbre ou de chaîne."

print("Les tests ont réussis.")


