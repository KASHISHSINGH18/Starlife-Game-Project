import random

def choose_word():
    """Returns a randomly chosen word from a predefined list."""
    words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Displays the word with guessed letters filled in and others as underscores.

    Args:
    - word (str): The word to be displayed.
    - guessed_letters (list): A list of letters that have been guessed.

    Returns:
    - str: The word with guessed letters filled in and others as underscores.
    """
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_stars(attempts):
    """
    Displays stars representing remaining attempts.

    Args:
    - attempts (int): The number of attempts remaining.

    Returns:
    - str: Stars representing remaining attempts.
    """
    stars = "*" * attempts
    return stars

def hangman():
    """Main function implementing the Hangman game."""
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Stars:", display_stars(attempts))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect!")
            attempts -= 1
            if attempts == 0:
                print("\nYou've run out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        hangman()
    else:
        print("Thanks for playing!")

hangman()
