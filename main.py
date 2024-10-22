'''
Autorin: Kseniya Shkadarevich
Datum: 14.08.2024
Zweck der Datei: Verwalten des Spielablaufs und der Zustände
Quellen:
- Verwendung von Klassen und Methoden in Python: https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self-in-python
- Zurückgeben von mehreren Werten in einer Python-Funktion: https://stackoverflow.com/questions/354883/alternatives-for-returning-multiple-values-from-a-python-function
- Verwendung von colorama-Bibliothek für farbigen Text im Terminal in Python: https://www.geeksforgeeks.org/print-colors-python-terminal/
- Verwendung von colorama-Bibliothek für farbigen Text im Terminal in Python:https://medium.com/ai-does-it-better/print-colored-text-in-python-enhance-terminal-output-b90aede058c8
'''

import report
import text
import menu
import funktions
import scenes
from colorama import init, Fore, Style


class Game:
    def __init__(self):
        """
        Initialisiert die Klasse Game und setzt die Ausgangswerte.

        Attributes:
            grading_number (int): Nummer der aktuellen Bewertungsrunde.
            energy_level_chocolate_grading (list): Liste, die den Schokoladen-Energiewert für jede Runde speichert.
            current_state (str): Der aktuelle Zustand des Spiels.
        """
        self.grading_number = 1
        self.energy_level_chocolate_grading = [0] * 3
        self.current_state = "grade1"

    def reset(self):
        """
        Setzt den Spielzustand auf die Ausgangswerte zurück.
        """
        report.reset_game_state()
        self.energy_level_chocolate_grading = [0] * 3
        self.grading_number = 1
        self.current_state = "grade1"

    def play_game(self):
        """
        Startet und verwaltet den Hauptablauf des Spiels, einschließlich der Spielzustände.
        """
        init()
        self.reset()
        text.prt("introduction")
        menu.grading()
        x = 0

        i = input(Fore.GREEN + ">>> " + Style.RESET_ALL).lower().strip()

        while i != 'exit':
            if i == 'inspect report':
                report.Semester_Report()
                i = input(Fore.GREEN + ">>> " +
                          Style.RESET_ALL).lower().strip()

            elif i == "delay grade" and self.current_state in {"grade1", "grade2"}:
                x = 8

            elif i == 'grade' and self.current_state in {"grade1", "grade2"}:
                x = 0
                x, self.current_state = funktions.grading(x, self.energy_level_chocolate_grading,
                                                          self.grading_number, self.current_state)
                if self.current_state == "end":
                    break

            elif i == "give feedback" and self.current_state in {"feedback1", "feedback2"}:
                i, self.current_state, self.grading_number = scenes.handle_feedback(
                    self.current_state, self.grading_number)
                x = 0
                if self.current_state == "end":
                    break

            elif i == "get eval" and self.current_state == "evaluation":
                text.prt("evaluation")
                self.current_state = "end"
                break

            elif i in menu.m_all_actions and self.current_state in menu.m_all_states:
                print("Dieses Befehl ist noch nicht verfügbar")
                i = input(Fore.GREEN + ">>> " +
                          Style.RESET_ALL).lower().strip()

            else:
                print("Ungültiger Befehl, bitte versuche es erneut")
                i = input(Fore.GREEN + ">>> " +
                          Style.RESET_ALL).lower().strip()

            if x == 8 and i in {"grade", "delay grade"}:
                if self.current_state == "grade1":
                    i, self.current_state = scenes.handle_grading_success(i,
                                                                          self.current_state, "feedback1", "grading1_success")
                elif self.current_state == "grade2":
                    i, self.current_state = scenes.handle_grading_success(i,
                                                                          self.current_state, "feedback2", "grading2_success")

        if self.current_state == "end":
            while True:
                menu.end()
                i = input(Fore.GREEN + ">>> " +
                          Style.RESET_ALL).lower().strip()
                if i == "play again":
                    self.play_game()
                    break
                elif i == "inspect report":
                    report.Semester_Report()
                elif i == 'exit':
                    print("Spiel verlassen.")
                    exit()
                else:
                    print("Ungültiger Befehl, bitte versuche es erneut")


game = Game()
game.play_game()
