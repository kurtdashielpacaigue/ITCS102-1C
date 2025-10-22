import random

print("TRY YOUR LUCK")
print("________________")

a = random.randint(1,10)
bruh = 0
balls = True
inn = input("Enter Your Name-->")
while balls == True:
    mv = eval(input("Enter a number 1-10--->"))
    bruh += 1
    if mv == a:
        print("Winner")
        break
    else:
        print("Choose Again")

print(f"Hi {inn}, Your number of Tries is {bruh}")
