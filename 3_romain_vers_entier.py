#  Conversion de chiffres romains en entiers
def romain_vers_entier(s):
    # Dictionnaire romain 
    valeurs = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # Somme totale de la conversion
    i = 0      # Index 

    
    while i < len(s): # Boucle principale 
       
        if i + 1 < len(s) and valeurs[s[i]] < valeurs[s[i + 1]]:
            total += valeurs[s[i + 1]] - valeurs[s[i]]
            i += 2  # logique de lecture des chiffre romain
        else:
            total += valeurs[s[i]]
            i += 1  

   
    return total


# test 
print("III  →", romain_vers_entier("III"))       # 3 = 1 + 1 + 1
print("LVIII →", romain_vers_entier("LVIII"))     # 58 = 50 + 5 + 3
print("MCMXCIV →", romain_vers_entier("MCMXCIV")) # 1994 = 1000 + 900 + 90 + 4
print("IX →", romain_vers_entier("IX"))           # 9 = 10 - 1
print("XL →", romain_vers_entier("XL"))           # 40 = 50 - 10

# Users/Utilisateur/Downloads/TP_Python/3_romain_vers_entier.py 
# III  → 3 
# LVIII → 58
# MCMXCIV → 1994
# IX → 9
# XL → 40

