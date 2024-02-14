##############################################
# Author: Keidy Lopez
# Filename: problem#7.py
# Description: a scramble game that gives you 5 guesses to guess a random srambled word
##############################################
from words import Words
import random

def main():
    # code needed for word import to work
    MyWords = Words()
    myString = MyWords.getRandWord()

    MyWords = Words()
    myList = MyWords.getRandWordList(20)

    # start of my code and welcome statement
    print('Let\'s play a word scramble game!\nYou get 5 guesses.')

    # main conditon and variable
    myCondition = True
    _word = MyWords.getRandWord()

    # while loop that give shuffled word, gives 5 attemps, and tells you whether you guessed right or wrong
    while myCondition:
        print('Your word is: '+str(shuffleWord(_word)))
        for let in range(1,6):
            word_guess = input('Enter your guess ('+str(let)+ ') :')
            if word_guess == _word:
                print('Awesome, you got it!\nThanks for playing!')
                myCondition = False
                break
        else:
            print('the word was '+str(_word)+'\n It was such a simple word can believe you couldn\'t get that ಠ_ಠ')
            myCondition = False


# function that shuffles imported random word
def shuffleWord(word: str)->str:
  shuffled_word = ''.join(random.sample(word, len(word))) # got help from a youtube video, what this does is join an
  return shuffled_word                                    # empty string with a random sample with the parameters of
                                                          # the word and the length of the word (generates a random
                                                          # sequence of letters in the range len(string) pulling the
                                                          # letters used out from the word given) and retruns resulting
                                                          # string


if __name__ == "__main__":
    main()