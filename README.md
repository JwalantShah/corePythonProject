# Programming Universe of Jwalant

A menu-driven Python application that bundles many small programs behind one console menu. Pick a number, the program runs, and you return to the menu when it finishes.

> **Status:** draft. Sections marked `TODO` need details from the rest of the project.

## Features

- Interactive console main menu with coloured output
- Programs are discovered automatically: drop a new `.py` file into `projectData/Programs/` and it appears in the menu, with no changes to the menu code
- Each menu entry is labelled with the program's own module docstring
- Modules are imported once and cached, so the menu redraws quickly
- Input validation: non-numeric or out-of-range choices show a friendly message instead of crashing
- Type `0` to exit

<!-- TODO: list the actual programs once the Programs folder is shared -->

## Requirements

- Python 3.8 or newer (`TODO`: confirm the minimum version)
- `TODO`: list any third-party packages used by `globalUDFs.py` or the programs

## Installation

```bash
git clone <your-repository-url>
cd <project-folder>
# pip install -r requirements.txt   # if applicable
```

## Usage

Run the main file from the project root (the folder that contains `projectData/`):

```bash
python main.py   # TODO: replace main.py with your actual file name
```

You will see a menu like this:

```
---------------- : WELCOME TO THE PROGRAMING UNIVERSE OF JWALANT : ----------------

PRESS 1. <docstring of first program>
PRESS 2. <docstring of second program>
...
PRESS 0. TO EXIT

ENTER YOUR CHOICE HERE :
```

Enter the number of the program you want. Enter `0` to exit.

## Project Structure

```
.
├── main.py                      # Main menu (TODO: confirm file name)
└── projectData/
    ├── Programs/                # One module per program shown in the menu
    │   ├── <program_one>.py
    │   └── <program_two>.py
    └── SupportScripts/
        └── globalUDFs.py        # Shared helpers: colorPrint, valInput, ...
```

## Adding a New Program

1. Create a new file in `projectData/Programs/`, for example `my_program.py`.
2. Start the file with a module docstring. This text becomes the menu label.
3. Define a `main()` function, which the menu calls when the program is chosen.

```python
"""My Program: a short description shown in the menu."""


def main():
    print("Hello from my program!")
```

Files whose names start with `_` are ignored, as are files that do not end in `.py`.

## Shared Helpers

`projectData/SupportScripts/globalUDFs.py` provides utilities used across the project, including:

- `colorPrint(text, colour)`: print coloured text to the console
- `valInput(prompt, error_message, default)`: read and validate numeric input

<!-- TODO: document any other helpers -->

## Contributing

Contributions are welcome. Fork the repository, create a branch, and open a pull request.

## License

TODO: choose a license (for example MIT) and add a `LICENSE` file.

## Author

Jwalant (TODO: add GitHub link or contact details)
