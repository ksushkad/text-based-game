'''
Kseniya Shkadarevich
14.08.2024
Anzeigen der Leistungsübersicht; Verwalten und Zurücksetzen von Spielzuständen.
Quellen:
- Verwenden von .ljust() zum Erweitern eines Strings auf eine bestimmte Länge: https://stackoverflow.com/questions/5676646/how-can-i-fill-out-a-python-string-with-spaces
'''


import random
from nltk.corpus import names

EnergyLevel = 10
evaluation_points = 0
Students = [""] * 8
Grades1 = [0] * 8
Grades2 = [0] * 8


def setup_student_names():
    """
    Setzt zufällige Namen für die Studenten im Spiel.
    """
    for i in range(8):
        student_names = names.words()[random.randint(
            0, len(names.words()) - 1)]
        Students[i] = student_names


def Semester_Report():
    """
    Gibt den aktuellen Semesterbericht des Spiels aus.
    """
    print("\n------------- SEMESTER REPORT ------------- ")
    print("Energy Level: " + str(EnergyLevel) +
          "     Evaluation: " + str(evaluation_points) + "\n")
    print("Grades:")
    for i in range(8):
        if Grades1[i] == 0:
            StGrades1 = " - "
        else:
            StGrades1 = str(Grades1[i])
        if Grades2[i] == 0:
            StGrades2 = " - "
        else:
            StGrades2 = str(Grades2[i])
        print(Students[i].ljust(14) + ": " +
              StGrades1 + " / " + StGrades2)


def reset_game_state():
    """
    Setzt alle relevanten Spielzustände auf die Ausgangswerte zurück.
    """
    global EnergyLevel, evaluation_points, Students, Grades1, Grades2
    EnergyLevel = 10
    evaluation_points = 0
    Students = [""] * 8
    Grades1 = [0] * 8
    Grades2 = [0] * 8
    setup_student_names()
