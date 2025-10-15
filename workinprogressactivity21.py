import random



print("number guessing gaem")
print("++++++++++++++++++++")



random_value = random.randint (1,10)
j = 0
cont = True
name= input("put your name")

while cont == True:
    num = eval(input("guess a number from 1 to 5:"))

    if num == random_value:
        j += 1
        print("!!winner")
        break

    else:
        print("incorrect guess:")
print(f"{name} your tries is {j}")
