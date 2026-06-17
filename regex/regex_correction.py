import re

def contient_chiffre(s: str) -> bool:
    return re.search(r'\d', s) != None

def commence_par_majuscule(s: str) -> bool:
    return re.match(r'[A-Z]', s) != None

def valide_code_postal(s: str) -> bool:
    return re.match(r'\d{5}$', s) != None

def trouve_chat(s: str) -> bool:
    return re.search(r'\bchat\b', s) != None

def nettoyer_espaces(s: str) -> str:
    return re.sub(r'\s+', ' ', s)

def extraire_dates(s: str) -> str:
    pattern = r'\b(?:0[1-9]|[12][0-9]|3[01])\/(?:0[1-9]|1[012])\/\d{4}\b'
    return re.findall(pattern, s)


def test_ex1_contient_chiffre():
    assert contient_chiffre("J'ai 2 chats.") is True
    assert contient_chiffre("Le prix est de 99€.") is True
    assert contient_chiffre("Pas de chiffre ici.") is False
    assert contient_chiffre("") is False


def test_ex2_commence_par_majuscule():
    assert commence_par_majuscule("Bonjour") is True
    assert commence_par_majuscule("A") is True
    assert commence_par_majuscule("bonjour") is False
    assert commence_par_majuscule("123 Bonjour") is False
    assert commence_par_majuscule(" Bonjour") is False  # Espace au début


def test_ex3_valide_code_postal():
    assert valide_code_postal("75001") is True
    assert valide_code_postal("06000") is True
    assert valide_code_postal("7500") is False   # Trop court
    assert valide_code_postal("750012") is False  # Trop long
    assert valide_code_postal("75A01") is False   # Contient une lettre
    assert valide_code_postal("abcde") is False   # Que des lettres


def test_ex4_trouve_chat():
    assert trouve_chat("Le chat dort.") is True
    assert trouve_chat("Mon chat, il est beau.") is True
    assert trouve_chat("J'ai acheté un château.") is False  # Mot composé (début)
    assert trouve_chat("C'est un achat utile.") is False    # Mot composé (fin)
    assert trouve_chat("chats") is False                     # Pluriel (frontière brisée)


def test_ex5_nettoyer_espaces():
    assert nettoyer_espaces("Un   deux  trois") == "Un deux trois"
    assert nettoyer_espaces("Texte\navec\t\tplusieurs   espaces") == "Texte avec plusieurs espaces"
    assert nettoyer_espaces("   Espace au début et à la fin   ") == " Espace au début et à la fin "
    assert nettoyer_espaces("Déjà-propre") == "Déjà-propre"

def extraire_hashtags(s: str) -> list[str]:
    return re.findall(r'#\S+', s)

def masquer_tel(s: str) -> str:
    return re.sub(r'(?:\d{2}[ \.-]?){5}', '[REDACTED]', s)

def extraire_paragraphes(s: str)-> list[str]:
    return re.findall(r'<p>(.*?)</p>', s)


def valide_pseudo(s: str) -> bool:
    return re.match(r'[a-zA-Z]\w{3,11}$', s) != None


def total_facture(s: str) -> float:
    pattern = r'\d+(?:[\.,]\d+){0,1} ?(?=€)'
    return sum([float(
        re.sub(r',', '.', p)
    ) for p in re.findall(pattern, s)])

def obtenir_ip_uniques(s: str) -> list[str]:
    ip_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])'
    l = re.findall(ip_pattern, s, re.MULTILINE)
    return sorted(list(set(l)))

def compresser_texte(s: str) -> str:
    pattern = r'([A-Z])\1*'
    return re.sub(
        pattern, 
        lambda m: m.group()[0] + str(len(m.group())), 
    s)

# # ---------------------------------------------------------------------
# # NIVEAU MOYEN : Extraction et Manipulation
# # ---------------------------------------------------------------------

def test_ex6_extraire_hashtags():
    assert extraire_hashtags("J'adore le #Python !") == ["#Python"]
    assert extraire_hashtags("#Deep_Learning et #IA") == ["#Deep_Learning", "#IA"]
    assert extraire_hashtags("Pas de hashtag ici.") == []
    assert extraire_hashtags("Le symbole # tout seul") == []


