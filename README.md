# Hangman Project

## Table of Content

- [Description](#description)
- [Installation instructions](#installation-instructions)
- [Usage instructions](#usage-instructions)
- [File structure](#file-structure)
- [License information](#license-information)

## Description

This is my second project at AiCore, where I aimed to create an engaging Hangman game playable on the terminal/console. The project leverages fundamental Object-Oriented Programming (OOP) principles, encapsulating game logic within the Hangman class. Key functionalities include word selection, user input validation, and list manipulation for game state tracking. The game employs a structured game loop, allowing repeated user input until game completion conditions are met.

### Aim:

To build a hangman game that can be played on the terminal/console

## What I learned

### Object-Oriented Programming (OOP):

The code demonstrates the use of object-oriented programming principles. The Hangman class encapsulates the game logic, and methods like check_guess and ask_for_input operate on the object's state.

### Random Selection and Initialization:

The project uses the random.choice function to randomly select a word from the provided word_list. This showcases a simple way to initialize the game with a random word.

### User Input Validation:

The ask_for_input method includes input validation to ensure that the user enters a single alphabetical character. This demonstrates a basic form of user input validation to handle potential errors.

### List Manipulation:

The code uses lists extensively, such as word_guessed to track the state of the word being guessed and list_of_guesses to keep track of letters that have already been guessed. This highlights how lists can be manipulated to manage game state.

### Game Loop:

The play_game function demonstrates the use of a game loop to repeatedly prompt the user for input until certain conditions are met (e.g., running out of lives or correctly guessing the word). Understanding how to structure a game loop is crucial for interactive programs.

## Installation instructions

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following software installed on your machine:

- [Python](https://www.python.org/) (version 3.12.0)

### Clone the Repository

```bash
git clone https://github.com/gitYasir/hangman420.git
```

### Navigate to the Project Directory

```bash
cd hangman
```

## How to play

Welcome to the Hangman game! Follow these instructions to play the game.

### Run the game

```bash
python milestone_5.py
```

### Objective

Your objective is to guess the hidden word by suggesting letters. For each incorrect guess, you lose a life. The game ends when you either correctly guess the entire word or run out of lives.

### Rules

1. At the start, a random word is selected from the word list.
2. You have a limited number of lives (default: 5) to guess the word.
3. Guess one letter at a time.
4. If your guess is correct, the letter will be revealed in the word.
5. If your guess is incorrect, you lose a life.
6. You can only guess each letter once.

### Controls

- Input a single alphabetical character when prompted to guess a letter.
- Press 'Enter' to submit your guess.

### Winning and Losing

- **Winning:** Successfully guess all the letters in the word before running out of lives.
- **Losing:** Run out of lives before guessing the entire word.

## File structure

- hangman/
  - hangman_Template.py
  - milestone_2.py
  - milestone_3.py
  - milestone_4.py
  - milestone_5.py
- README.md

## License information

MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
