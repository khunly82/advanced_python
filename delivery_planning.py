import heapq

def max_gain_livraisons(courses: list[dict]) -> int:
    if not courses:
       return 0
    s = sorted(courses, key=lambda c: c['deadline'])
    result = []
    for c in s:
        heapq.heappush(result, c['valeur'])
        if len(result) > c['deadline']:
            heapq.heappop(result)
    return sum(result)

"""
{"id": "A", "deadline": 1, "valeur": 40},
{"id": "B", "deadline": 1, "valeur": 10},
{"id": "C", "deadline": 2, "valeur": 50},
{"id": "D", "deadline": 2, "valeur": 60}
"""

print("Démarrage des tests pour le Planificateur de Livraisons...")

# Test 1 : Aucune course disponible
print("Test 1...", max_gain_livraisons([]))
assert max_gain_livraisons([]) == 0, "Échec Test 1 : Sans course, le gain est de 0"

# Test 2 : Deadlines identiques, arbitrage nécessaire
courses_identiques = [
    {"id": "A", "deadline": 1, "valeur": 20},
    {"id": "B", "deadline": 1, "valeur": 100},
    {"id": "C", "deadline": 1, "valeur": 50}
]
print("Test 2...", max_gain_livraisons(courses_identiques))
assert max_gain_livraisons(courses_identiques) == 100, "Échec Test 2 : On doit juste prendre la plus rentable"

# Test 3 : Exemple complexe de l'énoncé (Changement d'avis en cours de route)
courses_arbitrage = [
    {"id": "A", "deadline": 1, "valeur": 40},
    {"id": "B", "deadline": 1, "valeur": 10},
    {"id": "C", "deadline": 2, "valeur": 50},
    {"id": "D", "deadline": 2, "valeur": 60}
]
print("Test 3...", max_gain_livraisons(courses_arbitrage))
assert max_gain_livraisons(courses_arbitrage) == 110, "Échec Test 3 : L'optimum est 110 (50 + 60)"

# Test 4 : Grande deadline mais valeurs faibles vs petites deadlines valeurs fortes
courses_melange = [
    {"id": "A", "deadline": 2, "valeur": 10},
    {"id": "B", "deadline": 2, "valeur": 15},
    {"id": "C", "deadline": 1, "valeur": 100},
    {"id": "D", "deadline": 3, "valeur": 5}
]
# On peut faire C (t=1), B (t=2), A (t=3) -> Total = 120
print("Test 4...", max_gain_livraisons(courses_melange))
assert max_gain_livraisons(courses_melange) == 120, "Échec Test 4 : L'optimum est 125"

# Test 5 : Test de performance (Grand nombre de données avec éjections massives du tas)
import random
random.seed(42)
courses_perf = []
for i in range(5000):
    courses_perf.append({
        "id": f"C_{i}",
        "deadline": random.randint(1, 500), # Beaucoup de conflits (5000 courses pour 500 slots max)
        "valeur": random.randint(10, 1000)
    })

print("Test 5 (Test de performance)...")
resultat = max_gain_livraisons(courses_perf)
print(f"Gain max trouvé sur 5000 courses : {resultat}")
# Si le code est en O(N^2), le test va ramer ou crash. Avec heapq, c'est < 0.05 seconde.
assert resultat > 0, "Échec Test 5"

print("\nTous les tests sont validés ! Tu as dompté le tas.")