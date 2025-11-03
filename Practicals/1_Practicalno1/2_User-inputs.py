'''
    Write a Python program that asks the user for their name, age, height, and city using input(), and then prints:
'''

name = input("Enter your Name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height(in cm): "))
city = input("Where do you live?: ")

print("Hello", name,"! You are ",age,"years old,",height,"is your height in cm and live in",city,".")
