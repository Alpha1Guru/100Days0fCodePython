import random
import string
import os
from arts import logo, stages
from word_list import word_list


class Hangman:
    def __init__(self, lives=6):
        self.lives = lives
        self.no_of_failed_attempts = 0
        self.word = random.choice(word_list).lower()
        self.possible_guesses = set(self.word)
        self.correct_guesses = set()
        self.all_guesses = set()

    def clear_screen(self):
        if os.name == "nt":  # Windows
            os.system("cls")
        else:  # macOS/Linux
            os.system("clear")

    def display_status(self):
        print(f'{"❤ " * self.lives}{"x " * self.no_of_failed_attempts}')
        print(" ".join([ch if ch in self.correct_guesses else "_" for ch in self.word]))
        print(stages[self.lives])
        print(" ".join(["#" if ch in self.all_guesses else ch for ch in string.ascii_lowercase]))

    def get_guess(self):
        """Ask player for a valid guess."""
        while True:
            guess = input("Guess a letter: ").lower().strip()
            if not guess:
                print("❌ You didn’t type anything!")
            elif len(guess) > 1:
                print("❌ Please enter only one letter.")
            elif guess not in string.ascii_lowercase:
                print("❌ Invalid input. Only letters allowed.")
            elif guess in self.all_guesses:
                print("⚠️ Already guessed that letter.")
            else:
                return guess

    def process_guess(self, letter):
        """Apply the guessed letter and update game state."""
        self.all_guesses.add(letter)

        if letter in self.possible_guesses:
            self.correct_guesses.add(letter)
            if self.correct_guesses == self.possible_guesses:
                self.display_status()
                print("🎉 You won!")
                return True
        else:
            self.lives -= 1
            self.no_of_failed_attempts += 1
            if self.lives == 0:
                self.display_status()
                print(f"💀 You lost! The word was '{self.word}'.")
                return True
            else:
                print(f"❌ {letter} is not in the word. You lost a life.")
        return False

    def play(self):
        print(logo)
        while True:
            self.display_status()
            guess = self.get_guess()
            finished = self.process_guess(guess)
            if finished:
                break


def main():
    while True:
        game = Hangman()
        game.play()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
