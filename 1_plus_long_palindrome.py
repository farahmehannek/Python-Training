 #Trouver la plus longue sous-chaîne palindromiqu

def plus_long_palindrome(s):  # Fct principale qui renvoie la plus long sous-chaîne palindromique dans 's'
    
    if len(s) < 2:
        return s # si la chaîne est vide ou de longueur 1, on la renvoie telle quelle

    # On initialise les bornes du palindrome trouvé (début et fin)
    debut, fin = 0, 0


    def etendre_depuis_centre(gauche, droite): # Fct  pr étendre le palindrome autour d'un centre
        while gauche >= 0 and droite < len(s) and s[gauche] == s[droite]:
            gauche -= 1
            droite += 1
        # On retourne la sous-chaîne palindrome trouvée
        return s[gauche + 1:droite]

    
    for i in range(len(s)): # on mis chaque caractère comme centre possible
        # si palindrome est de  longueur impaire 
        p1 = etendre_depuis_centre(i, i)
        # si palindrome de longueur paire (ex : "abba")
        p2 = etendre_depuis_centre(i, i + 1)

        # On garde le plus long des deux
        plus_long = p1 if len(p1) > len(p2) else p2

        # Si le palindrome actuel est plus long que le précédent, on le remplace
        if len(plus_long) > fin - debut:
            debut = i - (len(plus_long) - 1) // 2
            fin = i + len(plus_long) // 2

    # On renvoie la plus longue sous-chaîne palindrome
    return s[debut:fin + 1]


# --- Partie test ---
print(plus_long_palindrome("babad"))
# "bab" ou "aba" → les deux sont des réponses valides

print(plus_long_palindrome("cbbd"))
# palindrome = "bb"

print(plus_long_palindrome("racecar"))
# palindrome = "racecar" (toute la chaîne)

print(plus_long_palindrome("python"))
# palindrome = "p" (aucun mot plus long)
