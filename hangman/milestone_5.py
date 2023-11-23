import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_to_be_guessed = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word_to_be_guessed)
        self.num_letters = int(len(set(self.word_to_be_guessed)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This function takes in the users guess.
        It updates upto 3 attributes (word_guessed and numb_letters if correct guess and num_lives if incorrect.
        """
        lowered_guess = guess.lower()
        if lowered_guess in self.word_to_be_guessed:
            print(f"Good guess! {guess} is in the word.")
            for position in range(len(self.word_to_be_guessed)):
                if lowered_guess == self.word_to_be_guessed[position]:
                    self.word_guessed[position] = lowered_guess
            self.num_letters -= 1

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        This function [currently] continuously asks for the user to make a guess.
        It updates list_of_guesses if acceptable guess.
        """
        while True:
            print("le", self.num_letters)
            print("li", self.num_lives)
            print("gu", self.word_guessed)
            guess = input("guess a letter \n")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters < 1:
            print("Congratulations. You won the game!")
            break


word_list = ["banana", "mango", "lime", "apple", "papaya"]


play_game(word_list)
