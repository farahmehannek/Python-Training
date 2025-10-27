
# Nombres divisibles par 7 et multiples de 5, compris 1500 et 2700 

# On crée une liste vide 
resultats = []

# La fonction  va de 1500 à 2700 inclus
for x in range(1500, 2701):


    if x % 7 == 0 and x % 5 == 0:
        resultats.append(x)

# Affichage final des nombres trouvés
print("Nombres divisibles par 7 et multiples de 5 entre 1500 et 2700 :")
print(resultats)

#C:\Users\Utilisateur\AppData\Local\Programs\Python\Python312\python.exe c:/Users/Utilisateur/Downloads/TP_Python/5_divisible_7_multiple_5.py
#Nombres divisibles par 7 et multiples de 5 entre 1500 et 2700 :
#[1505, 1540, 1575, 1610, 1645, 1680, 1715, 1750, 1785, 1820, 1855, 1890, 1925, 1960, 1995, 2030, 2065, 2100, 2135, 2170, 2205, 2240, 2275, 2310, 2345, 2380, 2415, 2450, 2485, 2520, 2555, 2590, 2625, 2660, 2695]