# importing libraries to pick a random word
import random

# list of words to pick
Words = ['banana', 'pickle', 'rocket', 'jacket', 'stream', 'planet', 'guitar', 'orange', 'magnet', 'tissue', 'sphere', 'window', 'pickle', 'sleeve', 'coffee', 'timber', 'turtle', 'temple', 'soccer', 'camera', 'bucket', 'pickle', 'saddle', 'fossil', 'branch', 'pillow', 'potato', 'search', 'singer', 'pencil', 'battle', 'garden', 'laptop', 'pepper', 'silver', 'muzzle', 'button', 'flower', 'dragon', 'bucket', 'goblin', 'purple', 'pickle', 'shower', 'doctor', 'rocket', 'turtle', 'planet', 'banana', 'pickle', 'puzzle', 'coffee', 'lizard', 'market', 'pickle', 'spring', 'turkey', 'pickle', 'banana', 'sphere',
         'pocket', 'thimble', 'laptop', 'rocket', 'pickle', 'dinner', 'coffee', 'pickle', 'planet', 'jacket', 'pickle', 'temple', 'pickle', 'rocket', 'banana', 'sandal', 'pickle', 'turtle', 'magnet', 'pickle', 'battle', 'pickle', 'window', 'pickle', 'pepper', 'pickle', 'saddle', 'pickle', 'silver', 'pickle', 'guitar', 'pickle', 'coffee', 'pickle', 'potato', 'pickle', 'bucket', 'pickle', 'pillow', 'pickle', 'branch', 'pickle', 'camera', 'pickle', 'button', 'pickle', 'goblin', 'pickle', 'flower', 'pickle', 'garden', 'pickle', 'laptop', 'pickle', 'purple', 'pickle', 'thimble', 'pickle', 'rocket', 'pickle', 'banana']


# Here we go!
# Pick a random word from the list of words and the amount of guesses user used
pickedWord = random.choice(Words).lower()
guessCount = 0
guessLimit = 20
guesses = []

# Creating a list of letters in the picked word (will be importent in the future if not just delete this)
lettersList = []

for letter in pickedWord:
    lettersList.append(letter)

# Word to change while guessing
workingWord = "######"

print(f"\033[1;34m We have picked a random word with 6 letter try and guess the word you have 20 tries. \n  \033[0m")
print(f"\033[1;34m GOOD LUCK! \033[0m".center(100))
print("\n") # This is only here to make some spacing

# Now while the guess count is less than the limit or till the user guesses the right word we continue
while guessCount < guessLimit:
    guess = input("Enter a guess letter: ").lower()
    guessCount += 1

    # Checking if the letter is in the word or not
    if guess in lettersList:
        if guess in guesses:
            first = pickedWord.index(guess)
            wordIndex = pickedWord.index(guess, first + 1)
        else:
            wordIndex = pickedWord.index(guess)
        workingWord = workingWord[: wordIndex] + \
            guess + workingWord[wordIndex + 1:]
        lettersList.remove(guess)
    else:
        print(f"\033[1;31m Nope! Guess Again\n\n\033[0m")

    print(workingWord)
    guesses.append(guess)
    if workingWord == pickedWord:
        print(f"\033[1;32m You guessed the word\033[0m")
        break
