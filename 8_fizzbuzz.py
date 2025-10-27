
#fct qui affichee les entier de 3 à 49:
#     - un multiple de 3  afficher "Fizz"
#     -  multiple de 5  afficher "Buzz"
#     - Si  des deux  afficher "FizzBuzz"
#     - Sinon  afficher le nombre lui-même
# ---------------------------------------------------------

def fizzbuzz():
    # Boucle de 3 à 49 nclus
    for i in range(3, 50):
        # de 3 ET de 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        #  multiple de 3
        elif i % 3 == 0:
            print("Fizz")

        #  multiple de 5
        elif i % 5 == 0:
            print("Buzz")

        # Sinon, on affiche i le nombre
        else:
            print(i)


#  test 
fizzbuzz()
