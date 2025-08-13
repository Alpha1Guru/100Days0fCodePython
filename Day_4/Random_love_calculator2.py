import random
print("Welcoome to the Love Calculator!")
print("This program will calculate the love score between two people based on their names.")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_name = name1.lower() + name2.lower()


love_score = random.randint(0,101)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} you are alright together.")
else:
    print(f"Your score is {love_score}")
