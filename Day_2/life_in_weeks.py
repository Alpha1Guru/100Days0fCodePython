while True:
    age = input("What is your age: ")
    years_left = 90 - int(age)
    months_left = years_left * 12
    weeks_left = years_left * 52
    days_left = years_left * 365
    print(f"Your have {days_left} days left, {weeks_left} weeks left, {months_left} months left {years_left} years left.")