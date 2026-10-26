marks = []
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
if students <= 0 or subjects <= 0:
    print("Enter positive numbers of students and subjects.")
else:
    for i in range(students):
        row = []
        print("Enter marks for student", i + 1)
        for j in range(subjects):
            mark = int(input("Subject " + str(j + 1) + ": "))
            row.append(mark)
        marks.append(row)
    for i in range(students):
        total = 0
        for j in range(subjects):
            total = total + marks[i][j]
        print("Student", i + 1, "total:", total, "average:", total / subjects)
