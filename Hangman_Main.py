import random
import Hangman_word
import Hangman_art

chosen_word = random.choice(Hangman_word.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(Hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have entered a letter they've already guessed")
        print(f"{' '.join(display)}")
        continue
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print("Entered the wrong letter. It is not in the word. Here is your punishment. ")
        lives -= 1
        print(Hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")