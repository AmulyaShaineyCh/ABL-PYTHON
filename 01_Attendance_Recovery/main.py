# Case Study 12: Attendance Recovery Computation

total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes <= 0:
    print("Invalid total classes. Enter a number greater than 0.")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid attended classes.")
else:
    attendance = attended_classes / total_classes * 100

    print("Current attendance:", attendance, "%")

    if attendance >= 75:
        print("You have reached 75% attendance.")
        print("Additional consecutive classes needed: 0")
    else:
        extra_classes = 0

        while (attended_classes + extra_classes) / (total_classes + extra_classes) * 100 < 75:
            extra_classes = extra_classes + 1

        print("Additional consecutive classes to attend:", extra_classes)
