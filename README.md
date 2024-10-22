
# Game Title: Semester Evaluation Game

## Description

The **Semester Evaluation Game** is a text-based game where you take on the role of a tutor. Your goal is to assess students, provide feedback, and manage your energy throughout the semester. You must grade assignments, collect energy points, and encounter various random events along the way. Your decisions impact the evaluation and the final outcome of the course.

## Installation

### Requirements

-   **Python 3** is required.
-   The game uses the **nltk** library and the **Reuters corpus**.
-   **Colorama** for colored console output.

### Package Installation

1.  Ensure that **Python 3** is installed. (Official download link: [https://www.python.org/downloads/](https://www.python.org/downloads/))
2.  Install the necessary **nltk** library:
    ``` 
    pip install nltk
    ```
3. Download the Reuters corpus and Names corpus by executing the following in a Python interpreter:
    ``` 
    import nltk
    nltk.download('reuters')
    nltk.download('names')
    nltk.download('punkt_tab')
   ```
  4. **Install the `colorama` library**: Run the following command in the command line:
      ``` 
      pip install colorama
      ```

### Game Installation

1.  Download the project and unzip it into a directory of your choice.
2.  Ensure that the following files are included in the directory:
    -   `main.py`
    -   `scenes.py`
    -   `text.py`
    -   `menu.py`
    -   `report.py`
    -   `function.py`
    -   `events.py`
    -   A folder named **text**, which contains scene descriptions in the form of text files.

## Usage

### Starting the Game

1.  Open a terminal or command prompt.
2.  Navigate to the directory where the files are located.
3.  Run the game with the following command:
- **macOS**: 
  ```bash 
  python3 main.py 
  ```
-  **Windows**, **Linux/UNIX**: 
   ```bash 
   python main.py 
   ``` 
   _Note_: If `python` does not work, try instead:
   ```bash 
   python3 main.py 
   ```

### Controls

-   **Grade**: `grade`
-   **Inspect report**: `inspect report`
-   **Give feedback**: `give feedback`
-   **Take a break**: `rest`
-   **Eat chocolate**: `eat chocolate`
-   **Exit game**: `exit`
-   **Delay grading**: `delay grade`
-   **Get evaluation**: `get eval`

### Example

After starting the game, you can check your status with the command `inspect report`. Then, begin grading the students by entering `grade`. Each time you enter a grade, you lose energy points, but you can regain energy by taking breaks (`rest`) or eating chocolate (`eat chocolate`).

_Visual Representation_: [Screenshots](https://photos.app.goo.gl/EeZqXSrubCLTwU5c8)

## Support

If you have any questions or issues, you can reach me at kseniya.shkadarevich@uni-potsdam.de.

## Roadmap

Future ideas for the game:

-   Expanding the feedback puzzles.
-   Adding more events and random factors that influence the course of the game.

## Authors and Acknowledgments

-   **Kseniya Shkadarevich** – Author of the game
