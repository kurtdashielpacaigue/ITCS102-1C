from activity23_1 import *

print("welcome to my compiler program")
name = input("hi visitor, what is your name -->")

print(f"hi{name}, select from the options below")
print("A - Greet name\nB-Greet  with name,Age,Location\nC-Triangle\nE-Exit")

isCont = True

while isCont == True:
     choice = input("select from A - E-->").lower()

     if choice == 'a':
          name = input("please state your name -->")
          GreetWithName(name)
          continue
     elif choice == 'b':
          number = eval(input("input any number-->"))
          print(f"Factorial of {number}is{Factorial(number)}")
          continue
     elif choice =='c':
          GetTriangle()
          continue
     elif choice == 'e':
          print("program terminated ...")
          break
     else:
          print("invalid choice")
          continue
     
