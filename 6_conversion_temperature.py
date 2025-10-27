
# Exercice 6 : Conversion de température Celsius au  Fahrenheit

def convertir_temperature(temp):
    
    if not temp: #si la saisie vide
        return "Entrée invalide !"

    # On récupère la dernière lettre (F ou C) et le nombre avant
    unite = temp[-1].upper()  # .upper() pour gérer F OU C
    valeur = temp[:-1]        # tout sauf la dernière lettre

    # Vérification que la valeur avant la lettre est bien un nombre
    try:
        valeur = float(valeur)
    except ValueError:
        return "Valeur numérique invalide !"

    # Si la température est en Fahrenheit en Celsius
    if unite == "F":
        celsius = (valeur - 32) * 5 / 9
        return f"La température en Celsius est de {round(celsius, 2)} °C."

    # Si la température est en Celsius 
    elif unite == "C":
        fahrenheit = (valeur * 9 / 5) + 32
        return f"La température en Fahrenheit est de {round(fahrenheit, 2)} °F."

    # Si l’unité est autre chose que C ou F
    else:
        return "Unité invalide ."

# test
print(convertir_temperature("104F"))

print(convertir_temperature("40C"))

print(convertir_temperature("25c"))

print(convertir_temperature("0C"))

print(convertir_temperature("212F"))

#S C:\Users\Utilisateur\Downloads\TP_Python> & C:\Users\Utilisateur\AppData\Local\Programs\Python\Python312\python.exe c:/Users/Utilisateur/Downloads/TP_Python/6_conversion_temperature.py
#la température en Celsius est de 40.0 °C.
#la température en Fahrenheit est de 104.0 °F.
#a température en Fahrenheit est de 77.0 °F.
#a température en Fahrenheit est de 32.0 °F.
#a température en Celsius est de 100.0 °C.
