# Case Study 68: Energy Conservation Before-and-After Analysis

## Problem Statement
Compare energy use before and after a conservation effort, then calculate the energy saved and percentage saved when usage decreases.

## Objectives
1. Read energy use before and after conservation.
2. Validate the entered values.
3. Identify when energy use increased.
4. Calculate and display the amount and percentage saved when usage does not increase.

## Assumptions
- Energy values are entered as numeric units.
- Energy use before conservation must be greater than zero.
- Energy use after conservation cannot be negative.
- A reduction is treated as energy saved; a higher after-value is treated as increased use.

## Algorithm
1. Start and read energy use before and after conservation.
2. If the before-value is not positive or the after-value is negative, display an error.
3. Otherwise, if after-use is greater than before-use, display the increase.
4. Otherwise, calculate energy saved by subtracting after-use from before-use.
5. Calculate the percentage saved using the before-value.
6. Display the energy saved and percentage saved.
7. Stop.

## Python Concepts Used
- Variables and `float()` conversion
- Input and output
- Arithmetic and comparison operators
- `if`, `elif`, and `else`

## Files
- `main.py` — Python program
- `problem_statement.txt` — problem description
- `objectives.txt` — project objectives
- `assumptions.txt` — assumptions
- `algorithm.txt` — step-by-step algorithm
- `pseudocode.txt` — language-independent pseudocode
- `flowchart.md` — diagrammatic flowchart with standard flowchart symbols and arrows (GitHub renders the diagram)
- `flowchart.txt` — text version of the flowchart
- `test_cases.txt` — sample test inputs and expected results
- `output/run_screenshot.svg` — illustrative sample-output graphic

## How to Run
Run `main.py` with Python 3 and enter the energy use before and after conservation.

## Sample Run
Input:
```
Enter energy use before conservation (units): 100
Enter energy use after conservation (units): 70
```

Expected output:
```
Energy saved: 30.0 units
Percentage saved: 30.0 %
```

## Conclusion
The program compares energy use before and after conservation and calculates savings when the after-value is not higher than the before-value.
