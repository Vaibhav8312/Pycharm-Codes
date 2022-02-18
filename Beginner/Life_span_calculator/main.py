
age = input("What is your current age? ")
choice = input('What do you want to check type = "w" for life wasted and type = "l" for life left? ').lower()

if choice == "l":
    years_left = 90 - int(age)
    days = years_left * 365
    weeks = years_left * 52
    months = years_left * 12
    print(f"You have {days} days, {weeks} weeks, and {months} months left.")
elif choice == "w":
    days = int(age) * 365
    weeks = int(age) * 52
    months = int(age) * 12
    print(f"You have {days} days, {weeks} weeks, and {months} months wasted.")
else:
    print("Please enter a valid character.")
