# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

# Remplissage de la liste et calcul de la somme des notes
for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))

    # Vérification que la note est dans la plage autorisée
    while note < 0 or note > 20:
        print("Veuillez entrer une note entre 0 et 20.")
        note = float(input(f"Note etudiant {i} : "))

    moyenne += note
    notes.append(note)

# Calcul de la moyenne de classe
moyenne = moyenne / nombreEtudiants

# Affichage de la moyenne de classe
print(f"Moyenne de classe : {moyenne}")

# Affichage du tableau avec le numéro de l'étudiant, la note et l'écart à la moyenne
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note} | {ecart}")