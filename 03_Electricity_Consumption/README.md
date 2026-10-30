# Case Study 45: Weekly Electricity Consumption Matrix

## Problem Statement
Record electricity consumption in units for each day of a week, then calculate the total weekly consumption and average daily consumption.

## Objectives
1. Read electricity usage for all seven days.
2. Add the daily usage to calculate weekly consumption.
3. Calculate the average daily consumption.
4. Display both results.

## Assumptions
- The user enters a numeric consumption value for each day.
- Consumption values are entered in units.
- The program records Monday through Sunday.

## Algorithm
1. Start and create a list of the seven days.
2. Set the total consumption to zero.
3. For each day, ask the user to enter the units consumed.
4. Add the entered value to the total.
5. Calculate the average by dividing the total by seven.
6. Display the weekly total and daily average.
7. Stop.

## Python Concepts Used
- Variables and lists
- Input and output
- `float()` type conversion
- Arithmetic operators
- `for` loop

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
Run `main.py` with Python 3 and enter the electricity units for each day from Monday to Sunday.

## Sample Run
Input:
```
Enter units for Monday: 1
Enter units for Tuesday: 2
Enter units for Wednesday: 3
Enter units for Thursday: 4
Enter units for Friday: 5
Enter units for Saturday: 6
Enter units for Sunday: 7
```

Expected output:
```
Weekly consumption: 28.0 units
Daily average: 4.0 units
```

## Conclusion
The program uses a list, a loop, and arithmetic operations to calculate weekly electricity consumption and the daily average.
