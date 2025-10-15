name=input("enter your name-->")

print("+++++++++++++++++++++++")
print("ODD NUMBER SELECTOR, PRESS 0 TO STOP THE LOOP")
print("\n+++++++++++++++++++++++")

f= True
sum= 0
odd = ""

while f == True:
    num = eval(input("input a random number -->"))

    if num %2 == 1:
        print("odd number detected")
        sum += num
        odd += str(num) + " "

    elif num == 0:
        print("loop terminated")
        break
    else:
        if num%2 == 0:
            print("even number detected ....")
        else:
            print("invalid number/input")
        continue

print(f"hi{name}, the sum of all odd nunmbers is {sum}")
print(f"odd numbers include the ff ->{odd}")
        
