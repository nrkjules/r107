def multiplication_table(nombre, limite):
    resultat_table = []

    for i in range(limite + 1):
        resultat = nombre * i
        resultat_arrondi = round(resultat, 1)
        resultat_table.append(f"{nombre} * {i} = {resultat_arrondi}")

    return resultat_table

def afficher_table(table):
    print("Vous cherchez la table de multiplication de quel nombre?")

    for ligne in table:
        print(ligne)

# Exemple d'utilisation avec la table de multiplication de 1.2 jusqu'à 9
nombre_a_chercher = float(input("Entrez le nombre pour la table de multiplication : "))
limite_table = 9

table_resultats = multiplication_table(nombre_a_chercher, limite_table)
afficher_table(table_resultats)