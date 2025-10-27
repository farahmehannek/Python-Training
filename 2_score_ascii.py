#  Calcul du "score" d'une chaîne


def score_ascii(s):
    # chaîne vide ou 1 caractère,  score  0
    if len(s) < 2:
        return 0

    score = 0  

    # On parcourt la chaîne caractère par caractère (sauf le dernier)
    for i in range(len(s) - 1):
        # ord() renvoie la valeur ASCII d'un caractère
        # abs() donne la valeur absolue d'une différence (pour éviter les négatifs)
        diff = abs(ord(s[i]) - ord(s[i + 1]))

        # On ajoute cette différence au total
        score += diff

        # Affichage de debug 
        print(f"{s[i]}({ord(s[i])}) - {s[i+1]}({ord(s[i+1])}) = {diff}")

    
    return score


#  test
print("Score de 'hello' :", score_ascii("hello"))

print("Score de 'zaz' :", score_ascii("zaz"))

print("Score de 'data' :", score_ascii("data"))

#Users/Utilisateur/Downloads/TP_Python/2_score_ascii.py
# h(104) - e(101) = 3
# e(101) - l(108) = 7
# l(108) - l(108) = 0
# l(108) - o(111) = 3
# Score de 'hello' : 13