import random
#List the words and store them.


word_list = []
word_file = open("words.txt")

for word in word_file:
    word_list.append(word.lower().strip())

# Pick a random word

answer = random.choice(word_list)

number_of_guesses = 0
guessed_correct = False

while number_of_guesses < 6 and not guessed_correct :
    # get guess from the user.

    guessedWord = input("Input a 5-letter word and press Enter: ")

    print("You guessed", guessedWord)
    number_of_guesses+=1


def processGuess(theAnswer, theGuess):
    pos = 0
    clue = ""
    for letter in theGuess:
        if letter == theAnswer[pos]:
            clue +="P"
        elif letter in theAnswer:
            clue += "U"
        else:
            clue+= "-" 
        pos +=1
    print(clue)
    return clue == "PPPPP" # returns true if all values are true 

# process the guess
guessed_correct = processGuess(answer, guessedWord)


#display the end or conclusion of the game

if guessed_correct:
    print("Congratulations You've guessed the word in ", number_of_guesses,"guesses")
else:
    print("BOINK BOINK BOINK. The answer is ", answer)
