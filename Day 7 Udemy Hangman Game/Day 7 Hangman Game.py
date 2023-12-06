import random
from hangman_words import word_list
import hangman_art

end_of_game = False
lives = 6

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

random_num = random.randint(0,2)
word = word_list[random_num]

#just some code testing...

#print(f"Hey you...the answer is {word}")

# for letter in word:
#     if guess == letter:
#         print("RIGHT")
#     else:
#         print("WRONG")

display = []
num_spaces = len(word)
for zed in range(0, num_spaces):
    display.append("_")

print(hangman_art.logo)

while not end_of_game:
    print("Welcome to Hangman! Made by Bayden Willms")
    guess = input("Guess a letter:\n> ").lower()
    guesses = []
    guesses.append(guess)
    index = 0
    found = False

    if guess in display:
        print(f"You have already guessed {guess}. Please try another.")

    for letter in word:
        if letter == guess:
            display[index] = guess
            found = True
        index += 1
    
    if not found:
        lives -= 1

    print(hangman_art.stages[lives])
    print(display)

    if lives == 0:
        print("YOU LOSE!")
        print(f"The word was {word}.")
        end_of_game = True
    elif "_" not in display:
        print("YOU WIN!")
        end_of_game = True
    else:
        if guess not in word:  
            print(f"{guess} is not in the word. Lives remaining:", lives)

