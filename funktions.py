'''
Kseniya Shkadarevich
14.08.2024
Implementiert Spielfunktionen wie Bewertung, Feedback 1 und Feedback 2.
Quellen:
- Zurückgeben von mehreren Werten in einer Python-Funktion: https://stackoverflow.com/questions/354883/alternatives-for-returning-multiple-values-from-a-python-function
- Verwendung von colorama-Bibliothek für farbigen Text im Terminal in Python: https://www.geeksforgeeks.org/print-colors-python-terminal/
- Verwendung von colorama-Bibliothek für farbigen Text im Terminal in Python:https://medium.com/ai-does-it-better/print-colored-text-in-python-enhance-terminal-output-b90aede058c8
'''
import report
import text
import random
import events
import time
from nltk.corpus import reuters
from colorama import init, Fore, Style

init()

noten = ["1.0", "1.3", "1.7", "2.0", "2.3", "2.7", "3.0", "3.3",
         "3.7", "4.0", "4.3", "4.7", "5.0"]
clarify_used = False


def grading(x, energy_level_chocolate_grading, grading_number, current_state):
    """
    Führt den Bewertungsprozess durch und verwaltet das Energielevel des Spielers.

    Args:
        x (int): Der Index des aktuellen Schülers in der Liste.
        energy_level_chocolate_grading (list): Liste, die den Einsatz von Schokolade in dieser Bewertungsrunde anzeigt.
        grading_number (int): Die aktuelle Bewertungsrunde (1 oder 2).
        current_state (str): Der aktuelle Zustand des Spiels (z.B. "grade1", "grade2").

    Returns:
        tuple: 
    """
    text.prt("grading")
    while x < 8:
        if report.EnergyLevel <= 0:
            text.prt("energy_gameover")
            current_state = "end"
            return x, current_state
        elif report.EnergyLevel <= 5:
            print(
                Fore.BLUE + "\nAchtung, dein Energielevel beträgt unter 5EP!" + Style.RESET_ALL)

        print("\nBitte gibt die Note für " +
              report.Students[x] + " ein. Oder möchtest du lieber eine Pause nehmen?")
        i = input(Fore.GREEN + ">>> " + Style.RESET_ALL).lower().strip()

        if i == 'inspect report':
            report.Semester_Report()
            continue

        if i == 'exit':
            print("Spiel verlassen.")
            exit()
        if i == 'rest':
            text.prt("rest_" + str(random.randint(1, 2)))
            report.EnergyLevel += 5

        if i == 'eat chocolate':
            if energy_level_chocolate_grading[grading_number] == 1:
                text.prt("chocolate_error")
            else:
                text.prt("chocolate")
                report.EnergyLevel += 10
                energy_level_chocolate_grading[grading_number] = 1

        if i in noten:
            if grading_number == 1:
                report.Grades1[x] = i
            elif grading_number == 2:
                report.Grades2[x] = i

            report.EnergyLevel -= 5
            if report.EnergyLevel <= 0:
                text.prt("energy_gameover")
                current_state = "end"
                return x, current_state
            print(Fore.GREEN + f"\nDie Note {i} für {
                  report.Students[x]} wurde eingetragen." + Style.RESET_ALL)

            events.events()

        elif i == 'rest' or i == 'eat chocolate':
            print("Dein Energielevel beträgt jetzt: " +
                  str(report.EnergyLevel) + "EP" + "\n")
            x -= 1
        else:
            print("\nDie Note ist ungültig. Bitte versuche es erneut.")
            x -= 1
        x += 1
    print("Du hast alle Noten eingetragen. \n")
    return x, current_state


