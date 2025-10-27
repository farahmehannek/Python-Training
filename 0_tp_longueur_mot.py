# fct qui calcule la longueur du dernier mot d'une phrase
def longueur_dernier_mot(s):
   
    s = s.strip()  # .strip() supprime tt les espaces au début et à la fin 

    mots = s.split(" ") # .split(" ") on découpe la phrase en une liste de mots, en séparant par les espaces

    for mot in reversed(mots):  # reversed(mots) on parcours la liste à l’envers
        
        if mot != "": # On vérifie que le mot n’est  vide espace
            return len(mot) #  on renvoie sa longueur avec len()
    return 0


# --- Partie test  ---

print(longueur_dernier_mot("bonjour papa"))
# C dernier mot = "papa", longueur = 4

print(longueur_dernier_mot(" fais moi des gouffres"))
#  strip() supprime cet espace au début 
# dernier mot = "gouffres", longueur = 8


print(longueur_dernier_mot("La vie est dure sans confiture "))
# strip() le retire à la fin
# dernier mot = "confiture", longueur = 9