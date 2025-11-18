'''
Prime factors 
Amicable number 
Prefect number 
Armstrong number
'''

num = int(input("Enter a Number: "))
factors = []

fact_num = 1

while num != fact_num:
    for x in range(2,num+1):
        if num % x == 0:
            factors.append(x)
            fact_num*2
    break
print(fact_num)
print(factors)