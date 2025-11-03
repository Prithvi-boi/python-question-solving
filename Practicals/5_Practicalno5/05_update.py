
contacts = {
    'cont1': {
        "name": "Ajay Devgan",
        "phone": "+91 98214 56734"
    },
    'cont2': {
        "name": "Bobby Deol",
        "phone": "+91 91234 56789"
    },
    'cont3': {
        "name": "Christopher Nolan",
        "phone": "+91 87965 43210"
    },
    'cont4': {
        "name": "Prithvi Beldar",
        "phone": "+91 70123 45678"
    },
    'cont5': {
        "name": "Shah Rukh Khan",
        "phone": "+91 80897 65432"
    }
}

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

update_contact()