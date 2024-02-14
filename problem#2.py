##############################################
# Author: Keidy Lopez
# Filename: problem#2.py
# Description: program that takes numbers and prints out their sum and average
##############################################

def main():

    # main variables
    mycondition = True
    counter = 0
    total_num = 0

    # while loop that takes integer input, adds the numbers, and stops if 0 or a negative integer is entered
    while mycondition:
        num = int(input(('please enter a positive number (press 0 or a negative interger to quit): ')))
        if num != 0 and num > 0:
            counter += 1
            total_num += num
        elif num == 0 or num < 0:
            mycondition = False

    # prints out sum and total if greater than 0
    if mycondition == False and counter > 0 and total_num > 0:
        print('Your input total is: '+str(total_num)+" and the average is: "+str(total_num/counter))
        print('thanks for using my program <3')

if __name__ == "__main__":
    main()