
'''
Practical 6 - set operation 
- two set of student names
- create sets for two classes
- find the union of both sets (student in either class)
- find the intersection
- find the difference
- check if a student is part of a sets using membership operator
'''

# Two sets of student names for Class A and Class B
class_A = {
    "PRITHVI BELDAR",
    "GALFAT VICKY",
    "MAHADIK HARSH",
    "RISHON MATHAI",
    "DOLAS ATHARV",
    "CHAUHAN PRIYANKA",
    "SHETE VARUN",           
    "UZMA NAYEEM"            
}

class_B = {
    "TIWARI PRATHAM",
    "TAMTA HIMESH",
    "YADAV ANIKET",
    "SAUMYA KANTI",
    "SAID KARAN",
    "SHETE VARUN",          
    "UZMA NAYEEM",          
    "HRITIKA CHETAN"
}

# Students in either class
union_students = class_A.union(class_B)
print("Union of both classes (students in either class):")
print(union_students)
print()

# Students common to both classes
intersection_students = class_A.intersection(class_B)
print("Intersection (students in both classes):")
print(intersection_students)
print()

# Students only in Class A
only_class_A = class_A.difference(class_B)
print("Students only in Class A:")
print(only_class_A)
print()

# Students only in Class B
only_class_B = class_B.difference(class_A)
print("Students only in Class B:")
print(only_class_B)
print()

# Check if a student is in a class
student_to_check = "RISHON MATHAI"
print(f"Checking membership for: {student_to_check}")
print(f"In Class A? {'Yes' if student_to_check in class_A else 'No'}")
print(f"In Class B? {'Yes' if student_to_check in class_B else 'No'}")
