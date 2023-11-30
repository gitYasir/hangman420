import random


class Hangman:
    """
    Hangman class represents the core logic of the Hangman game.

    Attributes:
    - word_list (list): List of words to be used in the game.
    - num_lives (int): Number of lives a player has to guess the word.
    - word_to_be_guessed (str): The randomly selected word for the game.
    - word_guessed (list): List representing the current state of the guessed word.
    - num_letters (int): Number of unique letters in the word_to_be_guessed.
    - list_of_guesses (list): List to store the letters guessed by the player.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new instance of the Hangman class.

        Parameters:
        - word_list (list): List of words to be used in the game.
        - num_lives (int): Number of lives a player has to guess the word.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_to_be_guessed = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word_to_be_guessed)
        self.num_letters = len(set(self.word_to_be_guessed))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks the validity of the user's guess and updates the game state.

        Parameters:
        - guess (str): The letter guessed by the user.
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
        Continuously prompts the user to make a guess and updates the list_of_guesses.
        """
        while True:
            print("Lives", self.num_lives)
            print("Word", self.word_guessed)
            print("Guessed letters", self.list_of_guesses)
            guess = input("Guess a letter \n")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            break


def play_game(word_list):
    """
    Initiates and runs the Hangman game.

    Parameters:
    - word_list (list): List of words to be used in the game.
    """
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
