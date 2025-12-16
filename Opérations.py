# python
# Définir des entiers
a = 5
b = -12
c = 0

# Opérations arithmétiques
somme = a + b
prod = a * 3
div_entière = b // 2   # division entière
modulo = a % 2         # reste
puissance = a ** 2     # 5^2 = 25

# Conversion depuis une chaîne
s = "42"
n = int(s)  # 42

# Lecture sécurisée depuis l'utilisateur
def read_int(prompt="Entier: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrée invalide, entre un nombre entier.")

# Générer un entier aléatoire
import random
r = random.randint(1, 10)  # entier entre 1 et 10 inclus

# Liste d'entiers
liste = [i for i in range(0, 10)]  # 0..9
# Vérifier le type
is_int = isinstance(n, int)  # True

# Entiers très grands (Python gère automatiquement la précision)
big = 10**50 

