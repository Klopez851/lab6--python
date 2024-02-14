##############################################
# Author: Keidy Lopez
# Filename: problem#8.py
# Description: word guessing game
##############################################
from words import Words


def main():
    # code to get word inmport to work
    MyWords = Words()
    myString = MyWords.getRandWord()
    MyWords = Words()
    myList = MyWords.getRandWordList(20)

    # beginning of my code and welcome statement
    print('Let\'s play a word guessing game! (case sensitive)')

    # main inputs and variables
    word_bank_amount = int(input('how many words do you want to try to guess'))
    word_bank = MyWords.getRandWordList(word_bank_amount)
    myCondition = True

    # while loop that continues the game until there are no more words in the bank or the user doesnt want to play
    while myCondition:

        # for loop that loops the number of words that are in word bank and prints out amount of letters in word being
        # guessed and tells user if they ran out of words
        for i in range(len(word_bank)):
            if myCondition == False:
                break
            else:
                print('your word has', len(word_bank[i]), 'letters')

            # for loop that prints out letters one at a time and determines whether user guesses right and whats to play
            # again
            for let in range(len(word_bank[i])):
                print('letter' +str([let+1])+':', word_bank[i][let])
                word_guess = input('Try to guess the word: ')

                if word_guess == word_bank[i]:
                    print('You got it!')
                    choice = input('\nwould you like to play again(Y/N): ')

                    if choice.upper() != 'Y':
                        myCondition = False
                        print('thanks for playing')
                        break
                    else:
                        break
            else:
                print('Sorry, the word was '+word_bank[i])
                choice2 = input('would you like tp play again(Y/N):')
                if choice2.upper() != 'Y':
                    print('thanks for playing')
                    myCondition = False
                    break
        else:
            print('sorry you\'re all out of words!')
            myCondition = False



if __name__ == "__main__":
    main()