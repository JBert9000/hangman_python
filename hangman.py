from tkinter import *
import tkinter.messagebox
import random


HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
===========''', '''
    +---+
    |   |
    0   |
        |
        |
        |
===========''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
===========''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
===========''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
===========''', '''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
===========''', '''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
===========''']

words = 'mario luigi bowser link toad peach yoshi wario waluigi donkey-kong king-koopa zelda ganondorf'.split()

def getRandomWord(wordList):
        # This function returns a random string from the list of strings.
        wordIndex = random.randint(0, len(wordList) - 1)
        return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
        print(HANGMANPICS[len(missedLetters)])
        print()

        print('Missed letters:', end = ' ')
        for letter in missedLetters:
                print(letter, end = ' ')
        print()

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)): # replace blanks with correctly guessed letters
                if secretWord[i] in correctLetters:
                        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
                elif secretWord[i] == '-':
                        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]


        for letter in blanks: # show the secret word with spaces in betweem each letter
                print(letter, end = ' ')
        print()

def getGuess(alreadyGuessed):
        # Returns the letter the player entered. This function makes sure the player entered a sinfle letter,
        # and not something else.
        while True:
                print('Guess a letter')
                guess = input()
                guess = guess.lower()
                if len(guess) != 1:
                        print('Excuse me? You can only type 1 letter at a time.')
                elif guess in alreadyGuessed:
                        print('You already guessed this letter! Tyr again')
                elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
                        print('only English letters please!')
                else:
                        return guess

def playAgain():
        # This function returns True if the player wants to play again, otherwise it returns False
        print('Do you want to play again? (y or n)')
        return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

        # Let the player type in a letter
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
                correctLetters = correctLetters + guess

                # Check if the player has won
                foundAllLetters = True
                for i in range(len(secretWord)):
                        if secretWord[i] not in correctLetters:
                                foundAllLetters = False
                                break

                if foundAllLetters:
                        print('Nice job! The word is "' + secretWord + '"! You have won.')
                        gameIsDone = True
        else:
                missedLetters = missedLetters + guess

                # Check if player has guessed too many times and lost
                if len(missedLetters) == len(HANGMANPICS) - 1:
                        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                        print('Not good enough, \nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '". Try '
                                                                                                         'harder next time.')
                        gameIsDone = True

                if gameIsDone:
                        if playAgain():
                                missedLetters = ''
                                correctLetters = ''
                                gameIsDone = False
                                secretWord = getRandomWord(words)
                        else:
                                break
