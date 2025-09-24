rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____] + hands[user
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
print("Welcome To A Game of Rock Paper Scissors")

"""
rock == 0
paper == 1
scissors == 2
"""

hands = [rock, paper, scissors]

# Get user's hand
while True:
    user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))
    if user_hand not in [0, 1, 2]:
        print("Invalid input. Please choose 0, 1, or 2.")
    else:
        break

#Get the computer hand
computer_hand = random.randint(0,2)

# Split each string into lines
user_lines = ["You Played"] + hands[user_hand].rstrip().split('\n')
computer_lines = ["Computer Played"] + hands[computer_hand].rstrip().split('\n')

# Print them side by side
for r_line, p_line in zip(user_lines, computer_lines):
    print(r_line.ljust(30) + p_line)

#To Determine the winner
"""
Rock wins against scissors. 0>2
Scissors win against paper. 2>1
Paper wins against rock.    1>0
"""
# #First Version
# if user_hand == computer_hand:
#     print("It's a draw")
# elif ((user_hand==0 and computer_hand ==2) # Rock beats Scissors
#       or (user_hand==2 and computer_hand ==1) # Paper beats Rock
#       or (user_hand==1 and computer_hand ==0) # Scissors beats Paper
#       ):
#     print("You won")
# else:
#     print("You lost")

#Chatgpt Suggestion
outcomes = {
    (0, 2): "You won",     # Rock beats Scissors
    (1, 0): "You won",     # Paper beats Rock
    (2, 1): "You won"      # Scissors beats Paper
}

if user_hand == computer_hand:
    print("It's a draw")
else:
    print(outcomes.get((user_hand, computer_hand), "You lost"))
