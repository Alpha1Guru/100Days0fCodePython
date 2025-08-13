print("Welcome To The Ticket Store")
height = int(input("Hello Boss what's your height in cm? "))
if height >= 120:
    age = int(input("What's your age? "))
    price = 0
    if age < 12:
        price = 5
        print("Your ticket price is ${}.".format(price))
    elif age <= 18:
        price = 7
        print("Your ticket price is ${}.".format(price))
    else:
        price = 12
        print("Your ticket price is ${}.".format(price))
    wants_photo = input("Do you want a photo taken? (yes/no) ").strip().lower()
    if wants_photo == 'yes':
        price += 3
        print("Your total ticket price is ${} extra for the photo.".format(price))
else:
    print("Sorry Bro You are too short!")