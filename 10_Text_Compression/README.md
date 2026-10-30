# Case Study 35: Text Compression Using Character Runs

## Problem Statement
Compress a non-empty string by representing each consecutive run of the same character as the character followed by the number of times it appears in that run.

## Objectives
1. Read text from the user.
2. Handle an empty input.
3. Count consecutive repeated characters.
4. Build and display the compressed string.

## Assumptions
- The input is intended to contain letters, as suggested by the program prompt.
- The program processes the entered characters as-is; it does not validate that every character is a letter.
- Each run is encoded as the character followed by its count.

## Algorithm
1. Start and read the text.
2. If the text is empty, display a message and stop.
3. Otherwise, set the compressed result to an empty string and the current run count to one.
4. Compare each character with the previous character.
5. If they match, increase the count.
6. If they differ, append the previous character and its count to the result, then reset the count to one.
7. After the loop, append the final character and its count.
8. Display the compressed text and stop.

## Python Concepts Used
- Variables and strings
- Input and output
- String indexing and `len()`
- `for` loop and `range()`
- `if` and `else`
- String concatenation and integer-to-string conversion

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
Run `main.py` with Python 3 and enter a non-empty string when prompted.

## Sample Run
Input:
```
Enter text using letters only: aabccccc
```

Expected output:
```
Compressed text: a2b1c5
```

## Conclusion
The program counts consecutive character runs and builds a compact representation using strings, indexing, and loops.
