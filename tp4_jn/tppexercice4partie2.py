def most_frequent(lst):
    # Trouvez le nombre avec le plus grand nombre d'occurrences en utilisant la méthode count().
    most_common_num = max(set(lst), key=lst.count)

    # Retournez le résultat sous la forme d'un tuple (nombre, occurrences).
    return most_common_num, lst.count(most_common_num)

# Exemple d'utilisation
liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
resultat = most_frequent(liste_exemple)

# Affichez le résultat
print("Le nombre le plus frequent dans la liste est le : {} ({} x)".format(resultat[0], resultat[1]))