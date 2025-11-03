'''
Practical 5 - Dictionary Based application
- build a phone book application in which first add new contact to the dictionary 
- search for a contact by name 
- update an existing contact number
- delete a contact 
- display all contact in alphabetical order of names
'''


contacts = {}
contact_count = 1

print("\n---- Choose any 1 Options ----  \n" \
      "  1. Add Contacts                 \n" \
      "  2. Display Contact list         \n" \
      "  3. Search Contact               \n" \
      "  4. Update Existing Number       \n" \
      "  5. Delete Contact               \n" \
      )


#Adding contacts
def add_contact():
    global contact_count # allows function to modify the global variable instead of making a local copy

    new_name = input("Enter Contact Name: ").strip().lower()
    take_phone = int(input("Enter Contact's Phone Number: "))

    new_phone = str(take_phone).strip()
    contacts['cont' + str(contact_count)] = {
            'name': new_name,
            'phone': new_phone,
        }
    
    contact_count +=1

# Displaying Contacts
def display_contacts():
    details = []

    for keys in contacts:
        (name,phone) = contacts[keys].values()

        details.append([name,phone])
    details.sort()

    print("\n Sr.no.    Name               | Phone")
    print("-------------------------------------")

    srnum = 1
    for i in range(len(details)):

        space_limit = 18
        req_space = space_limit - len(details[i][0])
        spaces = " " * req_space

        print("  ",srnum,"  -  ",details[i][0].capitalize(),spaces,"|",details[i][1])
        srnum += 1
    
# Search Contact
def search_contact():
    user_check = input("Check This Contact: ")

    found = False
    for id, info in contacts.items():
        if user_check.lower() in info["name"].lower():
            print("-- Contact Available --")
            print("Name  :", info["name"])
            print("Phone :", info["phone"])
            found = True
            break

    if not found:
        print("Contact Unavailable")

# Delete Contacts
def delete_contact():
    delete_contact = input("Delete contact by name: ")

    found = False
    for id, info in contacts.items():
        if delete_contact.lower() in info["name"].lower():
            print("-- Contact delete --")
            print("Name  :", info["name"])
            print("Phone :", info["phone"])
            
            found = True
            if found == True:
                contacts.pop(id)
                del info['name']
                del info['phone']
            break

    if not found:
        print("Contact Unavailable")

#Update Contacts
def update_contact():
    display_contacts()
    update_contact = input("Which Contact You want to update: ")
    
    check = input("Want to update name or number: ")

    if check == 'name':
        update_name = input("Enter Name: ")
    elif check == 'number':
        update_number= input("Enter Number: ")

    found = False
    for id, info in contacts.items():
        if update_contact.lower() in info["name"].lower():

            found = True
            if found == True:
                if check == 'name':
                    info['name'] = update_name
                elif check == 'number':
                    info['phone'] = update_number

            print("-- Contact Updated --")
            print("Name  :", info["name"])
            print("Phone :", info["phone"])
            break

    if not found:
        print("Contact Unavailable")

while True:
    user_option = int(input("Select Option (1/2/3/4): "))

    if user_option == 1:
        add_contact()
        display_contacts()
    elif user_option == 2:
        display_contacts()
    elif user_option == 3:
        search_contact()
    elif user_option == 4:
        delete_contact()
        display_contacts()
    elif user_option == 5:
        update_contact()
        display_contacts()
    else:
        print(f"There is no option for {user_option}!")