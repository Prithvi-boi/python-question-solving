
'''------------------------------------------------------------------------------------------------

    Write a take two collection as a = ["red" , "yellow", "green"] and b = ["apple" , "banana", "grapes"]
    print the value using nested for to display the collections

'''


a = ["red" , "yellow", "green"] 
b = ["apple" , "banana", "grapes"]

for x in a:
    for y in b:
        print(x,y)

print("\n")

i = 0
while i < len(a):
    j = 0
    while j < len(b):
        print(a[i], b[j])
        j += 1
    i += 1