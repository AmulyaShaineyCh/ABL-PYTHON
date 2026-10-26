days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
total = 0
for day in days:
    units = float(input("Enter units for " + day + ": "))
    total = total + units
print("Weekly consumption:", total, "units")
print("Daily average:", total / 7, "units")
