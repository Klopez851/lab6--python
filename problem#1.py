##############################################
# Author: Keidy Lopez
# Filename: problem#1.py
# Description: program that generates a random list of lowercase letter but stops at the first vowel
##############################################
import random

def main():
    # list variable
    letter_list = []

    # for loop that prints out list and stops at vowel
    for let in range(1,27):
        letter = random.randint(97,122)

        # adds letter to list if not a vowel
        if letter != 97 and letter != 101 and letter != 105 and letter != 111 and letter != 117:
            letter_list.append(chr(letter))

        # adds letter to list if a vowel and stops loop
        elif letter == 97 or letter == 101 or letter == 105 or letter == 111 or letter == 117:
            letter_list.append(chr(letter))
            break

    # prints out list and done
    print(*letter_list)
    print('Done!')





if __name__=="__main__":
    main()