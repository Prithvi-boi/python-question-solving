'''
Write a Python program that takes a number as input, converts it to both integer and float, and prints their types.
'''

take_number = input("Enter a Number: ") 

print(type(take_number),":",take_number) 

print("--- After conversion ---") 

print(type(int(take_number)),":",int(take_number)) 
print(type(float(take_number)),":",float(take_number))