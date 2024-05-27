import random
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the logo at the start of the game
print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for _ in range(word_length)]

# Track guessed letters
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed the letter
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.append(guess)

        # Check guessed letter
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            # If the letter is not in the chosen_word, lose a life
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}")

    # Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the stages
    print(stages[lives])
