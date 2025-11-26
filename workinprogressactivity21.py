import os
import json

os.system('cls' if os.name == 'nt' else 'clear')

print("DLL STUDENT INFORMATION SYSTEM")
print("++++++++++++++++++++++++++++++")

while True:
    print("\nSelect from the following options")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION")
    print("C - IF/ELSE FUNCTION")
    print("D - LOOP FUNCTION")
    print("E - EXIT SYSTEM")

    choice = input("\nInput your choice ---> ").lower().strip()

    # ----------------------
    # PRINT FUNCTION (A)
    # ----------------------
    if choice == 'a':
        print("\nYou selected PRINT FUNCTION")
        print("1 - Information about the code")
        print("2 - Run the code")

        sub = input("Choose ---> ").strip()

        if sub == '1':
            print("\n--- INFORMATION ABOUT PRINT FUNCTION ---")
            print("The print() function displays text or variables on the screen.")
            print("Example: print('Hello')")
        elif sub == '2':
            print("\n--- RUNNING PRINT FUNCTION EXAMPLE ---")
            print("Hello! This is the print function running.")
        else:
            print("Invalid selection.")

        input("\nPress Enter to continue...")
        continue

    # ----------------------
    # INPUT FUNCTION (B)
    # ----------------------
    elif choice == 'b':
        print("\nYou selected INPUT FUNCTION")
        print("1 - Information about the code")
        print("2 - Run the code")

        sub = input("Choose ---> ").strip()

        if sub == '1':
            print("\n--- INFORMATION ABOUT INPUT FUNCTION ---")
            print("The input() function lets the user enter information.")
            print("Example: name = input('Enter your name: ')")
        elif sub == '2':
            print("\n--- RUNNING INPUT FUNCTION EXAMPLE ---")
            name = input("Enter your name: ")
            print("Hello,", name)
        else:
            print("Invalid selection.")

        input("\nPress Enter to continue...")
        continue

    # ----------------------
    # IF/ELSE FUNCTION (C)
    # ----------------------
    elif choice == 'c':
        print("\nYou selected IF/ELSE FUNCTION")
        print("1 - Information about the code")
        print("2 - Run the code")

        sub = input("Choose ---> ").strip()

        if sub == '1':
            print("\n--- INFORMATION ABOUT IF/ELSE ---")
            print("If/Else is used for decisions in Python.")
            print("Example: if x > 10: print('Big')")
        elif sub == '2':
            print("\n--- RUNNING IF/ELSE EXAMPLE ---")
            x = int(input("Enter a number: "))
            if x > 10:
                print("Number is big.")
            else:
                print("Number is small.")
        else:
            print("Invalid selection.")

        input("\nPress Enter to continue...")
        continue

    # ----------------------
    # LOOP FUNCTION (D)
    # ----------------------
    elif choice == 'd':
        print("\nYou selected LOOP FUNCTION"
