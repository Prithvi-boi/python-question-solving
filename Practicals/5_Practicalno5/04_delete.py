

contacts = {
    'cont1': {
        "name": "Shah Rukh Khan",
        "phone": "+91 80897 65432"
    },
    'cont2': {
        "name": "Christopher Nolan",
        "phone": "+91 87965 43210"
    },
    'cont3': {
        "name": "Bobby Deol",
        "phone": "+91 91234 56789"
    },
    'cont4': {
        "name": "Prithvi Beldar",
        "phone": "+91 70123 45678"
    },
    'cont5': {
        "name": "Ajay Devgan",
        "phone": "+91 98214 56734"
    }
}


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

delete_contact()