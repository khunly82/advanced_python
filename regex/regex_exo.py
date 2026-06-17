import re


def contains_digit(text: str) -> bool:
    return re.search(r'\d', text) != None

def start_with_uppercase(text: str) -> bool:
    return re.match(r'[A-Z]', text) != None

def is_postal_code(text: str) -> bool:
    return re.match(r'\d{5}$', text) != None

def found_cat(text: str) -> bool:
    return re.search(r'\bchat\b', text) != None

def clean_spaces(text: str) -> bool:
    return re.sub(r'\s+', ' ', text)

def get_tags(text: str) -> list[str]:
    return re.findall(r'#\S+', text)

def extract_dates(text: str) -> list[str]:
    return re.findall(r'\b(?:0[1-9]|[12][\d]|3[01])\/(?:0[1-9]|1[012])\/\d{4}\b', text)

def valid_pseudo(text: str) -> bool:
    return re.match(r'^[a-zA-Z]\w{3,13}$', text) != None

def total_facture(text: str) -> float:
    prices = re.findall('(?:\d|\s|\.|,)+?(?=€)', text)
    return sum([
        float(re.sub(',', '.', p)) for p in prices
    ])

def compresser_texte(text):
    return re.sub(r'([A-Z])\1*', lambda s: f'{s.group()[0]}{len(s.group())}', text)

assert contains_digit('57dd') == True
assert contains_digit('d5d') == True
assert contains_digit('dd') == False

assert start_with_uppercase('Papa') == True
assert start_with_uppercase('papa') == False

assert is_postal_code('75000') == True
assert is_postal_code('6666666') == False
assert is_postal_code('6666') == False

assert found_cat('les achats') == False
assert found_cat('le chat est gentil') == True
assert found_cat('le chapeau de toto') == False
assert found_cat('achat') == False

assert clean_spaces('  Avez   vous\nvu\tle   nouveau    chapeau   de   zozo   ') == " Avez vous vu le nouveau chapeau de zozo "
assert get_tags('#test # #machin') == ['#test', '#machin']

assert extract_dates('le 05/06/1982 est une date mais 45/06/1999, 00/12/9999 et 123/12/1999 ne le sont pas' ) == ['05/06/1982']


assert valid_pseudo("Gamer_99") is True    # 8 caractere, commence par lettre
assert valid_pseudo("Alex") is True        # Limite basse (4 caractères)
assert valid_pseudo("X_Ragnarok_X") is True # Limite haute (12 caractères)
assert valid_pseudo("123Gamer") is False    # Commence par un chiffre
assert valid_pseudo("Ace") is False         # Trop court (3 caractères)
assert valid_pseudo("GamerPolonais99") is False # Trop long (15 caractères)
assert valid_pseudo("Sniper-45") is False   # Caractère interdit (-)

f1 = "Café: 2,50€, Sandwich: 5.50 €, Dessert: 4€."    
assert total_facture(f1) == 12.0    
assert total_facture("Rien n'est payant ici.") == 0.0    
assert total_facture("Gros achat à 1250,99 €") == 1250.99

print(compresser_texte("AAABBCDDDD"))
assert compresser_texte("AAABBCDDDD") == "A3B2C1D4"    
assert compresser_texte("A") == "A1"    
assert compresser_texte("AABBBBA") == "A2B4A1" # Repétitions séparées    
assert compresser_texte("") == ""

print('All tests have passed')