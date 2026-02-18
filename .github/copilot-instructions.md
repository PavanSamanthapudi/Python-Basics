# Copilot Instructions for AI Agents

## Project Overview
This workspace is a collection of beginner-friendly Python exercises and Jupyter notebook assignments focused on real-world logic, conditionals, and user input. It is designed for educational purposes, with each scenario implemented as a self-contained code cell or script.

## Key Files & Structure
- `21-01-26-Assignment.ipynb`: Main Jupyter notebook with assignment problems and solutions. Each problem is described in a markdown cell, followed by a code cell with the implementation.
- `1.py`: Minimal Python script (currently a "Hello World" example).
- `venv-1/`: Python virtual environment for dependency isolation. Do not modify or commit changes here.

## Patterns & Conventions
- Each notebook problem is independent; do not assume shared state between cells unless explicitly stated.
- User input is collected using `input()` and processed immediately in the same cell.
- Boolean logic is often based on string comparison (e.g., `input() == "Yes"` or `input() == "True"`).
- Output is printed directly using `print()`.
- Variable names are descriptive and match the scenario (e.g., `total_bill`, `access_code`).
- No external libraries are used except for standard Python and Jupyter features.

## Developer Workflows
- To run or test a scenario, execute the corresponding code cell in the notebook.
- For scripts, run with the Python interpreter from the project root (ensure the virtual environment is activated):
  ```
  venv-1\Scripts\activate
  python 1.py
  ```
- No build or test automation is present; all code is intended for direct execution and manual inspection.

## Integration & Dependencies
- No external APIs or services are integrated.
- All dependencies are managed via the `venv-1` virtual environment. Do not install packages globally.

## Examples
- See `21-01-26-Assignment.ipynb` for patterns such as:
  - Collecting user input for multiple independent conditions
  - Using if/elif/else for scenario branching
  - Calculating totals based on user choices

## Special Notes
- Do not add new dependencies or frameworks unless explicitly required by an assignment.
- Preserve the educational, step-by-step style when adding new problems or solutions.
- Keep all new code self-contained and easy to follow for beginners.
