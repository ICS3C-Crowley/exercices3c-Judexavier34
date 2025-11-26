# Mini questionnaire pour joueur 1 et joueur 2


joueur1 = input("joueur1, entre ton nom: ")
joueur2 = input("joueur2, entre ton nom: ")


print("Bonjour",joueur1)
print("Bonjour",joueur2)
print(f"lesjoueursont{joueur1} et {joueur2}.")


print("Question1: Quel est la capitale de l'Australie?")
options=["A: Sydney","B: Melbourne","C: Canberra","D: Brisbane"]
reponse ="C: Canberra"
reponse1=input(joueur1 + ", ta reponse: ")
reponse2=input(joueur2 + ", ta reponse: ")


print("Question2: Combien y a-t-il de continents sur Terre?")
options=["A: 5","B: 6","C:7","D:8"]
reponse ="C:7"
reponse3=input(joueur1 + ", ta reponse: ")
reponse4=input(joueur2 + ", ta reponse: ")


print("Question3: Quel est le plus grand pays du monde par superficie?")
options=["A: Canada","B: Chine","C: Russie","D: Etatas-Unis"]
reponse ="C: Russie"
reponse5=input(joueur1 + ", ta reponse:")
reponse6=input(joueur2 + ", ta reponse :")


print("Question4: Quel est l'élément chinique dont le symbole est '0' ?")
options=["A: Or","B: Oxygéne","C: Argent","D: Fer"]
reponse ="B: Oxygéne"
reponse7=input(joueur1 + ", ta reponse :")
reponse8=input(joueur2 + ", ta reponse :")


print("Question5: Quel est le plus long fleuve du monde ?")
options=["A: Nille","B: Amazone","C: Yangtsé","D: Mississippi"]
reponse="A: Nille"
reponse9=input(joueur1 + ", ta reponse :")
reponse10=input(joueur2 + ", ta reponse :")


# Calcul des scores

# TODO prend de la logique... à ajouter dans une prochaine version

# score_joueur1 =10
# score_joueur2 =10


print("Merci d'avioir participé au questionnairer.")
print(joueur1,"a répondu:", reponse1, reponse2, reponse3 ,reponse4,reponse5 )
print(joueur2,"a répondu:", reponse6, reponse6, reponse7,reponse8,reponse9,reponse10)
# print(joueur1,"a obtenu un score de:", score_joueur1)
# print(joueur2,"a obtenu un score de:", score_joueur2)
