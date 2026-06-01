import random
import shutil

words = [ "car", "bike" , "friend"  , "motivation" , "habits" , "love" , "faith" , "distiny" , "god" ,"people"]

word = random.choice(words)
# guess equal to len of the word
guessed = ["_"] * len(word)

attempts = 6
guessed_letters = []

print(" ******************WELCOME TO A SIMPLE HANGMAN GAME**************** ")
print(" ********************YOU HAVE TO GUESS A WORD****************** ")

print(" ".join(guessed))


# main logic of the game
print(" ")
print(words)
while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only alphabet letters: ")
        continue
    if guess in guessed_letters:
        print("\nYou have already guess that letter: ")
        continue
    guessed_letters.append(guess)

    if guess in word:
       print("Correct")

       for i in range(len(word)):
           if word[i] == guess:
               guessed[i] = guess
              # print(" ".join(guessed))
    else:
        attempts -= 1
        print("Wrong! Attempts left:" ,  attempts)
        print("Word:", " ".join(guessed))
        print("Guessed Letters:", ", ".join(guessed_letters))
    #print(" ".join(guessed))

if "_" not in guessed:
    print("Conguratulations! You Win! ") #conguratulations
    print("The word was:" , word)
else:
    print("\nBetter luck next time") 
    print("The word was" , word)              