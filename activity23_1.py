def GreetWithName(name):
    print(f"hi{name} hope your having a great day")

def Greetperson(name,loc,age):
    print(f"hi{name}")

def FunctionWithReturn(number):
    print(f"this function calculates the summation from 1 to {number}")
    sum=0
    for x in range(1,number +1,1):
        sum += x
    return sum

def Factorial(number):
    print(f"this function calculates the summation from 1 to {number}")
    fact=1
    for x in range(number,0,-1):
        fact *= x
    return sum 
