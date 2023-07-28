import random

def choose_word():
    lst = ['apple', 'black', 'pink', 'white', 'violet', 'newyork', 'hawaii', 'purple', 'blueberries']
    return random.choice(lst)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter an alphabetical letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def draw_hangman(attempts):
    hangman_stages = [
        """
         ____
        |    |
        |
        |
        |
        |_______
        """,
        """
         ____
        |    |
        |    O
        |
        |
        |_______
        """,
        """
         ____
        |    |
        |    O
        |    |
        |
        |_______
        """,
        """
         ____
        |    |
        |    O
        |   /|
        |
        |_______
        """,
        """
         ____
        |    |
        |    O
        |   /|\\
        |
        |_______
        """,
        """
         ____
        |    |
        |    O
        |   /|\\
        |   /
        |_______
        """,
        """
         ____
        |    |
        |    O
        |   /|\\
        |   / \\
        |_______
        """
    ]
    print(hangman_stages[attempts])

def hangman():
    chosen_word = choose_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(chosen_word, guessed_letters))

    while True:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in chosen_word:
            attempts += 1
            print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")
            draw_hangman(attempts)
        
        print(display_word(chosen_word, guessed_letters))

        if '_' not in display_word(chosen_word, guessed_letters):
            print("Congratulations! You guessed the word!")
            break

        if attempts == max_attempts:
            print(f"Sorry, you've run out of attempts. The word was '{chosen_word}'.")
            break

if __name__ == "__main__":
    hangman()
