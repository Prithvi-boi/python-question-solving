'''
Practical 5 - Dictionary Based application
- build a phone book application in which first add new contact to the dictionary 
- search for a contact by name 
- update an existing contact number
- delete a contact 
- display all contact in alphabetical order of names
'''

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
