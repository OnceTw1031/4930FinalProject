import random

# Answer options
word_list = ["twice", "reluv", "tzuyu", "gidle", "aespa", "stayc"]

# Choose a random word
word_to_guess = random.choice(word_list)


# Function to respond to a guess
def get_output(guess, word):
    output = []
    for i in range(5):
        if guess[i] == word[i]:
            output.append('G')  # Green = Correct letter and position
        elif guess[i] in word:
            output.append('Y')  # Yellow = Correct letter but wrong position
        else:
            output.append('X')  # X (Cross) = Letter is not used
    return output


print("Welcome to Kpordle! It's Kpop and Wordle! ")


# Player can make up to 6 guesses
for attempt in range(6):
    guess = input(f"Attempt {attempt + 1}/6: Enter your 5-letter guess: ").lower()

    # Check if the guess is valid
    if len(guess) != 5 or not guess.isalpha():
        print("Invalid guess. Please enter a 5-letter word.")
        continue

    # Provide feedback
    output = get_output(guess, word_to_guess)
    print("Result:", " ".join(output))

    # Check if the guess is correct
    if guess == word_to_guess:
        print("Congratulations! You guessed the word! #StanTwice")
        break
else:
    print(f"Sorry, you didn't guess the word. The word was '{word_to_guess}' #StanTwice.")

