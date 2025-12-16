# Mini questionnaire pour joueur 1 et joueur 2


joueur1 = input("joueur1, entre ton nom: ")
joueur2 = input("joueur2, entre ton nom: ")

print("Bonjour", joueur1) 
print("Bonjour", joueur2)
print(f"Les joueurs sont {joueur1} et {joueur2}.")

# Question 1
print("\nQuestion 1: Quel est la capitale de l'Australie ?")
options = ["A: Sydney", "B: Melbourne", "C: Canberra", "D: Brisbane"]
print("  " + "   ".join(options))
reponse1 = input(joueur1 + ", ta réponse: ")
reponse2 = input(joueur2 + ", ta réponse: ")

# Question 2
print("\nQuestion 2: Combien y a-t-il de continents sur Terre ?")
options = ["A: 5", "B: 6", "C: 7", "D: 8"]
print("  " + "   ".join(options))
reponse3 = input(joueur1 + ", ta réponse: ")
reponse4 = input(joueur2 + ", ta réponse: ")

# Question 3
print("\nQuestion 3: Quel est le plus grand pays du monde par superficie ?")
options = ["A: Canada", "B: Chine", "C: Russie", "D: Etats-Unis"]
print("  " + "   ".join(options))
reponse5 = input(joueur1 + ", ta réponse: ")
reponse6 = input(joueur2 + ", ta réponse: ")

# Question 4
print("\nQuestion 4: Quel est l'élément chimique dont le symbole est 'O' ?")
options = ["A: Or", "B: Oxygène", "C: Argent", "D: Fer"]
print("  " + "   ".join(options))
reponse7 = input(joueur1 + ", ta réponse: ")
reponse8 = input(joueur2 + ", ta réponse: ")

# Question 5
print("\nQuestion 5: Quel est le plus long fleuve du monde ?")
options = ["A: Nil", "B: Amazone", "C: Yangtsé", "D: Mississippi"]
print("  " + "   ".join(options))
reponse9 = input(joueur1 + ", ta réponse: ")
reponse10 = input(joueur2 + ", ta réponse: ")


# --- Calcul des scores et messages motivants ---
import re

# mettre les réponses des joueurs dans des listes (ordre Q1..Q5)
answers_j1 = [reponse1, reponse3, reponse5, reponse7, reponse9]
answers_j2 = [reponse2, reponse4, reponse6, reponse8, reponse10]

# bonnes réponses (lettres)
correct = ['C', 'C', 'C', 'B', 'A']

def normalize(resp):
    if not resp:
        return ''
    resp = str(resp).upper()
    m = re.search(r'[A-D]', resp)
    return m.group(0) if m else resp.strip()[:1]

def score_and_feedback(answers):
    score = 0
    details = []
    for i, a in enumerate(answers):
        ans = normalize(a)
        ok = ans == correct[i]
        details.append((i+1, a, ans, correct[i], ok))
        if ok:
            score += 1
    # message motivant selon le score
    if score == 5:
        msg = "Parfait ! Tu es un(e) champion(ne) 🎉"
    elif score >= 4:
        msg = "Super travail ! Continue comme ça 👍"
    elif score >= 2:
        msg = "Bien joué — tu peux encore t'améliorer 🙂"
    else:
        msg = "Courage — essaie encore, tu vas y arriver 💪"
    return score, msg, details

score1, msg1, details1 = score_and_feedback(answers_j1)
score2, msg2, details2 = score_and_feedback(answers_j2)

print("\nRésultats :")
print(f"{joueur1} — score: {score1}/5 — {msg1}")
print(f"{joueur2} — score: {score2}/5 — {msg2}\n")

print("Détail des réponses (Q#, réponse brute → lettre normalisée, bonne lettre, OK):")
for d in details1:
    print(f"{joueur1} Q{d[0]}: {d[1]} → {d[2]} (attendu: {d[3]})  {'✓' if d[4] else '✗'}")
for d in details2:
    print(f"{joueur2} Q{d[0]}: {d[1]} → {d[2]} (attendu: {d[3]})  {'✓' if d[4] else '✗'}")

print("\nMerci d'avoir participé au questionnaire.")

# --- Résumé motivant et enregistrement des meilleurs scores ---
import json
import os

# Déterminer le vainqueur et afficher un message
if score1 > score2:
    print(f"\n🏆 {joueur1} a gagné ! Bravo 🎉")
elif score2 > score1:
    print(f"\n🏆 {joueur2} a gagné ! Bravo 🎉")
else:
    print("\n🤝 Match nul ! Bien joué à tous les deux.")

# Sauvegarder les meilleurs scores dans best_scores.json (dans le même dossier)
best_path = os.path.join(os.path.dirname(__file__), "best_scores.json")
try:
    if os.path.exists(best_path):
        with open(best_path, "r", encoding="utf-8") as f:
            best = json.load(f)
    else:
        best = {}

    updated = False
    for name, sc in ((joueur1, score1), (joueur2, score2)):
        prev = best.get(name, 0)
        if sc > prev:
            best[name] = sc
            print(f"🎯 Nouvel record pour {name}: {sc}/5 (ancien : {prev}/5)")
            updated = True

    if updated:
        with open(best_path, "w", encoding="utf-8") as f:
            json.dump(best, f, ensure_ascii=False, indent=2)
    else:
        print("Aucun nouveau record cette fois — continue comme ça !")

except Exception as e:
    print("⚠️ Erreur lors de la sauvegarde des scores :", e)

# Conseils personnalisés selon le score
for name, sc in ((joueur1, score1), (joueur2, score2)):
    if sc == 5:
        advice = "Parfait ! Garde cette constance et aide les autres 👏"
    elif sc >= 4:
        advice = "Très bien — révise une ou deux questions pour être imbattable."
    elif sc >= 2:
        advice = "Bien débuté — travaille les thèmes manquants et recommence."
    else:
        advice = "Courage — lis quelques fiches de géographie et réessaie bientôt."
    print(f"{name} — conseil : {advice}")

print("\nMerci encore d'avoir joué — continue à t'entraîner !")
