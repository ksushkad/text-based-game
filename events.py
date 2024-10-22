'''
Kseniya Shkadarevich
14.08.2024
Verwalten von zufälligen Ereignissen, die den Energielevel des Spielers nach jeder Note beeinflussen.
Quellen:
- Verwenden von relativen Gewichten zur Auswahl von Elementen mit unterschiedlicher Wahrscheinlichkeit: https://pynative.com/python-weighted-random-choices-with-probability/
'''


import random
import text
import report


def events():
    """
    Führt ein zufälliges Ereignis nach jeder Noteneingabe aus. 
    """
    events = ["extention", "reevaluation", "debugging", "thanks"]
    event_probabilities = [0.2, 0.2, 0.3, 0.1]

    event = random.choices(events, event_probabilities)[0]

    if event == "extention":
        text.prt("extention")
        report.EnergyLevel -= 3
    elif event == "reevaluation":
        text.prt("reevaluation")
        report.EnergyLevel -= 2
    elif event == "debugging":
        text.prt("debugging")
        report.EnergyLevel -= 1
    elif event == "thanks":
        text.prt("thanks")
        report.EnergyLevel += 3
