
    # Importing random module to pick a random word
import random

# Different stages of hangman (visual representation)
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 / |  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
   |  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Total number of lives the player has
lives = 6

# Example: printing initial empty hangman stage
print(stages[lives])

# List of possible words for the game
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
choice = random.choice(word_list)

# (For testing) print the chosen word
# Remove this line if you want the game to be fair
print(choice)

# Create a placeholder with underscores (_ _ _)
placeholder = ""
word_length = len(choice)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

# Game state control variable
game_over = False

# List to store correctly guessed letters
correct_letter = []

# Main game loop
while not game_over:

    # Take input from the user
    guess = input("Guess a letter: \n").lower()
    print("You guessed:", guess)

    # This will store the updated word display
    display = ""

    # Loop through each letter in the chosen word
    for letter in choice:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    # Show current progress
    print("Word:", display)

    # If guessed letter is NOT in the word
    if guess not in choice:
        lives -= 1
        print("Wrong guess! Lives left:", lives)

        # If no lives left → lose
        if lives == 0:
            game_over = True
            print("You lose.")

    # If no "_" left → win
    if "_" not in display:
        game_over = True
        print("You win.")

    # Show current hangman stage
    print(stages[lives])