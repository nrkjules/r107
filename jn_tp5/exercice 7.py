import os.path
from datetime import datetime

def verifier_fichiers(fichier1, fichier2):
    # Vérification de l'existence des fichiers
    if os.path.isfile(fichier1) and os.path.isfile(fichier2):
        # Affichage des tailles des fichiers en octets
        taille_fichier1 = os.path.getsize(fichier1)
        taille_fichier2 = os.path.getsize(fichier2)
        print(f"La taille de {fichier1} est de {taille_fichier1} octets.")
        print(f"La taille de {fichier2} est de {taille_fichier2} octets.")

        # Comparaison des dates de modification
        date_modification1 = datetime.fromtimestamp(os.path.getmtime(fichier1))
        date_modification2 = datetime.fromtimestamp(os.path.getmtime(fichier2))

        if date_modification1 > date_modification2:
            print(f"{fichier1} a été modifié plus récemment le {date_modification1}.")
        elif date_modification2 > date_modification1:
            print(f"{fichier2} a été modifié plus récemment le {date_modification2}.")
        else:
            print("Les deux fichiers ont été modifiés en même temps.")
    else:
        print("Au moins l'un des fichiers n'existe pas.")

# Saisie des noms de fichiers
fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

# Vérification des fichiers
verifier_fichiers(fichier1, fichier2)