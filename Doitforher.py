import os

# -----------------------------
# A - PRINT FUNCTION
# -----------------------------
def print_info():
    print("\n--- INFORMATION ABOUT PRINT FUNCTION ---")
    print("The print() function displays text on the screen.")
    print("Example: print('Hello')")

def print_run():
    print("\n--- RUNNING PRINT FUNCTION EXAMPLE ---")
    print("Hello! This is the print() function running.")


# -----------------------------
# B - INPUT FUNCTION
# -----------------------------
def input_info():
    print("\n--- INFORMATION ABOUT INPUT FUNCTION ---")
    print("The input() function lets the user type values.")
    print("Example: name = input('Enter name: ')")

def input_run():
    print("\n--- RUNNING INPUT FUNCTION EXAMPLE ---")
    name = input("Enter your name: ")
    print("Hello,", name)


# -----------------------------
# C - IF/ELSE FUNCTION
# -----------------------------
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


# -----------------------------
# D - LOOP FUNCTION
# -----------------------------
def loop_info():
    print("\n--- INFORMATION ABOUT LOOPS ---")
    print("Loops repeat code many times.")
    print("Example: for i in range(5): print(i)")

def loop_run():
    print("\n--- RUNNING LOOP EXAMPLE ---")
    for i in range(1, 6):
        print("Loop:", i)


# -----------------------------
# E - EVAL + INPUT
# -----------------------------
def eval_info():
    print("\n--- INFORMATION ABOUT eval(input()) ---")
    print("eval(input()) evaluates what the user types as Python code.")
    print("Useful for math expressions like: 5 * (3 + 2)")
    print("⚠ WARNING: eval can run ANY code, so it is dangerous.")

def eval_run():
    print("\n--- RUNNING eval(input()) EXAMPLE ---")
    expr = input("Enter a math expression (e.g. 5*(3+2)): ")
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)


# -----------------------------
# F - int + input
# -----------------------------
def intinput_info():
    print("\n--- INFORMATION ABOUT int(input()) ---")
    print("int(input()) converts what the user types into an integer.")
    print("Example: age = int(input('Age: '))")
    print("Only works if the user types a number.")

def intinput_run():
    print("\n--- RUNNING int(input()) EXAMPLE ---")
    try:
        num = int(input("Enter a whole number: "))
        print("Your number squared is:", num * num)
    except:
        print("That is not a valid integer.")


# -----------------------------
# SUB-MENU HANDLER
# -----------------------------
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


# -----------------------------
# MAIN PROGRAM LOOP
# -----------------------------
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("DLL STUDENT INFORMATION SYSTEM")
    print("++++++++++++++++++++++++++++++\n")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION")
    print("C - IF, ELSE FUNCTION")
    print("D - LOOP FUNCTION")
    print("E - EVAL + INPUT")
    print("F - INT + INPUT")
    print("G - EXIT SYSTEM")

    choice = input("\nInput your choice ---> ").lower().strip()

    if choice == 'a':
        submenu(print_info, print_run, "PRINT FUNCTION")

    elif choice == 'b':
        submenu(input_info, input_run, "INPUT FUNCTION")

    elif choice == 'c':
        submenu(ifelse_info, ifelse_run, "IF/ELSE FUNCTION")

    elif choice == 'd':
        submenu(loop_info, loop_run, "LOOP FUNCTION")

    elif choice == 'e':
        submenu(eval_info, eval_run, "EVAL + INPUT")

    elif choice == 'f':
        submenu(intinput_info, intinput_run, "INT + INPUT")

    elif choice == 'g':
        print("\nExiting the system...")
        break

    else:
        print("Invalid input. Try again.")
        input("Press Enter to continue...")
