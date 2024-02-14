##############################################
# Author: Keidy Lopez
# Filename: problem#3.py
# Description: program that returns a list with random numbers between 10-50 after the first 4
##############################################
import random

def main():
    # welcome statement
    print('This program will add 16 random integers in the range 10-50 to an existing list [4,18,19,17] of 4 elements.')
    print('Here are the awesome results!')

    # list variable
    integer_list = [4,18,19,7]

    # for loop that appends random numbers(10-50) to list
    for i in range(1,17):
        num = random.randint(10,50)
        integer_list.append(num)

    # prints list
    print('\n', *integer_list)


if __name__ == "__main__":
    main()