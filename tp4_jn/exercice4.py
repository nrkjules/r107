def most_frequent(lst):
    # Créer un dictionnaire pour compter les occurrences de chaque nombre
    occurrences = {}

    # Remplir le dictionnaire avec les occurrences de chaque nombre
    for num in lst:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    # Trouver le nombre avec le plus grand nombre d'occurrences
    max_occurrences = max(occurrences.values())
    most_frequent_num = max(occurrences, key=occurrences.get)

    # Afficher le résultat
    print("Le nombre le plus frequent dans la liste est le : {} ({} x)".format(most_frequent_num, max_occurrences))


# Exemple d'utilisation
liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
most_frequent(liste_exemple)