def feedback_1():
    """
    Führt das erste Feedback-Spiel durch, bei dem der Spieler ein zufälliges Thema erraten muss.

    Args:
        Keine.

    Returns:
        int: Die erreichten Evaluationspunkte.
    """
    global clarify_used
    report.evaluation_points = 0
    categories_seen = set()

    text.prt("feedback1_introduction")

    for i in range(3):
        clarify_used = False
        while True:

            categories = reuters.categories()
            random_category = random.choice(categories)
            if random_category not in categories_seen:
                categories_seen.add(random_category)
                break

        valid_sents = []
        for sent in reuters.sents(categories=random_category):
            if len(sent) <= 20 and sum(1 for token in sent if token[0].isdigit()) <= 3:
                masked_sent = []
                for token in sent:
                    if random_category.lower() in token.lower():
                        masked_sent.append("[HIDDEN]")
                    else:
                        masked_sent.append(token)

                valid_sents.append(masked_sent)

        if not valid_sents:
            print("Keine geeigneten Sätze gefunden.")
            continue

        random_sentence = random.choice(valid_sents)

        # print("\nThema:", random_category)  # Hinweis auf das Thema
        print("\nFrage", len(categories_seen))
        print("Du hast 3 Versuche und 1 Minute Zeit.")
        print("\nSatz:", " ".join(random_sentence))

        other_sentences = []
        for sent in reuters.sents(categories=random_category):
            if sent != random_sentence and len(sent) <= 20 and sum(1 for token in sent if token[0].isdigit()) <= 3:
                masked_sent = []
                for token in sent:
                    if random_category.lower() in token.lower():
                        masked_sent.append("[HIDDEN]")
                    else:
                        masked_sent.append(token)
                other_sentences.append(masked_sent)

        attempt = 1

        while attempt <= 3:
            print(f"\nVersuch {attempt}")
            start_time = time.time()
            guess = input(
                Fore.GREEN + ">>> Rate das Thema (oder 'clarify' für einen Tipp):" + Style.RESET_ALL).lower().strip()
            elapsed_time = time.time() - start_time

            if elapsed_time > 60:
                text.prt("feedback_gameover_time")
                return

            if guess == random_category.lower():
                if attempt == 1:
                    report.evaluation_points += 40
                elif attempt == 2:
                    report.evaluation_points += 30
                else:
                    report.evaluation_points += 20
                print(Fore.GREEN + f"\nRichtig! Du hast {
                      (5 - attempt) * 10} Evaluationspunkte erhalten." + Style.RESET_ALL)
                break

            elif guess == 'clarify':
                if not clarify_used:
                    if other_sentences:
                        other_sentence = random.choice(other_sentences)
                        print("\nTipp:", " ".join(other_sentence))
                        clarify_used = True
                    else:
                        print("Keine weiteren Sätze verfügbar.")
                else:
                    print("\nDu hast den Tip bereits verwendet.")
                    continue
            elif guess == 'exit':
                print("Spiel verlassen.")
                exit()
            else:
                print("\nFalsch!")
                attempt += 1

            if attempt > 3:
                print('-'*60)
                print(Fore.RED + "\nOh, schade! Das Thema war " +
                      random_category + Style.RESET_ALL)
                text.prt("feedback1_gameover")
                return

        print("\nAktuelle Evaluationspunkte:", report.evaluation_points)

    print(Fore.GREEN + f"\nDu hast insgesamt {
          report.evaluation_points} Evaluationspunkte erreicht." + Style.RESET_ALL)
    return report.evaluation_points


def is_valid_code_sentence(sentence):
    """
    Rekursiv überprüft, ob der gegebene Codesatz nach bestimmten Regeln gültig ist.

    Args:
        sentence (str): Der zu prüfende Codesatz.

    Returns:
        bool: True, wenn der Codesatz gültig ist, sonst False.
    """

    tokens = sentence.split()
    n = len(tokens)

    def check_tokens(i):

        if i >= n - i - 1:
            if n % 2 == 1 and i == n // 2:
                return tokens[i][0] < tokens[i][-1]
            return True
        if not (tokens[i][0] <= tokens[n - i - 1][0] and tokens[n - i - 1][-1] <= tokens[i][-1]):
            return False
        return check_tokens(i + 1)
    return check_tokens(0)


def feedback_2():
    """
    Führt das zweite Feedback-Spiel durch, bei dem der Benutzer einen gültigen Codesatz eingeben muss.

    Args:
        Keine.

    Returns:
        int: Die erreichten Evaluationspunkte.
    """
    text.prt("feedback2_introduction")
    for attempt in range(3):
        code_sentence = input(
            Fore.GREEN + ">>> Gib einen Codesatz ein: " + Style.RESET_ALL).lower().strip()
        if is_valid_code_sentence(code_sentence):
            report.evaluation_points += 80
            print(
                Fore.GREEN + "\nDer Codesatz war gültig! Du erhältst 80 Evaluationspunkte." + Style.RESET_ALL)
            break
        else:
            print("\nUngültiger Codesatz, versuch es erneut.")
    else:
        text.prt("feedback2_gameover")
        return
    return report.evaluation_points
