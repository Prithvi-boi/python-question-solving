
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

        print("  ",srnum,"  -  ",details[i][0],spaces,"|",details[i][1])
        srnum += 1
    