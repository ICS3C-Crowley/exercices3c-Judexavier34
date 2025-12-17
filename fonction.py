"""
Démo pour les calculs (opérations mathématiques) 
et les conditions (opérations de comparaison)

Un calcul donne comme résultat : un chiffre (types int et float)
Une condition donne comme résultat : un booléen (vrai/faux)
"""

# variables : bon pour recevoir les réponses

# import math -> fonctions plus spécifiques
def divisible(num):
    divisor = 6
    print(f"{num} est divisible par...")
    while divisor <= 100:
        if num % divisor == 0 : # si le restant de la division est 0
            print(f"{divisor:2} : ✅")
        elif num % divisor == 1 : # si le restant de la division est 0
            print(f"{divisor:2} : 🤏")
        else :
            print(f"{divisor:2} : ❌")
        divisor += 1

while True:
    num = int(input("Un nombre entier (-1 pour quitter)> "))
    if num == -1 :
        break
    else :
        divisible(num)