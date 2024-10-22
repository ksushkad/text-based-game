'''
Kseniya Shkadarevich
14.08.2024
Verwaltung und Anzeige der verfügbaren Optionen für verschiedene Spielzustände.
Quellen:
'''

m_grading = ["grade", "inspect report", "exit", "delay grade"]
m_feedback = ["give feedback", "inspect report", "exit"]
m_evaluation = ["get eval", "inspect report", "exit"]
m_end = ["play again", "inspect report", "exit"]
m_all_actions = ["grade", "rest", "eat chocolate",
                 "give feedback", "get eval", "delay grade", "play again"]
m_all_states = ["grade1", "feedback1",
                "grade2", "feedback2", "evaluation", "end"]


def grading():
    """
    Zeigt die verfügbaren Optionen für die Bewertungsphase (grading) an.
    """
    tx = "Your options: "
    for i in range(len(m_grading) - 1):
        tx = tx + m_grading[i] + " | "
    tx = tx + m_grading[len(m_grading) - 1]
    print(tx)


def feedback():
    """
    Zeigt die verfügbaren Optionen für die Feedbackphase an.
    """
    print("\nWie möchtest du nun fortfahren?\n")
    tx = "Your options: "
    for i in range(len(m_feedback) - 1):
        tx = tx + m_feedback[i] + " | "
    tx = tx + m_feedback[len(m_feedback) - 1]
    print(tx)


def evaluation():
    """
    Zeigt die verfügbaren Optionen für die Evaluationsphase an.
    """
    print("\nWie möchtest du nun fortfahren?\n")
    tx = "Your options: "
    for i in range(len(m_evaluation) - 1):
        tx = tx + m_evaluation[i] + " | "
    tx = tx + m_evaluation[len(m_evaluation) - 1]
    print(tx)


def end():
    """
    Zeigt die verfügbaren Optionen für das Spielende an.
    """
    print("\nWie möchtest du nun fortfahren?\n")
    tx = "Your options: "
    for i in range(len(m_end) - 1):
        tx = tx + m_end[i] + " | "
    tx = tx + m_end[len(m_end) - 1]
    print(tx)
