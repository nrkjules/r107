def calculer_salaire(nombre_heures, salaire_horaire):
    heures_normales = min(nombre_heures, 160)
    heures_supplementaires1 = max(min(nombre_heures - 160, 40), 0)
    heures_supplementaires2 = max(nombre_heures - 200, 0)

    salaire_total = (
        heures_normales * salaire_horaire +
        heures_supplementaires1 * salaire_horaire * 1.25 +
        heures_supplementaires2 * salaire_horaire * 1.5
    )

    return salaire_total

# Saisie du nombre d'heures travaillées et du salaire horaire
nombre_heures = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

# Calcul et affichage du salaire
salaire_total = calculer_salaire(nombre_heures, salaire_horaire)
print(f"Le salaire total est de : {salaire_total} euros