# This code is a basic Hangman game implemented in Python. It selects a random word from a list, prompts the player to guess letters, and displays the progress and hangman stages. The game continues until the player either guesses the word correctly or runs out of lives. 

import random
import hangman_words
import hangman_art

print(hangman_art.logo)

stages = hangman_art.stages

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


lives = 6

display = []
for _ in range(word_length):
    display += "_"
    
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])