import re

while True:
    password = input("Enter Password: ")

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number")

    if re.search("[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")
        print("Password accepted!")
        break

    print("\nSuggestions to improve your password:")
    for item in suggestions:
        print("-", item)

    print("\nPlease try again.\n")
