'''
    Write a program to check if a person can watch a movie: If age ≥ 18 then "Allowed"
    Else, check if they are with a parent. If yes then "Allowed with parent", otherwise "Not allowed".
'''



age = int(input("Enter age: "))


if age >= 18:
    print("Age Verified")
    parents = str(input("Are you With you Parents? (Yes/No):").lower())
    
    if parents == "yes":
        print("Enjoy the Show")
    elif parents == "no":
        print("Not allowed, Watch this movie with your parents")
    else:
        print("Type Yes or No")
else:
    print("Invalid Age")
