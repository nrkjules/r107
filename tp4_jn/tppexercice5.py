def est_bissextile(annee):
    # Vérifie si l'année est bissextile
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verifier_date(date_str):
    # Vérifie la validité de la date

    # Vérifie la longueur de la chaîne
    if len(date_str) != 8:
        return False

    # Extrait le jour, le mois et l'année de la chaîne
    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:])

    # Vérifie la validité du jour, du mois et de l'année
    if jour < 1 or mois < 1 or mois > 12:
        return False

    jours_dans_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Vérifie la validité du jour en fonction du mois
    if jour > jours_dans_mois[mois]:
        # Vérifie le cas du mois de février pour une année bissextile
        if mois == 2 and est_bissextile(annee) and jour == 29:
            return True
        else:
            return False

    return True

# Demande à l'utilisateur de saisir la date
date_saisie = input("Entrez une date (jjmmaaaa) : ")

# Vérifie la validité de la date et affiche un message approprié
if verifier_date(date_saisie):
    print("La date est valide.")
else:
    print("La date est invalide. Veuillez corriger votre saisie.")