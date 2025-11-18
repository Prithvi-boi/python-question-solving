'''
Prime number 
'''

num = int(input("Enter a Number: "))

div_count = 0

for i in range(1,num+1):
    div = num % i
    if div == 0:
        div_count += 1
    
if div_count == 2:
    print('Prime number')
else:
    print('Not a Prime number')
        