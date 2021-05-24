import os
import string
from words import choose_word
from images import IMAGES
os.system('cls')


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    index = 0
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            pass
        else:
            return False
        index += 1
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    all_letters = string.ascii_lowercase
    letters_left = ""
    index = 0
    while(index < 26):
        if all_letters[index] in letters_guessed:
            pass
        else:
            letters_left += str(all_letters[index])
        # print(letters_left)
        index += 1
    return letters_left


def hint_generato(secret_word, letters_guessed):
    '''
    Appends the first unguessed letter in letters_guessed
    '''
    index = 0
    while(index < len(secret_word)):
        if(secret_word[index] not in letters_guessed):
            return secret_word[index]
        index += 1


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    remaining_lives = 8
    hint = 1
    letters_guessed = []
    while(remaining_lives > 0):
        print("\n\nAvailable letters: {} ".format(
            get_available_letters(letters_guessed)))
        print("Available attmepts : {}".format(remaining_lives))
        if(hint == 1):
            print("Available hints : {}".format(hint))
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if(letter == "hint" and hint == 1):
            letters_guessed.append(hint_generato(secret_word, letters_guessed))
            hint -= 1
            print("guessed word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
            else:
                continue
        else:
            while (letter < 'a' or letter > 'z' or len(letter) > 1 or (letter == "hint" and hint == 0)):
                print("Invalid Input! Enter Again")
                guess = input("Please guess a letter: ")
                letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            remaining_lives -= 1
            print("You have " + str(remaining_lives) + " attempts remaining")
            if(remaining_lives == 0):
                print("You Lost")
                print(IMAGES[len(IMAGES) - remaining_lives - 1
                             ])
                print("\n Secret Word : ", secret_word)
                break
            print(IMAGES[len(IMAGES) - remaining_lives - 1
                         ])
            print("")


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
