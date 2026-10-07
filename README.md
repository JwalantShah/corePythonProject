# Programming Universe of Jwalant

A menu-driven Python console application that bundles a collection of small programs behind one coloured main menu: a student database, pattern drawing, matrix multiplication, a family of number-theory explorers, and threading demos. Pick a number, the program runs, and `0` returns you to the menu.

## Features

- **Auto-discovered menu.** Every `.py` file in `projectData/Programs/` becomes a menu entry, labelled with its module docstring. Files starting with `_` are hidden from the menu.
- **Coloured console UI** using ANSI escape codes (no extra dependency).
- **Validated input helpers** that re-prompt instead of crashing on bad input.
- **Persistent data** for the student database and the number programs, stored under `projectData/Data/`.

## Programs

| Program | What it does |
|---|---|
| **Student Database** (`studentDirectory`) | CRUD operations on student records held in a dictionary. Add students (roll number format like `09DCE212`, three subject marks from 0 to 100), update a name or marks, delete, and list everyone in a table. Data is saved to a pickle file, plus text files for marks and grades (A: 80 to 100, B: 60 to <80, C: 40 to <60). |
| **Design Pattern** (`designPattern`) | Draws triangle and diamond patterns using any character or string you choose, with a configurable number of lines. Also generates a **word made of a pattern**: choose full or broken, bold or normal, solid or hollow, and one of several colour schemes (including tri-colour). |
| **Matrix Multiplication** (`matrixMultiplication`) | Enter the dimensions and elements of two matrices, check that they can be multiplied, and see the multiplication worked out step by step. |
| **Numbers** (`numbers`) | A sub-menu of number-theory programs, listed below. |
| **Thread demo** (`thread`) | Demonstrates threading: a shared counter without protection, and a bank balance protected with `threading.Lock`. |
| **Test** (`test`) | A scratch file for trying out snippets (comprehensions, `bytearray` and `memoryview`, `namedtuple`, generators, `itertools`, threads). |

### Numbers sub-menu

| Program | Options |
|---|---|
| **Armstrong Numbers** | Check a number, first N, between two numbers, N above or below a number, status of the precomputed list |
| **Fibonacci Numbers** | Check a number, first N, between two numbers, N after or before a number, Nth term, terms between positions M and N |
| **Harshad (Niven) Numbers** | Check a number, first N, between two numbers, N after or before a number |
| **Perfect, Deficient and Abundant Numbers** | Classify a number, first N of each type, in a range, N above or below a number |
| **Prime Numbers** | Check a number (shows the divisor when it is composite), primes up to N or between two numbers, a **timed generator** that runs for the minutes you enter and appends results to a text file, a log viewer, and a setting for how many primes print per line |
| **Misc Numbers** | Factorial and palindrome check (Harshad and triangular numbers are still in progress) |

## Requirements

- Python 3.8 or newer
- [`tabulate`](https://pypi.org/project/tabulate/) (prime generation log table)
- [`prettytable`](https://pypi.org/project/prettytable/) (student list table)

```bash
pip install tabulate prettytable
```

## Installation

```bash
git clone <your-repository-url>
cd <project-folder>
pip install tabulate prettytable
```

## Usage

Run the main menu script from the project root, the folder that **contains** `projectData/`. The programs open data files using paths relative to this folder, so running from elsewhere will break them.

```bash
python main.py
```

You will see a menu like this (the entries come from each program's docstring, so the order may vary):

```
---------------- : WELCOME TO THE PROGRAMING UNIVERSE OF JWALANT : ----------------

PRESS 1. PROGRAM TO DEMONSTRATE CRUD OPERATION ON TEXT FILE.USING STUDENT DATA IN DICTIONARY
PRESS 2. PROGRAM TO DEMONSTRATE THE DESIGNING OF VARIOUS SHAPES WITH PATTERN
PRESS 3. PROGRAM TO DEMONSTRATE THE MULTIPLICATION OF TWO DYNAMICALLY GENERATED MATRIX
PRESS 4. PROGRAM TO DEMONSTRATE VARIOUS NUMBERS LIKE PRIME,ARMSTRONG,PALINDROME NUMBERS
...
PRESS 0. TO EXIT

ENTER YOUR CHOICE HERE :
```

## Project Structure

```
.
├── main.py                          # Main menu
└── projectData/
    ├── Programs/                    # One module per menu entry; each defines main()
    │   ├── studentDirectory.py
    │   ├── designPattern.py
    │   ├── _wordPattern.py          # Hidden from the menu; used by designPattern
    │   ├── matrixMultiplication.py
    │   ├── numbers.py               # Sub-menu that loads Programs/Numbers/*
    │   ├── thread.py
    │   ├── test.py
    │   └── Numbers/
    │       ├── armstrongNumbers.py
    │       ├── fibonacciNumbers.py
    │       ├── harshadNumber.py
    │       ├── perfectNumbers.py
    │       ├── primeNumbers.py
    │       └── miscNumbers.py
    ├── SupportScripts/              # Logic behind each program (the *_SF modules)
    │   ├── globalUDFs.py            # Shared input and colour helpers
    │   ├── studentDirectory_SF.py
    │   ├── designPattern_SF.py
    │   ├── wordPatternSF1.py
    │   ├── matrixMultiPlication_SF.py
    │   └── Numbers/                 # One *_SF.py per number program
    └── Data/
        ├── StudentData/             # StudentData.pkl, studentInfo.txt, studentMarks.txt, A/B/CGrade.txt
        └── Numbers/                 # Cached lists (.pkl), primeNumberList.txt, PrimeNumberLog.txt
```

The code is split in two layers. A file in `Programs/` holds only the menu and user interaction. The matching `*_SF.py` file in `SupportScripts/` holds the actual logic.

## Adding a New Program

1. Create a new file in `projectData/Programs/`, for example `myProgram.py`.
2. Start it with a module docstring. This text becomes the menu label.
3. Define a `main()` function, which the menu calls when the program is chosen.

```python
"""MY PROGRAM: A SHORT DESCRIPTION SHOWN IN THE MENU"""
from projectData.SupportScripts.globalUDFs import *


def main():
    colorPrint('Hello from my program!', 'Green')
```

To keep a helper module out of the menu, start its file name with `_`.

## Shared Helpers

`projectData/SupportScripts/globalUDFs.py` provides:

- `valInput(prompt, error_message, category)`: re-prompting input. Categories: `0` whole number, `1` letters with optional space, `2` letters only, `3` integer or decimal, `4` decimal.
- `rangeInput(low, high, prompt, error_message, category)`: input checked against a range or lower bound.
- `colorPrint(text, colour)` and `colorPrint2(text, text_colour, background_colour)`: coloured output. Colours include Red, Green, Yellow, Blue, Magenta, Cyan, Orange, Pink, Purple and Saffron.

## Data Files

- `Data/Numbers/primeNumberList.txt` is generated by the timed prime generator and keeps growing. It is already about 100 MB, which is above GitHub's 100 MB per-file limit. Add it to `.gitignore` or use [Git LFS](https://git-lfs.com/) if you publish the repository.
- `Data/Numbers/PrimeNumberLog.txt` records each generation run, and the next run resumes after the last prime it logged. Keep it in step with the list file.
- The `.pkl` files are precomputed lists and saved records created by the programs.

## License

TODO: choose a license (for example MIT) and add a `LICENSE` file.

## Author

Jwalant Shah (TODO: add GitHub link or contact details)
