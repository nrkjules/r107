import random

def deviner_nombre_mystere():
    nombre_mystere = random.randint(0, 100)

    tours = 0

    print("Devinez le nombre mystÃ¨re entre 0 et 100.")

    while True:

        tentative = int(input("Votre proposition : "))
        tours += 1


        if tentative < nombre_mystere:
            print("Plus grand. Essayez encore.")
        elif tentative > nombre_mystere:
            print("Plus petit. Essayez encore.")
        else:
            print(f"Bravo ! Vous avez trouvÃ© le nombre mystÃ¨re {nombre_mystere} en {tours} tours.")
            break


deviner_nombre_mystere()