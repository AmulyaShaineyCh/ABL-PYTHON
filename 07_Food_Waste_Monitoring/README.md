# Case Study 53: Food Waste Monitoring System

## Problem Statement
Record food waste in kilograms for five weekdays, calculate the total and daily average, and display a suggestion based on the total waste.

## Objectives
1. Read food waste for Monday through Friday.
2. Calculate total food waste.
3. Calculate average daily waste.
4. Display a suggestion based on whether the total exceeds 10 kg

## Assumptions
- The user enters a numeric waste amount for each weekday.
- Values are measured in kilograms.
- The program uses five days, Monday through Friday.
- The suggestion threshold is 10 kg for the total recorded period.

## Algorithm
1. Start and create a list of weekdays.
2. Set total food waste to zero.
3. For each day, ask for the food waste in kilograms and add it to the total.
4. Calculate the average by dividing the total by the number of days.
5. Display the total and daily average.
6. If the total is greater than 10 kg, suggest reviewing food preparation quantities.
7. Otherwise, encourage continued monitoring.
8. Stop.

## Python Concepts Used
- Variables and lists
- Input and output
- `float()` type conversion
- Arithmetic operators
- `for` loop
- `if` and `else`

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
Run `main.py` with Python 3 and enter the food waste in kilograms for each weekday.

## Sample Run
Input:
```
Enter food waste in kg for Monday: 2
Enter food waste in kg for Tuesday: 3
Enter food waste in kg for Wednesday: 2
Enter food waste in kg for Thursday: 1
Enter food waste in kg for Friday: 4
```

Expected output:
```
Total food waste: 12.0 kg
Daily average waste: 2.4 kg
Suggestion: review food preparation quantities.
```

## Conclusion
The program totals weekday food waste, calculates the average, and provides a simple monitoring suggestion.
