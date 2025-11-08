import random

# Step 1: Predefined list of words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Step 2: Randomly choose one
secret_word = random.choice(words)

# Step 3: Initialize game variables
guessed_letters = []
attempts = 6
word_display = ["_"] * len(secret_word)

print("🎯 Welcome to Hangman Game!")
print("Guess the fruit name!")
print("You have 6 chances.\n")

# Step 4: Game loop
while attempts > 0:
    print("Word:", " ".join(word_display))
    print(f"Remaining attempts: {attempts}")
    
    guess = input("Enter a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.\n")
        continue
    
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        # Update display
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                word_display[i] = guess
    else:
        print("❌ Wrong guess!\n")
        attempts -= 1

    # Check win condition
    if "_" not in word_display:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("😢 Out of attempts! The word was:", secret_word)
