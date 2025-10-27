# Compter le nombre de nombres pairs et impairs dasn une liste


def compter_pair_impair(numbers):
    # Initialisation des compteurs
    pair = 0
    impair = 0

    # Boucle sur tous les nombres de la liste
    for n in numbers:
   
        if n % 2 == 0:
            pair += 1
        else:
            impair += 1

    # le résultat 
    print("Nombre de nombres pairs :", pair)
    print("Nombre de nombres impairs :", impair)


#test
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
compter_pair_impair(numbers)

# Users/Utilisateur/Downloads/TP_Python/7_pair_impair.py 
# Nombre de nombres pairs : 4
# Nombre de nombres impairs : 5


