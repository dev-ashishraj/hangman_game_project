import random


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

# Example of how to print the last stage (empty gallows)
lives = 6
print(stages[lives])
word_list = ["aardvark","baboon","camel"]


lives = 6

choice = random.choice(word_list)
print(choice)

placeholder = ""
world_length = len(choice)
for position in range(world_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: \n").lower()
    print(guess)




    display = ""


    for letter in choice:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"


    print(display)

    if guess not in choice:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
    
    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])