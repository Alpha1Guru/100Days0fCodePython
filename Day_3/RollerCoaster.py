print("Welcome To The Ticket Store")
height = int(input("Hello Boss what's your height in cm? "))
if height > 120:
    age = int(input("What's your age? "))
    if age < 12:
        print("Your ticket price is $5")
    elif age <= 18:
        print("Your ticket price is $7")
    else:
        print("Your ticket price is $12")
    print("Here have your roller coaster ticket! 🎟")
else:
    print("Sorry Bro You are too short!")