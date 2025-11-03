'''
Practical 4- Tuple and their applications
- Create a program to handle student record which will stores student details like roll number , name , marks in a tuple
- use tuple unpacking the retrieve the details
- then creates a function that accepts a variable len argument tuple 
- then calculate the avg marks of the student
'''


student_details = (
    # Student name       | Roll number      | Marks
    ["AARYA BHASKAR YADAV"     ,2501, [98,45,78,83,60]],
    ["BELDAR PRITHVI RAJKUMAR" ,2505, [48,88,45,90,68]],
    ["CHRIS JACOB BINOY"       ,2515, [78,75,76,74,80]],
    ["DHOLU DEVANSHI KAMLESH"  ,2519, [66,65,23,81,69]],
    ["GALFAT VICKY RAJU"       ,2523, [67,55,80,93,97]]
)

(student1,student2,student3,student4,student5) = student_details


#----------------------------------------------------------------------------------
# with * means: get_variable = ( student1, )   ← A tuple with one element
# without means: get_variable = ["AARYA BHASKAR YADAV", 2501, [98,45,78,83,60]]

def calculate_avg(*get_varible): 
    for details in get_varible:
        (name, rollno, marks) = details

        sum = 0
        for x in marks:
            sum += x 
        
        avg = sum/len(marks)

        print(f"\n | Student name:{name} \n | Roll number: {rollno},\n | Total marks: {sum},\n | Average marks: {avg} \n")


print("\n")
print("Enter Your roll number to get details")

def value_checker():
    check = int(input("Type Here: "))
    if check == 2501:
        calculate_avg(student1)
    elif check == 2505:
        calculate_avg(student2)
    elif check == 2515:
        calculate_avg(student3)
    elif check == 2519:
        calculate_avg(student4)
    elif check == 2523:
        calculate_avg(student5)
    else: 
        print(f"Roll number '{check}' is not listed yet! Try different")
        value_checker()

value_checker()


    