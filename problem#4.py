##############################################
# Author: Keidy Lopez
# Filename: problem#4.py
# Description: program that appends numbers to a list using
##############################################

def main():
    # welcome statement
    print('This program will accept integers and save all the unique integers entered')

    # main variable and condition
    myCondition = True
    num_list = []

    # while loop that takes numbers and adds them to a list(no repeats) and stops if 0 is entered
    while myCondition:
        num = int(input('Enter an integer for me to save or a zero (0) to stop: '))
        if num == 0:
            myCondition = False
        elif num not in num_list:
            num_list.append(num)

    # prints out list
    print('Here is your list: ', *num_list)




if __name__ == "__main__":
    main()