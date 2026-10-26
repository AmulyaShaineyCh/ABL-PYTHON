password = input("Enter a password: ")
has_digit = False
has_upper = False
for ch in password:
    if ch >= "0" and ch <= "9":
        has_digit = True
    if ch >= "A" and ch <= "Z":
        has_upper = True
if len(password) >= 8 and has_digit and has_upper:
    print("Password meets the basic policy.")
else:
    print("Password does not meet the basic policy.")
    if len(password) < 8:
        print("Use at least 8 characters.")
    if not has_digit:
        print("Include at least one digit.")
    if not has_upper:
        print("Include at least one uppercase letter.")
