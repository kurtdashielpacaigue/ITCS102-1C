import os


def print_info():
    print("\n--- INFORMATION ABOUT PRINT FUNCTION ---")
    print("The print() function displays text on the screen.")
    print("Example: print('Hello')")

def print_run():
    print("\n--- RUNNING PRINT FUNCTION EXAMPLE ---")
    print("Hello! This is the print() function running.")



def input_info():
    print("\n--- INFORMATION ABOUT INPUT FUNCTION ---")
    print("The input() function lets the user type values.")
    print("Example: name = input('Enter name: ')")

def input_run():
    print("\n--- RUNNING INPUT FUNCTION EXAMPLE ---")
    name = input("Enter your name: ")
    print("Hello,", name)



def ifelse_info():
    print("\n--- INFORMATION ABOUT IF/ELSE ---")
    print("If/Else is used for decision making.")
    print("Example: if x > 10: print('big')")

def ifelse_run():
    print("\n--- RUNNING IF/ELSE EXAMPLE ---")
    x = int(input("Enter a number: "))
    if x > 10:
        print("The number is big.")
    else:
        print("The number is small.")



def loop_info():
    print("\n--- INFORMATION ABOUT LOOPS ---")
    print("Loops repeat code many times.")
    print("Example: for i in range(5): print(i)")

def loop_run():
    print("\n--- RUNNING LOOP EXAMPLE ---")
    for i in range(1, 6):
        print("Loop:", i)



def submenu(info_func, run_func, title):
    print(f"\nYou selected: {title}")
    print("1 - Information about this code")
    print("2 - Run this code")

    sub = input("Choose ---> ").strip()

    if sub == '1':
        info_func()
    elif sub == '2':
        run_func()
    else:
        print("Invalid selection.")

    input("\nPress Enter to continue...")



while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("DLL STUDENT INFORMATION SYSTEM")
    print("++++++++++++++++++++++++++++++\n")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION")
    print("C - IF, ELSE FUNCTION")
    print("D - LOOP FUNCTION")
    print("E - EXIT SYSTEM")

    choice = input("\nInput your choice ---> ").lower().strip()

    if choice == 'a':
        submenu(print_info, print_run, "PRINT FUNCTION")
        continue

    elif choice == 'b':
        submenu(input_info, input_run, "INPUT FUNCTION")
        continue

    elif choice == 'c':
        submenu(ifelse_info, ifelse_run, "IF/ELSE FUNCTION")
        continue

    elif choice == 'd':
        submenu(loop_info, loop_run, "LOOP FUNCTION")
        continue

    elif choice == 'e':
        print("\nExiting the system...")
        break

    else:
        print("Invalid input. Try again.")
        input("Press Enter to continue...")
