# Exemple : structures de contrôle simples en Python

def deplacer_joueur(position, commande):
    # if / elif / else : décider du mouvement
    if commande == "gauche":
        position -= 2
    elif commande == "droite":
        position += 2
    elif commande == "saute":
        print("Le joueur saute !")
    else:
        print("Commande inconnue.")
    return position

def compte_a_rebours(n):
    # while : boucle jusqu'à 0
    while n > 0:
        print("Compte à rebours :", n)
        n -= 1
    print("Go !")

def iterer_liste(objets):
    # for + continue/break
    for obj in objets:
        if obj == "ignore":
            continue   # passe à l'itération suivante
        if obj == "stop":
            break      # sort de la boucle
        print("Objet :", obj)

def lire_entier(prompt="Entier: "):
    # try / except pour gérer les erreurs d'entrée
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrée invalide — entre un nombre entier.")

# Exemple : True / False et opérateurs logiques

def est_pair(n):
    return n % 2 == 0  # renvoie True ou False

# Variables booléennes
a = True
b = False

# if avec and / or / not
if a and not b:
    print("a est vrai et b est faux")

# utiliser une fonction qui renvoie un booléen
x = 7
if est_pair(x):
    print(x, "est pair")
else:
    print(x, "est impair")

# while avec un drapeau (flag)
running = True
compteur = 0
while running:
    compteur += 1
    print("Boucle :", compteur)
    if compteur >= 3:
        running = False  # bascule vers False pour sortir de la boucle

# combiner conditions
score = 8
vies = 2
if score >= 5 and vies > 0:
    print("Continue — tu as des vies et un bon score")
elif score >= 5 and vies == 0:
    print("Bon score mais plus de vies")
else:
    print("Encore du travail")

# exemple d'utilisation
if __name__ == "__main__":
    pos = 5
    pos = deplacer_joueur(pos, "droite")
    print("Position:", pos)

    iterer_liste(["pomme", "ignore", "banane", "stop", "orange"])

    compte_a_rebours(3)

    age = lire_entier("Quel âge as-tu ? ")
    if age >= 18:
        print("Tu es majeur.")
    else:
        print("Tu es mineur.")