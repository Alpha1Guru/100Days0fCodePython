import random
import string
import os
from arts import logo, stages
from word_list import word_list


# -----------------------------
# Helpers
# -----------------------------

def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS/Linux
        os.system("clear")


def new_game(lives=6):
    """Initialize and return a new game state."""
    word = random.choice(word_list).lower()
    return {
        "lives": lives,
        "no_of_failed_attempts": 0,
        "word": word,
        "possible_guesses": set(word),
        "correct_guesses": set(),
        "all_guesses": set()
    }


def display_status(game):
    print(f'{"❤ " * game["lives"]}{"x " * game["no_of_failed_attempts"]}')
    print(" ".join([ch if ch in game["correct_guesses"] else "_" for ch in game["word"]]))
    print(stages[game["lives"]])
    print(" ".join(["#" if ch in game["all_guesses"] else ch for ch in string.ascii_lowercase]))


def get_guess(game):
    """Ask the player for a valid guess."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if not guess:
            print("❌ You didn’t type anything!")
        elif len(guess) > 1:
            print("❌ Please enter only one letter.")
        elif guess not in string.ascii_lowercase:
            print("❌ Invalid input. O nly letters allowed.")
        elif guess in game["all_guesses"]:
            print("⚠️ Already guessed that letter.")
        else:
            return guess


def apply_guess(game, letter):
    """Apply the guessed letter and update the game state."""
    game["all_guesses"].add(letter)

    if letter in game["possible_guesses"]:
        game["correct_guesses"].add(letter)
        if game["correct_guesses"] == game["possible_guesses"]:
            display_status(game)
            print("🎉 You won!")
            return True
    else:
        game["lives"] -= 1
        game["no_of_failed_attempts"] += 1
        if game["lives"] == 0:
            display_status(game)
            print(f"💀 You lost! The word was '{game['word']}'.")
            return True
        else:
            print(f"❌ {letter} is not in the word. You lost a life.")
    return False


def play():
    print(logo)
    game = new_game()
    while True:
        display_status(game)
        guess = get_guess(game)
        finished = apply_guess(game, guess)
        if finished:
            break


def main():
    while True:
        play()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
