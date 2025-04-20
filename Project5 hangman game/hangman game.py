import random

words = ["python", "java", "kotlin", "javascript", "html", "css", "ruby", "swift", "go", "rust"]
word = random.choice(words)
guesses_letters = []
attempts = 6

print("Welcome to Hangman Game - Project 5")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guesses_letters:
        print("You have already guessed that letter.")
        continue

    guesses_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    # Show current state of the word
    displayed_word = " ".join([letter if letter in guesses_letters else "_" for letter in word])
    print("\nWord: ", displayed_word)

    if "_" not in displayed_word:
        print(f"\nCongratulations! You guessed the correct word: {word}")
        break

# Game over condition
if "_" in displayed_word:
    print(f"\nGame over! The correct word was: {word}")