def test_ex7_extraire_dates():
    texte = "Inscrit le 12/05/2023, modifié le 01/12/2025."
    print(extraire_dates(texte))
    assert extraire_dates(texte) == ["12/05/2023", "01/12/2025"]
    assert extraire_dates("Date invalide : 123/01/2022") == []
    assert extraire_dates("Autre format : 2026-05-28") == []


def test_ex8_masquer_tel():
    assert masquer_tel("Appelez le 0612345678") == "Appelez le [REDACTED]"
    assert masquer_tel("Fixe : 01.42.56.78.90") == "Fixe : [REDACTED]"
    assert masquer_tel("Mon num: 07-89-10-11-12") == "Mon num: [REDACTED]"
    # assert masquer_tel("International +33 6 12 34 56 78") == "International +33 [REDACTED]"


def test_ex9_extraire_paragraphes():
    html = "<p>Premier</p> de l'histoire et <p>Second</p>"
    assert extraire_paragraphes(html) == ["Premier", "Second"]
    assert extraire_paragraphes("<p></p>") == [""] # Vide mais valide
    assert extraire_paragraphes("<div>Pas de p</div>") == []


def test_ex10_valide_pseudo():
    assert valide_pseudo("Gamer_99") is True    # 8 caractere, commence par lettre
    assert valide_pseudo("Alex") is True        # Limite basse (4 caractères)
    assert valide_pseudo("X_Ragnarok_X") is True # Limite haute (12 caractères)
    assert valide_pseudo("123Gamer") is False    # Commence par un chiffre
    assert valide_pseudo("Ace") is False         # Trop court (3 caractères)
    assert valide_pseudo("GamerPolonais99") is False # Trop long (15 caractères)
    assert valide_pseudo("Sniper-45") is False   # Caractère interdit (-)


# # ---------------------------------------------------------------------
# # NIVEAU DIFFICILE : Regex & Algorithmique
# # ---------------------------------------------------------------------

def test_ex11_total_facture():
    f1 = "Café: 2,50€, Sandwich: 5.50 €, Dessert: 4€."
    assert total_facture(f1) == 12.0
    assert total_facture("Rien n'est payant ici.") == 0.0
    assert total_facture("Gros achat à 1250,99 €") == 1250.99


def test_ex12_obtenir_ip_uniques():
    logs = """
    192.168.1.1 - Login success
    10.0.0.254 - Bad gateway
    192.168.1.1 - Duplicate entry
    999.999.999.999 - Fausse IP sauvage
    """
    assert obtenir_ip_uniques(logs) == ["10.0.0.254", "192.168.1.1"]
    assert obtenir_ip_uniques("Aucune IP") == []


def test_ex13_compresser_texte():
    assert compresser_texte("AAABBCDDDD") == "A3B2C1D4"
    assert compresser_texte("A") == "A1"
    assert compresser_texte("AABBBBA") == "A2B4A1" # Repétitions séparées
    assert compresser_texte("") == ""


def test_ex14_evaluer_mot_de_passe():
    # Test mot de passe parfait (5/5)
    r1 = evaluer_mot_de_passe("Secr3t!_")
    assert r1["score"] == 5
    assert len(r1["manquants"]) == 0

    # Test mot de passe faible (2/5)
    r2 = evaluer_mot_de_passe("bobby")
    assert r2["score"] == 2 # Longueur non validée, pas de maj, pas de chiffre, pas de spécial
    assert "Au moins une majuscule" in r2["manquants"]
    assert "Au moins un chiffre" in r2["manquants"]
    assert "Au moins 8 caractères" in r2["manquants"]


# def test_ex15_markdown_to_html():
#     md = "# Titre\n## Sous-titre\nDu **gras** et un [lien](http://test.com)."
#     attendu = "<h1>Titre</h1>\n<h2>Sous-titre</h2>\nDu <strong>gras</strong> et un <a href=\"[http://test.com](http://test.com)\">lien</a>."
#     assert markdown_to_html(md) == attendu


test_ex1_contient_chiffre()
test_ex2_commence_par_majuscule()
test_ex3_valide_code_postal()
test_ex4_trouve_chat()
test_ex5_nettoyer_espaces()
test_ex6_extraire_hashtags()
test_ex7_extraire_dates()
test_ex8_masquer_tel()

test_ex9_extraire_paragraphes()

test_ex10_valide_pseudo()

test_ex11_total_facture()

test_ex12_obtenir_ip_uniques()

test_ex13_compresser_texte()

test_ex14_evaluer_mot_de_passe()