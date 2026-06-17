def resoudre_labyrinthe(lab):
    n = len(lab)
    solution = [[0 for _ in range(n)] for _ in range(n)]

    def solve(x: int, y: int) -> bool:
        if x >= n or y >= n or lab[x][y] == 1:
            return False
        solution[x][y] = 1
        if x == n - 1 and y == n - 1:
            return True
        
        if(solve(x, y + 1)):
            return True

        if(solve(x + 1, y)):
            return True
        
        solution[x][y] = 0
        return False
     
    return solution if solve(0,0) else None

def extraire_case_arrivee(solution):
    """Renvoie la valeur de la case d'arrivée en bas à droite."""
    if not solution or isinstance(solution, str):
        return 0
    return solution[-1][-1]

def extraire_case_depart(solution):
    """Renvoie la valeur de la case de départ en haut à gauche."""
    if not solution or isinstance(solution, str):
        return 0
    return solution[0][0]

# Test 1 : Cas de base - Labyrinthe miniature 2x2 tout ouvert
lab_simple = [
    [0, 0],
    [0, 0]
]

res_1 = resoudre_labyrinthe(lab_simple)
print("Test 1...", res_1)
assert extraire_case_arrivee(res_1) == 1, "Échec Test 1 : Un labyrinthe simple et ouvert doit être résolu."


# Test 2 : Pas de solution - Arrivée bloquée par un mur
lab_bloque = [
    [0, 1],
    [0, 1]
]
res_2 = resoudre_labyrinthe(lab_bloque)
print("Test 2...", res_2)
assert res_2 is None or "Pas de solution" in str(res_2) or res_2 == False, "Échec Test 2 : Si l'arrivée est un mur, l'algorithme doit retourner un échec."


# Test 3 : Départ bloqué immédiatement
lab_depart_bloque = [
    [1, 0],
    [0, 0]
]
res_3 = resoudre_labyrinthe(lab_depart_bloque)
print("Test 3...", res_3)
assert extraire_case_depart(res_3) == 0, "Échec Test 3 : Si la case de départ est un mur, impossible de commencer."


# Test 4 : L'exemple classique du cours (avec un seul chemin sinueux)
lab_cours = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]
res_4 = resoudre_labyrinthe(lab_cours)
print("Test 4...")
# On vérifie un point clé du chemin obligatoire (la case (1, 1) et (2, 1))
assert res_4[1][1] == 1 and res_4[2][1] == 1 and res_4[3][3] == 1, "Échec Test 4 : Le chemin trouvé n'est pas le bon ou a sauté une étape clé."


# Test 5 : Le piège du cul-de-sac (Force le Backtracking)
# L'algorithme va vouloir aller tout droit (à droite), va s'enfoncer, bloquer, et devoir TOUT reculer
lab_piege = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
res_5 = resoudre_labyrinthe(lab_piege)
print("Test 5...")
# Si le backtracking a mal nettoyé ses traces, la case (0, 3) ou (1, 2) pourrait être restée à 1 indûment
assert res_5[0][1] == 1 and res_5[0][2] == 1, "Échec Test 5 : L'algorithme s'est perdu dans le cul-de-sac ou n'a pas nettoyé ses pas."


# Test 6 : Labyrinthe géant (Performance de l'exploration)
# Une longue ligne droite qui serpente en zig-zag
taille = 30
lab_geant = [[0] * taille for _ in range(taille)]
# On remplit de murs pour faire un unique serpentin
for i in range(taille):
    for j in range(taille):
        if i % 2 == 1 and j < taille - 1:
            lab_geant[i][j] = 1
res_6 = resoudre_labyrinthe(lab_geant)
print("Test 6 (Test de performance)...")
assert extraire_case_arrivee(res_6) == 1, "Échec Test 6 : L'algorithme a planté (Stack Overflow ?) ou est trop lent sur une grande grille."

# Test 7 : Le piège du départ sans issue (Test de nettoyage absolu du path)
lab_impasse_depart = [
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 0]  # L'arrivée est là, mais le départ est muré de tous les côtés
]

print("Test 7 (Test de l'impasse initiale)...")
res_7 = resoudre_labyrinthe(lab_impasse_depart)

# On vérifie que la fonction renvoie bien None
assert res_7 is None, "Échec Test 7 : La fonction aurait dû renvoyer None car le labyrinthe est impossible."

# Test 8 : Le Grand Escalier avec fausses pistes (Compatible Bas/Droite uniquement)
size = 25
lab_geant = [[0] * size for _ in range(size)]

# 1. On crée une structure en escalier (le vrai chemin suit la diagonale)
# Mais on ouvre de grands boulevards "pièges" tout droit et vers le bas
for i in range(size):
    for j in range(size):
        # On mure les zones inutiles pour forcer un entonnoir diagonal
        if j > i + 1 or i > j + 1:
            lab_geant[i][j] = 1

# 2. LES PIÈGES : On ouvre des couloirs qui vont tout droit vers les bords...
# mais qui finissent par des culs-de-sac tout au bout.
for i in range(0, size - 2, 3):
    # Fausse piste horizontale
    lab_geant[i][i+1] = 0 
    if i + 2 < size:
        lab_geant[i][i+2] = 0
        if i + 3 < size:
            lab_geant[i][i+3] = 1 # Cul-de-sac !

print(f"Test 8 (Labyrinthe Géant {size}x{size} en Escalier)...")
res_8 = resoudre_labyrinthe(lab_geant)

# Assertions pour valider le résultat
assert res_8 is not None, "Échec Test 8 : Le grand escalier a une solution valide en Bas/Droite !"
assert res_8[size-1][size-1] == 1, "Échec Test 8 : L'arrivée en bas à droite n'est pas atteinte."
# On vérifie qu'une des fausses pistes (ex: ligne 3, colonne 6) a bien été nettoyée (vaut 0)
assert res_8[2][5] == 0, "Échec Test 8 : Le backtracking n'a pas nettoyé les fausses pistes de l'escalier !"

print("\nTous les tests du Labyrinthe sont passés avec succès !")