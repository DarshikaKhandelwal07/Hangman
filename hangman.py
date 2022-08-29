import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

stages=[
'''
 +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

end_of_game = False
lives = 0

display = []
# vowels = ['a','e','i','o','u']
for i in chosen_word:
    display += '_'
print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(display)
    if guess not in chosen_word:
        print(stages[lives])
        lives += 1
        if lives == 6:
            end_of_game = True
            print("You lose")
            print("The word was " + chosen_word)
    if "_" not in display:
        end_of_game = True
        print("You win")