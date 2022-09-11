import random
from hangman_guess_word import l

def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word
secret_word = random.choice(l).lower()
hangman(secret_word)

def main():
    global user
    user=input("Hmmmmmmmm CHOOSE 👉 ")
    if user=="Yes":
        print("let's begin the game 😎")
        hangman()
    else:
        print("See you when you are in mood to play the game ✌🏻")
main()