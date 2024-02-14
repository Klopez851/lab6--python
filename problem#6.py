##############################################
# Author: Keidy Lopez
# Filename: problem#6.py
# Description: program that takes a list of items and their pricces and allows one to look the prices of items up later
##############################################

def main():
    # main lists and conditions for while loop
    my_first_condition = True
    my_second_condition = True
    my_item_list = []
    my_item_price_list = []

    # prints out action that needs to be taken
    print('Item Input')

    # while loop that takes items and their prices and stops if 'q'q is entered
    while my_first_condition:
        item1 = input('\tPlease enter more than three letters for the item for sale (q to quit): ')
        if item1.upper() == 'Q':
            my_first_condition = False
        elif len(item1) < 3:
            print('Please enter more than three letters for the item for sale!')
        else:
            my_item_list.append(item1)
            price_item1 = input('\tPlease enter the price for '+item1+' : ')
            my_item_price_list.append(price_item1)

    # makes a space between the last string and the next string
    print()

    # prints out action that needs to be taken
    print('Item Search')

    # while loop that loops throught a the list of items using a for loop to look for the the 3+ letters in item list
    # that match and prints out the price which in a parallel second list
    while my_second_condition:
        item2 = input('\tPlease enter at least 3 letters of the item to search for to retrieve the price (q to quit): ')
        if item2.upper() == 'Q':
            print('thanks for using my program <3')
            my_second_condition = False
        elif len(item2) < 3:
            print('Please enter more than three letters for the item your searching for!')
        else:
            for item in range(len(my_item_list)):
                if my_item_list[item].startswith(item2):
                    print('the price of '+str(my_item_list[item])+' is: '+str(my_item_price_list[item]))
                    break
            else:
                print('item not previously entered')
                break










if __name__ == "__main__":
    main()