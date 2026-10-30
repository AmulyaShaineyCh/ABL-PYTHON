# Case Study 29: Password Policy Validation

## Problem Statement
Check whether a password meets a basic policy: at least eight characters long, with at least one digit and one uppercase letter. Display which requirements are missing when the password does not qualify.

## Objectives
1. Read a password from the user.
2. Check its length.
3. Check whether it contains a digit.
4. Check whether it contains an uppercase letter.
5. Display the result and any missing requirements

## Assumptions
- The password is entered as text.
- A valid password must contain at least eight characters, one digit, and one uppercase English letter.
- This is a basic classroom example and does not check every real-world password-security requirement.

## Algorithm
1. Start and read the password.
2. Set the digit-found and uppercase-found flags to false.
3. Examine each character in the password.
4. If a character is a digit, set the digit flag to true.
5. If a character is an uppercase letter, set the uppercase flag to true.
6. If the password has at least eight characters and both flags are true, display that it meets the policy.
7. Otherwise, display that it does not meet the policy and list each missing requirement.
8. Stop.

## Python Concepts Used
- Variables and Boolean values
- Input and output
- String iteration and `len()`
- Comparison and logical operators
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
Run `main.py` with Python 3 and enter a password when prompted.

## Sample Run
Input:
```
Enter a password: Hello123
```

Expected output:
```
Password meets the basic policy.
```

## Conclusion
The program checks password length, digits, and uppercase letters using string iteration and conditional statements.
