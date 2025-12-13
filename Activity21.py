import random

print("TRY YOUR LUCK")
print("________________")

a = random.randint(1,10)
b = 0
c = True
e = input("Enter Your Name-->")
while c == True:
    d = eval(input("Enter a number 1-10--->"))
    b += 1
    if d == a:
        print("Winner")
        break
    else:
        print("Choose Again")

print(f"Hi {e}, Your Tries is {b}")
