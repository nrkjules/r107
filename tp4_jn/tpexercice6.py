def tri_par_selection(tableau):
    n = len(tableau)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if tableau[j] < tableau[min_index]:
                min_index = j

        # Permutation des éléments
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]

        # Affichage de l'évolution du tableau à chaque phase
        print(tableau)


# Déclaration de la liste
liste_exemple = [5, 2, 4, 8, 1, 3]

# Affichage du tableau initial
print(liste_exemple)

# Tri par sélection avec affichage à chaque phase
tri_par_selection(liste_exemple)

# Affichage de la liste triée avec la fonction sorted()
print(sorted(liste_exemple))

# Affichage de la liste triée avec la méthode sort()
liste_exemple.sort()
print(liste_exemple)