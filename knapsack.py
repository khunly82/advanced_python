from functools import cache


def knapsack(capacite: int, objets: list[dict]) -> int:
    @cache
    def recurse(remaining_weight, idx):
        if idx >= len(objets) or remaining_weight < objets[idx]['poids']:
            return 0
        return max(
            recurse(remaining_weight, idx + 1),
            objets[idx]['valeur'] + recurse(remaining_weight - objets[idx]['poids'] ,idx +1)
        )
    return recurse(capacite, 0)

def knapsack(capacite: int, objets: list[dict]) -> int:
    dp = [0] * (capacite + 1)
    for item in objets:
        for i in range(capacite, item['poids'] - 1, -1):
            dp[i] = max(dp[i], item['valeur'] + dp[i - item['poids']])
    return dp[capacite]
        

print("Démarrage des tests pour le Sac à Dos 0/1 (Format Objets)...")

# Test 1 : Sac vide ou capacité nulle
print("Test 1...", knapsack(0, [{"valeur": 10, "poids": 1}, {"valeur": 20, "poids": 2}]))
assert knapsack(0, [{"valeur": 10, "poids": 1}, {"valeur": 20, "poids": 2}]) == 0, "Échec Test 1 : Capacité 0 doit renvoyer 0"

# Test 2 : Un seul objet disponible et il rentre
print("Test 2...", knapsack(10, [{"valeur": 100, "poids": 5}]))
assert knapsack(10, [{"valeur": 100, "poids": 5}]) == 100, "Échec Test 2 : L'objet doit être pris"

# Test 3 : Un seul objet disponible mais trop lourd
print("Test 3...", knapsack(10, [{"valeur": 100, "poids": 15}]))
assert knapsack(10, [{"valeur": 100, "poids": 15}]) == 0, "Échec Test 3 : Objet trop lourd, valeur 0"

# Test 4 : Tous les objets rentrent
objets_tous = [{"valeur": 10, "poids": 1}, {"valeur": 20, "poids": 2}, {"valeur": 30, "poids": 3}]
print("Test 4...", knapsack(10, objets_tous))
assert knapsack(10, objets_tous) == 60, "Échec Test 4 : Tout rentre, on additionne tout"

# Test 5 : Le piège glouton classique (Meilleur ratio valeur/poids qui bloque l'optimum global)
objets_piege_ratio = [
    {"valeur": 65, "poids": 12}, # ratio 6 (meilleur)
    {"valeur": 50, "poids": 10}, # ratio 5
    {"valeur": 50, "poids": 10}  # ratio 5
]
print("Test 5...", knapsack(20, objets_piege_ratio))
assert knapsack(20, objets_piege_ratio) == 100, "Échec Test 5 : Piège glouton de ratio ! L'optimum est 100 (50+50)"

# Test 6 : Le piège glouton par le poids (Prendre le plus léger d'abord échoue)
objets_piege_poids = [
    {"valeur": 10, "poids": 2},  # Plus léger
    {"valeur": 100, "poids": 5}  # Plus lourd mais beaucoup plus rentable
]
print("Test 6...", knapsack(5, objets_piege_poids))
assert knapsack(5, objets_piege_poids) == 100, "Échec Test 6 : Piège glouton sur le poids léger"

# Test 7 : Objets identiques (Choix multiples possibles)
objets_identiques = [{"valeur": 20, "poids": 5}, {"valeur": 20, "poids": 5}, {"valeur": 20, "poids": 5}]
print("Test 7...", knapsack(11, objets_identiques))
assert knapsack(11, objets_identiques) == 40, "Échec Test 7 : Doit prendre exactement 2 objets sur 3"

# Test 8 : Performance (Grand nombre d'objets - Risque d'explosion 2^n sans DP)
objets_grand = [
    {"valeur": 10, "poids": 1},  {"valeur": 20, "poids": 2},  {"valeur": 30, "poids": 3},
    {"valeur": 40, "poids": 4},  {"valeur": 50, "poids": 5},  {"valeur": 60, "poids": 6},
    {"valeur": 70, "poids": 7},  {"valeur": 80, "poids": 8},  {"valeur": 90, "poids": 9},
    {"valeur": 100, "poids": 10}, {"valeur": 110, "poids": 11}, {"valeur": 120, "poids": 12},
    {"valeur": 130, "poids": 13}, {"valeur": 140, "poids": 14}, {"valeur": 150, "poids": 15},
    {"valeur": 160, "poids": 16}, {"valeur": 170, "poids": 17}, {"valeur": 180, "poids": 18},
    {"valeur": 190, "poids": 19}, {"valeur": 200, "poids": 20}
]
print("Test 8 (Test de performance)...", knapsack(50, objets_grand))
assert knapsack(50, objets_grand) == 500, "Échec Test 8 : Trop lent ou mauvaise valeur"

# Test 9 : Performance extrême avec grande capacité
objets_ext = [
    {"valeur": 5, "poids": 50},  {"valeur": 10, "poids": 100}, {"valeur": 15, "poids": 150},
    {"valeur": 20, "poids": 200}, {"valeur": 25, "poids": 250}, {"valeur": 30, "poids": 300}
]
print("Test 9 (Test de performance grande capacité)...", knapsack(1000, objets_ext))
assert knapsack(1000, objets_ext) == 100, "Échec Test 9 : Échec sur une capacité élevée"

print("\nTous les tests du Sac à Dos (Format Objets) sont passés avec succès !")