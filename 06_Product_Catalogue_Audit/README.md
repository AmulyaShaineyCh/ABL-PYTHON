# Case Study 49: Tuple-Based Product Catalogue Audit

## Problem Statement
Use a tuple-based product catalogue to display each product's price, quantity, and stock value, and calculate the total value of all products in stock.

## Objectives
1. Store product details in a tuple.
2. Read each product's name, price, and quantity from the tuple.
3. Calculate each product's stock value.
4. Calculate and display the total stock value.

## Assumptions
- The catalogue is already defined in the program.
- Each product entry contains a name, price, and quantity.
- Stock value is calculated as price multiplied by quantity.

## Algorithm
1. Start and define the product catalogue as a tuple of product tuples.
2. Set the total stock value to zero.
3. For each product, read its name, price, and quantity using tuple indexing.
4. Calculate the product's stock value.
5. Add that value to the running total.
6. Display the details and stock value for each product.
7. Display the total stock value and stop.

## Python Concepts Used
- Tuples and tuple indexing
- Variables
- `for` loop
- Arithmetic operators
- Input/output through `print()`

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
Run `main.py` with Python 3. The catalogue is built into the program, so no user input is required.

## Sample Run
Expected output:
```
Product catalogue
Pen - price: 10 quantity: 25 stock value: 250
Notebook - price: 50 quantity: 12 stock value: 600
Pencil - price: 5 quantity: 40 stock value: 200
Total stock value: 1050
```

## Conclusion
The program uses nested tuples and a loop to calculate individual product stock values and the total value of the catalogue.
