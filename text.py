'''
Kseniya Shkadarevich
14.08.2024
Gibt den Inhalt einer Textdatei aus dem Verzeichnis ./txt/ basierend auf dem Dateinamen aus
Quellen:
- Dateiein- und -ausgabe (prt Funktion): https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
- Verwenden von UTF-8 beim Lesen von Dateien in Python.: https://www.w3docs.com/snippets/python/unicode-utf-8-reading-and-writing-to-files-in-python.html
'''


def prt(filename):
    """
    Liest den Inhalt einer Textdatei und gibt ihn auf der Konsole aus.

    Args:
        filename (str): Der Name der Datei (ohne Pfad und Erweiterung), die aus dem Ordner './txt/' gelesen werden soll.

    Returns:
        None
    """
    with open('./txt/' + filename + '.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    print("\n" + content)
