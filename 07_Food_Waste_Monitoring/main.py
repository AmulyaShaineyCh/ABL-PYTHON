days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
total = 0
for day in days:
    kg = float(input("Enter food waste in kg for " + day + ": "))
    total = total + kg
average = total / len(days)
print("Total food waste:", total, "kg")
print("Daily average waste:", average, "kg")
if total > 10:
    print("Suggestion: review food preparation quantities.")
else:
    print("Good work: keep monitoring food waste.")
