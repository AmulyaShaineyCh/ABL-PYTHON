# Case Study 21: Traffic Violation Penalty Calculator

## Problem Statement
Compare a vehicle's speed with the speed limit and calculate an illustrative fine when the vehicle exceeds the limit.

## Objectives
1. Read the vehicle speed and speed limit.
2. Validate the speed values.
3. Determine whether the speed exceeds the limit.
4. Assign an illustrative fine based on how much the limit is exceeded.
5. Display the result.

## Assumptions
- Speed values are entered as whole numbers in km/h.
- Vehicle speed cannot be negative.
- The speed limit must be greater than zero.
- Fine amounts are examples used for this case study, not a statement of actual legal penalties.

## Algorithm
1. Start and read vehicle speed and speed limit.
2. If speed is negative or the limit is not positive, display an error.
3. If speed is at or below the limit, display that there is no speeding fine.
4. Otherwise, calculate the excess speed.
5. If excess is at most 10 km/h, set the illustrative fine to Rs. 500.
6. Else if excess is at most 20 km/h, set it to Rs. 1,000.
7. Otherwise, set it to Rs. 2,000.
8. Display the excess speed and illustrative fine, then stop.

## Python Concepts Used
- Variables and integer conversion
- Input and output
- Arithmetic and comparison operators
- `if`, `elif`, and `else`
- Nested conditional statements

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
Run `main.py` with Python 3 and enter the vehicle speed and speed limit in km/h.

## Sample Run
Input:
```
Enter vehicle speed (km/h): 75
Enter speed limit (km/h): 60
```

Expected output:
```
Speed exceeded by: 15 km/h
Illustrative fine amount: Rs. 1000
```

## Conclusion
The program validates speed inputs, checks the excess speed, and selects an illustrative fine using conditional statements.
