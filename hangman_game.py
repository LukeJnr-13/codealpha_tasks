import random

WORDS = ["apple", "chair", "happy", "window", "jump"]
MAX_WRONG = 6

def display_word(word, guessed):
    """Show the word with unguessed letters as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)

def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0
    
    print("=== HANGMAN ===")
    print(f"Guess the word. You can miss {MAX_WRONG} times.\n")

    while wrong < MAX_WRONG:
        print(display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print(f"Guessed so far: {', '.join(sorted(guessed)) or 'none'}")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

        if all(letter in guessed for letter in word):
            print(f"You won! The word was '{word}'.")
            return

    print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
        break
    print()