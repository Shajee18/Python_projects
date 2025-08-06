import random

def play_hangman():
    words = ["gobi", "mtr", "alu", "pyaaz"]
    secret_word = random.choice(words)
    display_word = ["_"] * len(secret_word)
    guessed_letters = []
    attempts = 6

    print("\n🎮 Welcome to Hangman!!")
    print("🍽️ Roti Edition")
    print("Word to guess:", " ".join(display_word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only a single alphabet letter.")
            continue

        # Already guessed check
        if guess in guessed_letters:
            print("❗ You have already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in secret_word:
            print("✅ Correct guess!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Current word:", " ".join(display_word))

        # Win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", secret_word)
            break
    else:
        # Lose condition
        print("\n💀 Game Over! The word was:", secret_word)

# 🔁 Loop for replay
while True:
    play_hangman()
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("👋 Thanks for playing Hangman. Goodbye!")
        break



    


            
    