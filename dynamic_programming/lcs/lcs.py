# O(2^(n + m))
from functools import cache
import sys
sys.setrecursionlimit(1000000)

# def lcs(chaine1: str, chaine2: str) -> int:
#     @cache
#     def recurse(i: int, j: int) -> int:
#         n = len(chaine1)
#         m = len(chaine2)
#         if i >= n or j >= m:
#             return 0
#         if chaine1[i] == chaine2[j]:
#             return 1 + recurse(i + 1 , j + 1)
#         return max(
#             recurse(i + 1, j),
#             recurse(i, j + 1)
#         )
#     return recurse(0,0)

def lcs(chaine1: str, chaine2: str) -> int:
    n = len(chaine1)
    m = len(chaine2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n):
        for j in range(m):
            if chaine1[i] == chaine2[j]:
                dp[j + 1][i + 1] = 1 + dp[j][i]
            else:
                dp[j + 1][i + 1] = max(dp[j+1][i], dp[j][i+1])
    return dp[m][n]



print("Démarrage des tests pour la Plus Longue Sous-Suite Commune (LCS)...")

# Test 1 : Cas de base - Mots identiques
print("Test 1...", lcs("PYTHON", "PYTHON"))
assert lcs("PYTHON", "PYTHON") == 6, "Échec Test 1 : Deux mots identiques doivent renvoyer leur longueur totale"

# Test 2 : Aucun point commun
print("Test 2...", lcs("ABC", "XYZ"))
assert lcs("ABC", "XYZ") == 0, "Échec Test 2 : Aucun caractère commun doit renvoyer 0"

# Test 3 : Un mot est vide
print("Test 3...", lcs("", "TEST"))
assert lcs("", "TEST") == 0, "Échec Test 3 : Si un des mots est vide, le résultat doit être 0"

# Test 4 : Inclusion totale (Un mot est caché dans l'autre)
print("Test 4...", lcs("AC", "ABC"))
assert lcs("AC", "ABC") == 2, "Échec Test 4 : 'AC' est entièrement présent dans 'ABC'"

# Test 5 : Lettres consécutives vs non-consécutives (L-G-O)
print("Test 5...", lcs("LOGIQUE", "ALGORITHME"))
assert lcs("LOGIQUE", "ALGORITHME") == 4, "Échec Test 5 : Problème avec les lettres espacées (L-G-O)"

# Test 6 : L'exemple du cours (C-A-M-P-I-N-G)
print("Test 6...", lcs("CHAMPIGNON", "CAMPING"))
assert lcs("CHAMPIGNON", "CAMPING") == 6, "Échec Test 6 : L'exemple classique 'CAMPING' a échoué"

# Test 7 : Piège des inversions d'ordre
print("Test 7...", lcs("AB", "BA"))
assert lcs("AB", "BA") == 1, "Échec Test 7 : L'algorithme doit respecter l'ordre des lettres (soit 'A', soit 'B')"

# Test 8 : Performance (Chaînes plus longues - Risque d'explosion 2^n sans DP)
grand_mot1 = "ANANAS_" * 50  # 350 caractères
grand_mot2 = "BANANE_" * 50  # 350 caractères
print("Test 8 (Test de performance)...", lcs(grand_mot1, grand_mot2))
assert lcs(grand_mot1, grand_mot2) == 250, "Échec Test 8 : L'algorithme est trop lent ou gère mal les grands volumes"


# Test 9 : Le Test de l'Apocalypse (Chaos total et choix destructeurs)
mot_piege_1 = "A" + "B"*40 + "C" + "D"*40 + "E" + "F"*40 + "G"
mot_piege_2 = "B"*40 + "A" + "D"*40 + "C" + "F"*40 + "E" + "G"

print("Test 9 (Le Test de l'Apocalypse)...", lcs(mot_piege_1, mot_piege_2))
# Explication : 
# Soit on apparie les lettres uniques (A, C, E, G) -> Longueur 4
# Soit on prend les blocs de lettres répétées (B*40 + D*40 + F*40 + G) -> Longueur 121
assert lcs(mot_piege_1, mot_piege_2) == 121, "Échec Test 10 : L'algorithme a sacrifié les grands blocs pour sauver les premières lettres uniques !"

print("\nTous les tests LCS sont passés avec succès !")