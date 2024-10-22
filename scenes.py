'''
Kseniya Shkadarevich
14.08.2024
Koordiniert Zustandsverwaltung in dem Spiel
Quellen:
- Zurückgeben von mehreren Werten in einer Python-Funktion: https://stackoverflow.com/questions/354883/alternatives-for-returning-multiple-values-from-a-python-function
- Verwendung von colorama-Bibliothek für farbigen Text im Terminal in Python: https://www.geeksforgeeks.org/print-colors-python-terminal/
- Verwendung von colorama-Bibliothek für farbigen Text im Terminal in Python:https://medium.com/ai-does-it-better/print-colored-text-in-python-enhance-terminal-output-b90aede058c8
'''

import text
import menu
import funktions
from colorama import init, Fore, Style

init()


def handle_grading_success(i, current_state, feedback_state, success_message):
    """
    Verarbeitet den Abschluss des Bewertungsprozesses und aktualisiert den Zustand des Spiels.

    Args:
        i (str): Die aktuelle Benutzereingabe, die eine Aktion im Spiel darstellt.
        current_state (str): Der aktuelle Zustand des Spiels (z. B. "grade1", "grade2").
        feedback_state (str): Der nächste Feedback-Zustand (z. B. "feedback1", "feedback2").
        success_message (str): Die Nachricht, die bei erfolgreichem Abschluss der Bewertung angezeigt wird.

     Returns:
        str: Die nächste Benutzereingabe nach Abschluss des Feedback-Menüs.
        str: Der aktualisierte Zustand des Spiels nach dem Feedback.
    """
    current_state = feedback_state
    if i == "grade":
        text.prt(success_message)
    menu.feedback()

    return input(Fore.GREEN + ">>> " + Style.RESET_ALL).lower().strip(), current_state


def handle_feedback(current_state, grading_number):
    """
    Verarbeitet den Feedback-Prozess und aktualisiert den Zustand und die Bewertungsrunde.

    Args:
        current_state (str): Der aktuelle Feedback-Zustand, entweder "feedback1" oder "feedback2".
        grading_number (int): Die aktuelle Bewertungsrunde (1 oder 2).

    Returns:
        Returns:
        str: Die nächste Benutzereingabe nach dem Feedback-Prozess.
        str: Der aktualisierte Zustand des Spiels.
        int: Die neue Bewertungsrunde (z. B. 2 für die zweite Bewertungsrunde).
    """
    if current_state == "feedback1":
        if not funktions.feedback_1():
            current_state = "end"
            return current_state, current_state, grading_number
        text.prt("feedback1_success")
        current_state = "grade2"
        grading_number = 2
        menu.grading()

    elif current_state == "feedback2":
        if not funktions.feedback_2():
            current_state = "end"
            return current_state, current_state, grading_number
        text.prt("feedback2_success")
        current_state = "evaluation"
        menu.evaluation()

    return input(Fore.GREEN + ">>> " + Style.RESET_ALL).lower().strip(), current_state, grading_number
