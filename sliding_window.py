from collections import deque

def max_fenetre_glissante(nums: list[int], k: int) -> list[int]:
    results = []
    indexes = deque()
    for i in range(len(nums)):
        if indexes and i > indexes[0] + k - 1:
            indexes.popleft()
        while indexes and nums[indexes[-1]] < nums[i]:
            indexes.pop()
        indexes.append(i)
        if i >= k - 1:
            results.append(nums[indexes[0]])
    return results

print("Démarrage des tests pour la Fenêtre Glissante (Format Deque)...")

# Test 1 : Fenêtre de taille 1 (Le résultat est identique au tableau d'origine)
print("Test 1...", max_fenetre_glissante([1, 3, -1, 5], 1))
assert max_fenetre_glissante([1, 3, -1, 5], 1) == [1, 3, -1, 5], "Échec Test 1"

# Test 2 : Fenêtre égale à la taille du tableau
print("Test 2...", max_fenetre_glissante([1, 3, -1, 5], 4))
assert max_fenetre_glissante([1, 3, -1, 5], 4) == [5], "Échec Test 2"

# Test 3 : Tableau strictement croissant
print("Test 3...", max_fenetre_glissante([1, 2, 3, 4, 5], 3))
assert max_fenetre_glissante([1, 2, 3, 4, 5], 3) == [3, 4, 5], "Échec Test 3"

# Test 4 : Tableau strictement décroissant
print("Test 4...", max_fenetre_glissante([5, 4, 3, 2, 1], 3))
assert max_fenetre_glissante([5, 4, 3, 2, 1], 3) == [5, 4, 3], "Échec Test 4"

# Test 5 : Éléments identiques
print("Test 5...", max_fenetre_glissante([2, 2, 2, 2], 2))
assert max_fenetre_glissante([2, 2, 2, 2], 2) == [2, 2, 2], "Échec Test 5"

# Test 6 : Cas classique alternatif (valeurs négatives)
print("Test 6...", max_fenetre_glissante([1, 3, -1, -3, 5, 3, 6, 7], 3))
assert max_fenetre_glissante([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7], "Échec Test 6"

# Test 7 : Test de performance (Grand tableau, grande fenêtre)
# Une approche en O(n*k) ferait environ 500 000 000 d'opérations et prendrait plusieurs secondes/minutes.
# Une approche en O(n) avec deque prend quelques millisecondes.
import random
grand_tableau = [i for i in range(50000)] # Tableau croissant pour simplifier la validation
k_grand = 10000
print("Test 7 (Test de performance)...")
resultat_perf = max_fenetre_glissante(grand_tableau, k_grand)
# Le premier max de la fenêtre [0...9999] doit être 9999, le dernier doit être 49999
assert len(resultat_perf) == 40001, "Échec Test 7 : Taille du résultat incorrecte"
assert resultat_perf[0] == 9999 and resultat_perf[-1] == 49999, "Échec Test 7 : Valeurs incorrectes ou trop lent"

print("\nTous les tests de la Fenêtre Glissante ont passé avec succès !")
