import random

def choose_word(difficulty):
    """Returns a randomly chosen word from predefined lists based on difficulty."""
    easy_words = ["apple", "banana", "cherry"]
    medium_words = ["orange", "kiwi", "melon"]
    hard_words = ["mango", "strawberry", "pineapple"]
    
    if difficulty == "easy":
        return random.choice(easy_words)
    elif difficulty == "medium":
        return random.choice(medium_words)
    elif difficulty == "hard":
        return random.choice(hard_words)
    else:
        raise ValueError("Invalid difficulty level")

def display_word(word, guessed_letters):
    """Displays the word with guessed letters filled in and others as underscores."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_stars(attempts):
    """Displays stars representing remaining attempts."""
    stars = "*" * attempts
    return stars

def calculate_score(attempts, word_length):
    """Calculates the score based on attempts and word length."""
    return attempts * word_length

def starlife():
    """Main function implementing the Starlife game."""
    print("Welcome to Starlife!")
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose again.")
            continue
        
        word = choose_word(difficulty)
        guessed_letters = []
        attempts = 6
        score = 0

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
                    score = calculate_score(attempts, len(word))
                    print("\nCongratulations! You've guessed the word:", word)
                    print("Your score:", score)
                    break

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

starlife()
