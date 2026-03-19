import random

words = ["python", "apple", "chair", "table", "robot"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 You won! The word is:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("💀 You lost! The word was:", word)