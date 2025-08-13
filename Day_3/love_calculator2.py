print("Welcoome to the Love Calculator!")
print("This program will calculate the love score between two people based on their names.")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_name = name1.lower() + name2.lower()

true = 0
love = 0
#Calculate True
# for char in combined_name:
#     if char in "true":
#         true += 1
true = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") +combined_name.count("e")

print("True: {}".format(true))

#Calculate Love
# for char in combined_name:
#     if char in "love":
#         love += 1
love = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") +combined_name.count("e")
print("Love: {}".format(love))

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} you are alright together.")
else:
    print(f"Your score is {love_score}")
