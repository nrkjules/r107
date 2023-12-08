def taille_chaine(chaine):
    taille = 0
    for caractere in chaine:
        if caractere == '\0':  # Caractère de fin de chaîne
            break
        taille += 1
    return taille

def pourcentage_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    total_voyelles = sum(1 for caractere in chaine if caractere in voyelles)
    taille = taille_chaine(chaine)
    if taille > 0:
        pourcentage = (total_voyelles / taille) * 100
        return pourcentage
    else:
        return 0

def recherche_sous_chaine(chaine, sous_chaine):
    for i in range(len(chaine) - len(sous_chaine) + 1):
        if chaine[i:i + len(sous_chaine)] == sous_chaine:
            return i
    return -1

def nombre_occurrences(chaine, sous_chaine):
    occurrences = 0
    index = recherche_sous_chaine(chaine, sous_chaine)
    while index != -1:
        occurrences += 1
        index = recherche_sous_chaine(chaine[index + 1:], sous_chaine)
    return occurrences

# Saisie de la chaîne par l'utilisateur
chaine = input("Entrez une chaîne de caractères : ")

# Question 1 : Calcul de la taille de la chaîne
taille = taille_chaine(chaine)
print(f"La taille de la chaîne est : {taille}")

# Question 2 : Calcul du pourcentage de voyelles
pourcentage = pourcentage_voyelles(chaine)
print(f"Le pourcentage de voyelles dans la chaîne est : {pourcentage:.2f}%")

# Questions 3 et 4 : Test de la chaîne 'wagon'
sous_chaine = 'wagon'
index_occurrence = recherche_sous_chaine(chaine, sous_chaine)
occurrences = nombre_occurrences(chaine, sous_chaine)

if index_occurrence != -1:
    print(f"'{sous_chaine}' est une sous-chaîne de la chaîne à l'indice {index_occurrence}")
    print(f"Nombre d'occurrences de '{sous_chaine}' dans la chaîne : {occurrences}")
else:
    print(f"'{sous_chaine}' n'est pas une sous-chaîne de la chaîne.")