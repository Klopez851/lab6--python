##############################################
# Author: Keidy Lopez
# Filename: problem#5.py
# Description: program that generates 10 to 30 lottery numbers (random numbers between 10 and 50)
##############################################
import random

def main():
    # main varibles
    num1 = int(input('how many numbers would you like to generate (number has to be between 10-30): '))
    random_list = []

    # if number is not between 10-30 ask user try again
    if num1 < 10 or num1 > 30:
        print('Please enter a number between 10 and 30 !')
        return

    # for loop that generates random numbers between 10-50 and addes to to a list as many times as the user asked(num1)
    for i in range(1, num1+1):
        randNum = random.randint(10,50)
        random_list.append(randNum)

    # prints out list of random number
    print('Your lottery numbers are:',*random_list)


if __name__ == "__main__":
    main()