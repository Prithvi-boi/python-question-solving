
'''
Write a Python program that takes two numbers from the user and demonstrates all types of operators in Python: arithmetic, comparison, logical, assignment, bitwise, and identity operators. Print at least one example of each type using the two numbers.
'''
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num_list = [1,2,3,4,5]

print("\n --- Arithmetic operators --- ")
print("Addition      :",num1 + num2)
print("Subtraction   :",num1 - num2)
print("Multiplication:",num1 * num2)
print("Division      :",num1 / num2)
print("Modulus       :",num1 % num2)
print("Exponention   :",num1 ** num2)
print("Floor division:",num1 // num2)

print("\n --- Relational operators --- ")
print("Equal to (==)              :", num1 == num2)
print("Not equal to (!=)          :", num1 != num2)
print("Greater than (>)           :", num1 > num2)
print("less than (<)              :", num1 < num2)
print("Greater than equal to (>=) :", num1 >= num2)
print("less than equal to (<=)    :", num1 <= num2)

print("\n --- Assignment operators --- ")
num1 += num2    ; print(("+=  :"),num1)
num1 -= num2    ; print(("-=  :"),num1)
num1 *= num2    ; print(("*=  :"),num1)
num1 /= num2    ; print(("/=  :"),num1)
num1 %= num2    ; print(("%=  :"),num1)
num1 **= num2   ; print(("**= :"),num1)
num1 //= num2   ; print(("//= :"),num1)

print("\n --- Logical operators --- ")
print("AND - num2 > 0 and num2 < 100  :",num2 > 0 and num2 <= 100)
print("OR  - num2 > 0 or num2< 10     :",num2 > 0 or num2 < 10)
print("NOT - num2 > 0 and num2 <= 100 :",not (num2 > 0 and num2 <= 100))

print("\n --- Membership operators --- ")
print("  In   - num2 in num_list     :",num2 in num_list)
print("Not in - num2 not in num_list :",num2 not in num_list)

print("\n --- Identity operators --- ")
print("  Is   - num1 is num2     :",num1 is num2)
print("Is not - num1 is not num2 :",num1 is not num2)

print("\n --- BItwise operators --- ")
print("&  :", int(num1) & num2)
print("|  :", int(num1) | num2)
print("^  :", int(num1) ^ num2)
print("<< :", int(num1) << num2)
print(">> :", int(num1) >> num2)
print("~  :", int(~ num2))

