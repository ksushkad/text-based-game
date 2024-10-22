
# Spielname: Semesterbewertungsspiel



## Beschreibung 
Das **Semesterbewertungsspiel** ist ein textbasiertes Spiel, bei dem du die Rolle einer Tutorin übernimmst. Dein Ziel ist es, Studierende zu bewerten, Feedback zu geben und deine Energie während des Semesters zu verwalten. Du musst Aufgaben bewerten, Energiepunkte sammeln und dabei verschiedenen zufälligen Ereignissen begegnen. Deine Entscheidungen beeinflussen die Evaluation und das Endergebnis des Kurses.


## Installation 
### Anforderungen 
- **Python 3** ist erforderlich. 
- Das Spiel verwendet die **nltk**-Bibliothek und das **Reuters-Korpus**. 
- **Colorama** für farbige Konsolenausgaben.
### Installation der Pakete 
1. Stelle sicher, dass **Python 3** installiert ist. (Offizieller Download-Link: [https://www.python.org/downloads/](https://www.python.org/downloads/))
2. Installiere die nötige **nltk**-Bibliothek: 
   ``` 
   pip install nltk
   ```
3. Lade das Reuters-Korpus und Names-Korpus herunter, indem du folgendes in einem Python-Interpreter ausführst:
    ``` 
    import nltk
    nltk.download('reuters')
    nltk.download('names')
    nltk.download('punkt_tab')
   ```
  4. **Installiere die `colorama`-Bibliothek**: Führe folgenden Befehl in der Kommandozeile aus:
      ``` 
      pip install colorama
      ```
### Installation des Spiels

1.  Lade das Projekt herunter und entpacke es in ein Verzeichnis deiner Wahl.
2.  Stelle sicher, dass die folgenden Dateien im Verzeichnis enthalten sind:
    -   `main.py`
    -   `scenes.py`
    -   `text.py`
    -   `menu.py`
    -   `report.py`
    -   `funktion.py`
    -   `events.py`
    -   Ein Ordner namens **text**, der Szenenbeschreibungen in Form von Textdateien enthält.


## Nutzung

### Spiel starten

1.  Öffne ein Terminal oder eine Eingabeaufforderung.
2.  Navigiere in das Verzeichnis, in dem sich die Dateien befinden.
3.  Führe das Spiel mit folgendem Befehl aus:
- **macOS**: 
  ```bash 
  python3 main.py 
  ```
-  **Windows**, **Linux/UNIX**: 
   ```bash 
   python main.py 
   ``` 
   *Hinweis*: Falls `python` nicht funktioniert, versuche stattdessen: 
   ```bash 
   python3 main.py 
   ```
### Steuerung

-   **Bewerten**: `grade`
-   **Bericht inspizieren**: `inspect report`
-   **Feedback geben**: `give feedback`
-   **Pause einlegen**: `rest`
-   **Schokolade essen**: `eat chocolate`
-   **Spiel beenden**: `exit`
-   **Bewertung verzögern**: `delay grade`
-   **Evaluation einholen**: `get eval`
### Beispiel

Nach dem Start des Spiels kannst du den Status mit dem Befehl `inspect report` einsehen. Beginne dann mit der Bewertung der Studierenden, indem du `grade` eingibst. Jedes Mal, wenn du eine Note eingibst, verlierst du Energiepunkte, kannst aber durch Pausen (`rest`) oder Schokoladengenuss (`eat chocolate`) wieder Energie sammeln.

_Visuelle Darstellung_: [Screenshots](https://photos.app.goo.gl/EeZqXSrubCLTwU5c8)


## Support

Bei Fragen oder Problemen kannst du mich über kseniya.shkadarevich@uni-potsdam.de erreichen. 

## Roadmap

Zukünftige Ideen für das Spiel:

-   Erweiterung der Feedback-Rätsel.
-   Hinzufügen weiterer Ereignisse und zufälliger Faktoren, die den Verlauf des Spiels beeinflussen.

## Autoren und Anerkennung

-   **Kseniya Shkadarevich** – Autorin des Spiels



