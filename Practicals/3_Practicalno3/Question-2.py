'''
(2) LIST AND THEIR OPERATIONS.
- Create a shopping list application in which first add item to a list, then remove it if it's purchased.
- sort the list alphabetically.
- print the list of an item after each operation.
'''

# To loop Deleting and Creating Original list
while True:
    while True: # This loop will stop after you Tap enter (ie: Empty String)
        create_list = input("-- Press enter to Create a List --")
        if create_list != "":
            print("Just Tap Enter!")
        else:
            print("list is Created! \n")
            break

    orginal_list = []                   # Creating original list

    list_count = len(orginal_list)      # This Variable will track length of the list
    list_limit = 5                      # setting a limit to this list

    print('-- Now Add items to your list --')

    while list_count < list_limit:      # Keep adding items until length of the list is equal to limit
        add_items = input(f"Item {list_count+1}: ").capitalize()
        orginal_list.append(add_items)
        list_count += 1                 

    orginal_list.sort()                 # Sorting original list alphabetically 

    print('\n-- Your list --')          # Printing original list using for loop
    for x in range(list_limit):
        print(x+1,'-',orginal_list[x])

    #---------------- Checking if the user want to remove purchased item or not --------------------------#

    continue_check = input("Want to remove purchased items?(yes/no): ").lower()     

    if continue_check == "yes":          # if yes then create a purchased list to store those removed items
        purchased_items = []
        new_list_count = len(purchased_items)   # setting the purchased list same as the original list

        print("\n Okhay! type 'done' if you want to stop removing")

        # Using a While loop to keep removing untill the user type done. 
        while True:
            select = input(f"Type purchased item {new_list_count}/5: ").capitalize()
            purchased_items.append(select)
            if select != 'Done':
                new_list_count +=1
                orginal_list.remove(select)
                print(select,"is removed from the list")
                if new_list_count == 5:                         # if the user remove everything print: 'everything is removed'
                    print(f"Every items is removed {new_list_count}/5")
                    break
            else:
                purchased_items.remove("Done")  # after the user type 'done' , we remove done from the list and break the loop
                break
            
        y = (list_limit)-len(purchased_items) # setting the value of range --> eg:  5 - ( 3 purchase items) = 2 

        print('\n-- Current list --')   # Printing edited original list using for loop
        for x in range(y):
            print(x+1,'-',orginal_list[x])

    #---------------- Asking user to select any one option --------------------------#
    
    print(''' ----- Select Option -----
    1. Delete the current list and make a new one
    2. See Purchased items list
    ''') 
    select_option = int(input(" Enter (1 or 2): "))
    if select_option == 1:                              # if '1' , then delete original list and restart the program
        del orginal_list
        continue
    
    elif select_option == 2:                            # if '2' , show purchased list and exit the loop/program
        print('\n-- Purchased items list --')

        y = len(purchased_items)
        for x in range(y):
            print(x+1,'-',purchased_items[x])
        break

