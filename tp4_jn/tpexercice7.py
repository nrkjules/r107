#partie1
binome = ('jul',1, '',2)
print(f"L'etudiant {binome[0]} est en binome avec l'etudiant {binome[1]}")

#Partie 2
nouveau_login = input("Entrez le nouveau login : ")
binome = (binome[0], nouveau_login)
print(f"Nouveau binÃ´me : l'etudiant {binome[0]} est en binome avec l'etudiant {binome[1]}")

#Partie 3
troisieme_login = input("Entrez le troisiÃ¨me login : ")
binome = binome + (troisieme_login,)
print(f"Trinpme : {binome}")

