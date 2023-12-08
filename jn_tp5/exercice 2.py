def saisie_notes():
    notes = []
    coefficients = []

    for i in range(1, 6):
        try:
            entree = input(
                f"Veuillez entrer la note du module {i} et le coefficient correspondant (séparés par un espace) : ")
            valeurs = entree.split()

            note = float(valeurs[0])
            coefficient = int(valeurs[1])

            notes.append(note)
            coefficients.append(coefficient)

        except (ValueError, IndexError):
            print(
                "Erreur de saisie. Veuillez entrer une valeur numérique pour la note et un entier pour le coefficient.")
            return None, None

    return notes, coefficients


def calcul_moyenne(notes, coefficients):
    somme = sum(note * coeff for note, coeff in zip(notes, coefficients))
    total_coefficients = sum(coefficients)
    moyenne = somme / total_coefficients
    return moyenne


def evaluer_admission(moyenne, notes):
    if moyenne > 10 and all(note >= 8 for note in notes):
        return "Admis"
    else:
        return "Non admis"


# Saisie des notes et coefficients
notes, coefficients = saisie_notes()

# Vérification de la validité des données
if notes is not None and coefficients is not None:
    # Calcul de la moyenne générale
    moyenne = calcul_moyenne(notes, coefficients)

    # Évaluation de l'admission
    resultat = evaluer_admission(moyenne, notes)

    # Affichage des résultats
    print(f"Moyenne générale : {moyenne:.2f}")
    print(f"Résultat : {resultat}")