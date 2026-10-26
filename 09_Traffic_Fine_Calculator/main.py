speed = int(input("Enter vehicle speed (km/h): "))
limit = int(input("Enter speed limit (km/h): "))
if speed < 0 or limit <= 0:
    print("Enter a valid speed and a positive speed limit.")
elif speed <= limit:
    print("No speeding fine.")
else:
    excess = speed - limit
    if excess <= 10:
        fine = 500
    elif excess <= 20:
        fine = 1000
    else:
        fine = 2000
    print("Speed exceeded by:", excess, "km/h")
    print("Illustrative fine amount: Rs.", fine)
