def calcul_prix_location(heure_debut, heure_fin):

    if heure_debut < 0 or heure_fin > 24:
        print("Les heures doivent Ãªtre comprises entre 0 et 24 !\n")
        return


    if heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique Ã  l'heure de dÃ©but.\n")
        return
    elif heure_debut > heure_fin:
        print("Attention ! Le dÃ©but de la location est aprÃ¨s la fin.\n")
        return


    if heure_debut >= 0 and heure_fin <= 7 or heure_debut >= 17 and heure_fin <= 24:
        tarif = 1
    else:
        tarif = 2

    duree_location = heure_fin - heure_debut
    prix_location = tarif * duree_location


    print(f"Le coÃ»t de la location pour la pÃ©riode {heure_debut}h Ã  {heure_fin}h est de {prix_location} euros.")


heure_debut = int(input("Entrez l'heure de dÃ©but de location (entre 0 et 24) : "))
heure_fin = int(input("Entrez l'heure de fin de location (entre 0 et 24) : "))


calcul_prix_location(heure_debut, heure_fin)