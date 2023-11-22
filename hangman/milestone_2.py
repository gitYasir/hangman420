import random

word_list = ["banana", "mango", "lime", "apple", "papaya"]

word = random.choice(word_list)
guess = input("guess a letter")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
