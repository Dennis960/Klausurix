# Klausurix

## Development Setup

### Required Software

- Visual Studio Code

  - Install the recommended extensions (have a look at `.vscode/extensions.json`)

- Python 3.8 or higher
  - Make sure to add Python to your PATH

### Clone the repository

- Open a Terminal
- Run `git clone https://github.com/DirkJLehmann/Klausurix`

### Python venv (optional)

- Open a Terminal in the root folder of this repository
- Run `python3 -m venv venv`

For Windows:

- Run `venv\Scripts\activate`

For Linux:

- Run `source venv/bin/activate`

### Install dependencies

- Run `pip install -r requirements.txt`

### Run the application

- **Requires venv to be setup**: Run the vscode launch configuration `Run Klausurix`. For this, press `F5` or open the debug tab on the left and click on the green play button.
- Alternatively, run `python src/main.py`

## Tests

- **Requires venv to be setup**: Run the vscode launch configuration `Test Klausurix`.
- Alternatively, run `python src/run_tests.py`.
