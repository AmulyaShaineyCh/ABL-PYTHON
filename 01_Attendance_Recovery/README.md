# Case Study 12: Attendance Recovery Computation

## Problem Statement
Calculate a student's current attendance percentage from the total classes held and classes attended. If attendance is below 75%, find the minimum number of consecutive future classes the student must attend to reach at least 75%.

## Objectives
1. Read and validate the total classes held and classes attended.
2. Calculate and display the current attendance percentage.
3. Check whether the student has already reached 75%.
4. If attendance is below 75%, calculate the minimum additional consecutive classes required.

## Assumptions
- Total classes held must be greater than zero.
- Classes attended must be between zero and total classes held, inclusive.
- The student attends every future class counted by the program.
- The required attendance threshold is 75%.

## Algorithm
1. Start and read total classes held and classes attended.
2. If total classes held is zero or less, display an error.
3. If classes attended is less than zero or greater than total classes held, display an error.
4. Otherwise, calculate and display attendance percentage.
5. If attendance is at least 75%, display that no additional classes are needed.
6. Otherwise, increase the additional-class count until the projected attendance reaches at least 75%.
7. Display the count and stop.

## Python Concepts Used
- Variables and integer conversion
- Input and output
- Arithmetic, comparison, and logical operators
- `if`, `elif`, and `else`
- `while` loop

## Files
- `main.py` — Python program
- `problem_statement.txt` — problem description
- `objectives.txt` — project objectives
- `assumptions.txt` — assumptions
- `algorithm.txt` — step-by-step algorithm
- `pseudocode.txt` — language-independent pseudocode
- `flowchart.txt` — text-based flowchart
- `test_cases.txt` — sample test inputs and expected results
- `output/run_screenshot.svg` — illustrative sample-output graphic

## How to Run
Run `main.py` with Python 3, then enter the total classes held and classes attended when prompted.

## Sample Run
Input:
```
Enter total classes held: 20
Enter classes attended: 12
```

Expected output:
```
Current attendance: 60.0 %
Additional consecutive classes to attend: 12
```

## Conclusion
The program validates attendance inputs, calculates the current percentage, and uses a loop to find the minimum number of consecutive classes needed to reach 75% attendance.
