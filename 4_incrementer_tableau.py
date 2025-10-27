# Incrémenter un grand entier représenté sous forme de liste

def incrementer_tableau(digits):
    # On part de la fin du tableau (chiffre le moins significatif)
    for i in range(len(digits) - 1, -1, -1):
        # Si le chiffre n'est pas 9, on ajoute 1 et on peut retourner la liste directement
        if digits[i] < 9:
            digits[i] += 1
            return digits  # Fin de la fonction, pas besoin de continuer

        # Si c’est un 9, il devient 0 et on continue la boucle (retenue à reporter)
        digits[i] = 0

    # Si on arrive ici, c’est que tous les chiffres étaient des 9
    # Exemple : [9,9,9] devient [1,0,0,0]
    return [1] + digits


# test 
print(incrementer_tableau([1, 2, 3]))   
print(incrementer_tableau([4, 3, 2, 1]))
print(incrementer_tableau([9]))        
print(incrementer_tableau([9, 9, 9]))    # 

#  C:\Users\Utilisateur\AppData\Local\Programs\Python\Python312\python.exe c:/Users/Utilisateur/Downloads/TP_Python/4_incrementer_tableau.py
# [1, 2, 4]
# [4, 3, 2, 2]
# [1, 0]
# [1, 0, 0, 0]
