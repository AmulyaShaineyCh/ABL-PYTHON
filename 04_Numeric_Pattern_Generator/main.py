rows = int(input("Enter number of rows (1 to 9): "))
if rows < 1 or rows > 9:
    print("Please enter a number from 1 to 9.")
else:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
