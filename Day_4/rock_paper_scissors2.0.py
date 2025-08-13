import random

# ASCII Art
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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
hand_names = ["Rock", "Paper", "Scissors"]

# Outcome logic
outcomes = {
    (0, 2): "You won",     # Rock beats Scissors
    (1, 0): "You won",     # Paper beats Rock
    (2, 1): "You won"      # Scissors beats Paper
}
emojis = {
    "You won": "🎉",
    "You lost": "😢",
    "It's a draw": "🤝"
}

# Scoreboard
score = {"You": 0, "Computer": 0, "Draws": 0}

print("🎮 Welcome to Rock, Paper, Scissors!")

while True:
    # Get user's hand with validation
    while True:
        try:
            user_hand = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))
            if user_hand in [0, 1, 2]:
                break
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Computer's hand
    computer_hand = random.randint(0, 2)

    # Display choices
    user_lines = [f"You Played: {hand_names[user_hand]}".ljust(25)] + hands[user_hand].rstrip().split('\n')
    computer_lines = [f"Computer Played: {hand_names[computer_hand]}"] + hands[computer_hand].rstrip().split('\n')

    for u_line, c_line in zip(user_lines, computer_lines):
        print(u_line.ljust(35) + c_line)

    # Determine outcome
    if user_hand == computer_hand:
        result = "It's a draw"
        score["Draws"] += 1
    elif (user_hand, computer_hand) in outcomes:
        result = "You won"
        score["You"] += 1
    else:
        result = "You lost"
        score["Computer"] += 1

    print(f"\nResult: {result} {emojis[result]}")
    print(f"Scoreboard: You {score['You']} | Computer {score['Computer']} | Draws {score['Draws']}\n")

    # Replay option
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! 👋")
        break
