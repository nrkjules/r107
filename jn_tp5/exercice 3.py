def nettoyer_chaine(chaine):
    """
    Retire les caractères non alphabétiques de la chaîne et la convertit en minuscules.
    """
    caracteres_permis = [c.lower() for c in chaine if c.isalpha() or c.isspace()]
    return ''.join(caracteres_permis)

def est_palindrome(chaine):
    """
    Teste si la chaîne est un palindrome.
    """
    chaine = nettoyer_chaine(chaine)
    return chaine == chaine[::-1]

# Saisie de la chaîne
entree = input("Entrez un mot ou une phrase : ")

# Test et affichage
if est_palindrome(entree):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")