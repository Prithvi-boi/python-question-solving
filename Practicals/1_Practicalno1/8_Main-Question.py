'''
    PYTHON - PRACTICAL NO 01
    ------------------------
    Write a program to calculate the Average and grade of a student based on marks entered , Use if elif else condition to assign grades.
    like a , b , c ... f grades. Use a For loop to input marks for 5 subjects and calculate the average.
    Use a While loop to ask the user if they want to calculate another students grade.

'''

while True:
    get_Student_name = input("Enter your name: ")

    subject = ["Python", "Science", "Maths", "English", "Hindi"]    # Creating an array for collection of subjects
    count = 0                                                       # count will use as index value to access subject variable elements
    total_marks = 0                                                 # initial total marks is 0 , each time the user enter marks we will add them into total marks

    for x in range(5):                                              
        if x >= 0:
            get_Subject_marks = float(input(f"Enter {subject[count]} Marks: "))

            while get_Subject_marks > 100 or get_Subject_marks < 0:
                print("Marks must be under 0 to 100")
                get_Subject_marks = float(input(f"Enter {subject[count]} Marks: "))

            count += 1
            total_marks += get_Subject_marks

    average = total_marks/5

    print("Student Name: ", get_Student_name)
    print("Total marks: ", round(total_marks),"/ 500")
    print("percentage: ", round(average),"%")

    if average <= 100 and average >= 85: 
        print("Your is Grade : A  and you got:" , average,"%")
    elif average < 85 and average >= 70: 
        print("Your is Grade : B  and you got:" , average,"%")
    elif average < 70 and average >= 50: 
        print("Your is Grade : C  and you got:" , average,"%")
    elif average < 50 and average >= 35: 
        print("Your is Grade : D  and you got:" , average,"%")
    else:
        print("Your is Grade : F  and you got:" , average,"%")

    again = input("Do you want to calculate another students grades?(yes/no): ").strip().lower()
    
    if again == "no":
        print("Ok bye")
        break

    if again != "yes" :
        while True:
            print('Invalid, type "yes" or "no" only ')
            again = input("Do you want to calculate another students grades?(yes/no): ").strip().lower()

            if again == "yes":
                break
            elif again == "no":
                print("Ok bye")
                break_outer = True
                break
            
        if break_outer:
            break 