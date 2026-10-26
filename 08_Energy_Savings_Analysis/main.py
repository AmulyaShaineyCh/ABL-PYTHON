before = float(input("Enter energy use before conservation (units): "))
after = float(input("Enter energy use after conservation (units): "))
if before <= 0 or after < 0:
    print("Enter valid non-negative values; before must be above 0.")
elif after > before:
    print("Energy use increased by", after - before, "units.")
else:
    saved = before - after
    print("Energy saved:", saved, "units")
    print("Percentage saved:", saved / before * 100, "%")
