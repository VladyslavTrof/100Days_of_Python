import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)


display = ["_" for _ in range(word_length)]
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.append(guess)


        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter


        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])


#Changes made:

#Imported word_list, logo, and stages from the respective modules.
#Added a list guessed_letters to keep track of guessed letters.
#Checked if the user has already guessed a letter and notified them if so.
#Printed the corresponding stage of the hangman after each guess.
#Included a conditional to check if the guessed letter is incorrect, reduce lives, and end the game if lives reach 0.