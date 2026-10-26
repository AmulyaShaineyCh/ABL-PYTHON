# Student Marks Matrix Analysis
# Concepts: variables, input/output, conditionals, loops, lists and nested lists.

marks = []
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Invalid input. Students and subjects must be greater than 0.")
else:
    for i in range(students):
        row = []
        print("Enter marks for student", i + 1)
        for j in range(subjects):
            mark = int(input("Subject " + str(j + 1) + " (0-100): "))
            while mark < 0 or mark > 100:
                print("Invalid mark. Enter a mark from 0 to 100.")
                mark = int(input("Subject " + str(j + 1) + " (0-100): "))
            row.append(mark)
        marks.append(row)

    print("\nStudent Marks Analysis")
    for i in range(students):
        total = 0
        for j in range(subjects):
            total = total + marks[i][j]
        average = total / subjects
        print("Student", i + 1, "total:", total, "average:", round(average, 2))
