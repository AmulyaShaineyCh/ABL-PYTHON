# Case Study 42: Student Marks Matrix Analysis

## Problem Statement
Read marks for multiple students across multiple subjects, store the marks in a nested list, and calculate each student's total and average marks.

## Objectives
1. Read the number of students and subjects.
2. Accept and validate each mark from 0 to 100
3. Store marks in a nested list.
4. Calculate and display each student's total and average.

## Assumptions
- The number of students and subjects must be greater than zero.
- Each mark must be between 0 and 100, inclusive.
- Marks are entered as whole numbers.

## Algorithm
1. Start and read the number of students and subjects.
2. If either value is not positive, display an error.
3. Otherwise, use nested loops to read each student's marks.
4. Repeatedly ask for a mark if it is outside the range 0–100.
5. Store each student's marks in a row and add the row to the marks list.
6. For each student, calculate the total and average.
7. Display each student's total and average, then stop.

## Python Concepts Used
- Variables and integer conversion
- Input and output
- Arithmetic and comparison operators
- `if`, `else`, and `while`
- `for` loops
- Lists and nested lists

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
Run `main.py` with Python 3, then enter the number of students, number of subjects, and each student's marks when prompted.

## Sample Run
Input:
```
Enter number of students: 2
Enter number of subjects: 2
Enter marks for student 1
Subject 1 (0-100): 80
Subject 2 (0-100): 90
Enter marks for student 2
Subject 1 (0-100): 70
Subject 2 (0-100): 75
```

Expected output:
```
Student Marks Analysis
Student 1 total: 170 average: 85.0
Student 2 total: 145 average: 72.5
```

## Conclusion
The program uses a nested list and loops to store student marks and calculate the total and average for each student.
