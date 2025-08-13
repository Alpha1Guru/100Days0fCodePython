import random

while True:
    user_seed = input("Create a seed (it's a digit e.g 1,34, 104): ")
    if user_seed.isdecimal():
        seed = random.seed(user_seed)
        break
    else:
        print("Not a digit!")

flip_coin = random.choice(("Heads", "Tails"))
print(flip_coin)