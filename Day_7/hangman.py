import random
import string
from arts import logo, stages
from word_list import word_list
import os

def clear_screen():
  #Check the operating system
  if os.name == "nt": #For Windows
    os.system("cls")
  else: #For macOS and Linux
    os.system("clear")

no_lives = 6
lives = no_lives
no_of_failed_attempts = 0
hang_word = random.choice(word_list).lower()
possible_guesses = set(hang_word)
all_guesses = set()
correct_guesses = set()

def display_status():
  #Display Current Status
  print(f"{"\u2764 " * lives}{"x "*no_of_failed_attempts}")
  print(" ".join([char if char in correct_guesses else "_" for char in hang_word]))
  print(stages[lives])
  print(" ".join(["#" if char in all_guesses else char for char in string.ascii_lowercase]))


print(logo)
while no_of_failed_attempts < no_lives:
  display_status()
  #Input Validation
  while True:
    guessed_letter = input("Guess the letter: ").lower().strip()
    if not guessed_letter:
      print("You Didn't Type anything! Give me A LETTER")
    elif len(guessed_letter) > 1:
      print("Invalid I only need one letter!")
    elif guessed_letter not in string.ascii_lowercase:
      print("Invalid Input Give me A LETTER!")
    elif guessed_letter in string.ascii_lowercase:
      if guessed_letter in all_guesses:
        print("You have guessed this letter before!\t"
              "Try another one!")
      elif not guessed_letter in all_guesses:
        all_guesses.add(guessed_letter)
        break

  #For a Correct Guess
  if guessed_letter in possible_guesses:
    correct_guesses.add(guessed_letter)
    if correct_guesses == possible_guesses:
      print("You Won!")
      break
    elif correct_guesses < possible_guesses:
      print("You got this let's go")

  #For a Wrong Guess
  elif guessed_letter not in possible_guesses:
    lives -= 1
    no_of_failed_attempts += 1
    if lives > 0:
      print(f"You guessed {guessed_letter}, that's not in the word. You lose a life")
    else:
      #Display Current Status
      display_status()
      print(f"You Lose the word was '{hang_word}' ")