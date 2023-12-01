# Partie 5
# Enregistrement dans un dictionnaire
info_etudiant = {
    'firstname': 'John',
    'name': 'Doe',
    'promo': 2023,
    'group': 'TP4'
}

# Affichage des données caractérisant l'étudiant
print("Votre nom est '{}', prénom est '{}', vous faites partie de la promo '{}' et votre groupe est '{}'".format(
    info_etudiant['name'],
    info_etudiant['firstname'],
    info_etudiant['promo'],
    info_etudiant['group']
))

# Partie 6
# Affichage du contenu du dictionnaire en utilisant les méthodes keys(), values() et items()
dic = {"name": "toto", "firstname": "titi", "promo": 2022, "group": 202}
print("\nLes clés du dictionnaire sont :")
for key in dic.keys():
    print("-{}".format(key))

print("\nLes valeurs du dictionnaire sont :")
for value in dic.values():
    print("-{}".format(value))

print("\nLes tuplets du dictionnaire sont :")
for item in dic.items():
    print("-{}".format(item))

# Partie 7
# Ajout d'un autre dictionnaire pour former un binôme
binome_info = {
    "name": "tata",
    "firstname": "tutu",
    "promo": 2022,
    "group": 201
}

# Formation du binôme
binome = {'id1': info_etudiant, 'id2': binome_info}

# Partie 8
# Création du dictionnaire "binôme"
print("\nAffichage du binôme :")
for key, value in binome.items():
    print("Membre {} du binôme :".format(key))
    for k, v in value.items():
        print("-{}: {}".format(k, v))

# Partie 9
# Affichage des membres d'un binôme ligne par ligne
print("\nAffichage des membres du binôme ligne par ligne :")
for key, value in binome.items():
    print("Membre {} du binôme :".format(key))
    for k, v in value.items():
        print("-{}: {}".format(k, v))