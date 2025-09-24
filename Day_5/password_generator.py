"""This is a Password Generator Python Script"""
import random
import string
greeting = "Welcome to the PyPassword Generator!"
print(greeting)

letters = list(string.ascii_letters)
numbers = list(string.digits)
# special_chars = list(string.punctuation)
special_chars = ["!", "#", "$", "%", "&", ")", "(", "*", "+"]

def getValidateNumericInput(message):
    while True:
        userInput = input(message).strip()
        if userInput.isdigit():
            return userInput
        else:
            print("This is not a number please provide and interger number!")
#Get and validate user input
num_of_letters = int(getValidateNumericInput("How many letters would you like in your password? "))
num_of_numbers = int(getValidateNumericInput("How many numbers would you like in your password? "))
num_of_special_chars = int(getValidateNumericInput("How many special characters would you like in your password? "))

#This wouldn't work as the code will break 
#When the num of char requested by the user exceeds the list
#e.g if num_of_numbers = 30 the code will break as len(numbers) = 10 i.e 0123...9
# random_letters = random.sample(letters, k=num_of_letters)
# random_numbers = random.sample(numbers, k=num_of_numbers)
# random_special_chars = random.sample(special_chars, k=num_of_special_chars)

random_letters = [random.choice(letters) for _ in range(num_of_letters)]
random_numbers = [random.choice(numbers) for _ in range(num_of_numbers)]
random_special_chars = [random.choice(special_chars) for _ in range(num_of_special_chars)]

password_chars = random_letters + random_numbers + random_special_chars
random.shuffle(password_chars)
final_password = "".join(password_chars)

print("Your Password is: {}".format(final_password))
random.choices