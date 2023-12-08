def decomposer_somme(somme):
    billets100 = somme // 100
    reste = somme % 100

    billets50 = reste // 50
    reste = reste % 50

    billets10 = reste // 10
    reste = reste % 10

    pieces2 = reste // 2
    pieces1 = reste % 2

    return billets100, billets50, billets10, pieces2, pieces1


# Saisie de la somme
somme = int(input("Entrez la somme d'argent en euros : "))

# Décomposition de la somme
billets100, billets50, billets10, pieces2, pieces1 = decomposer_somme(somme)

# Affichage du résultat
message = f"{somme} euros, c'est donc {billets100} billets de 100, {billets50} de 50, {billets10} de 10, {pieces2} pièces de 2 et {pieces1} pièce de 1."
print(message)