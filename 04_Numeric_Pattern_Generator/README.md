# Case Study 27: Numeric Pattern Generator

## Problem Statement
Display a number pattern with the requested number of rows. Each row begins at 1 and continues up to that row's number.

## Objectives
1. Read the number of rows.
2. Validate that the row count is between 1 and 9.
3. Use nested loops to print the numeric pattern.
4. Display an error message for an invalid row count.

## Assumptions
- The number of rows must be a whole number from 1 to 9, inclusive.
- The pattern prints numbers in ascending order in each row.

## Algorithm
1. Start and read the number of rows.
2. If the row count is less than 1 or greater than 9, display an error.
3. Otherwise, start an outer loop from 1 to the requested row count.
4. For each row, use an inner loop to print numbers from 1 to the current row number.
5. Move to a new line after each row.
6. Stop.

## Python Concepts Used
- Variables and integer conversion
- Input and output
- Comparison operators
- `if` and `else`
- Nested `for` loops
- The `print()` `end` argument

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
Run `main.py` with Python 3 and enter a whole number from 1 to 9.

## Sample Run
Input:
```
Enter number of rows (1 to 9): 4
```

Expected output:
```
1
1 2
1 2 3
1 2 3 4
```

## Conclusion
The program validates the requested row count and uses nested loops to generate the numeric pattern.
