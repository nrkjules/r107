# Déclarer une variable nMax représentant la taille maximale des vecteurs
nMax = 3

# Déclarer deux listes vides v1 et v2
v1 = []
v2 = []

# Demander à l'utilisateur d'entrer n, la taille effective des vecteurs
while True:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et {}] ? ".format(nMax)))
    if 1 <= n <= nMax:
        break
    else:
        print("La taille doit être comprise entre 1 et {}.".format(nMax))

# Demander à l'utilisateur les composantes des vecteurs v1 et v2
print("Saisie du premier vecteur:")
v1 = [int(input("v1[{}] = ".format(i))) for i in range(n)]

print("Saisie du second vecteur:")
v2 = [int(input("v2[{}] = ".format(i))) for i in range(n)]

# Calculer le produit scalaire de v1 et v2
produit_scalaire = sum(x * y for x, y in zip(v1, v2))

# Afficher le résultat
print("Le produit scalaire de v1 par v2 vaut {}".format(produit_scalaire))