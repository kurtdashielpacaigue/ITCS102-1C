import os




def Printinfo():
    print("n\The Print Allows us to show things on screen Whether it be a Variable or Function")
    print("n\----> print() <----- = print('DU DU DU DU MAX VERSTAPPEN') =")
    print("\n--- INFORMATION ABOUT PRINT FUNCTION ---")
    print("The print() function displays text on the screen.")
    print("Example: print('Hello')")

    
def PrintRun():
    print("---This is The Print Function---")
    print("Hello! Im Max Verstappen and im the print() function running")
    print("EXAMPLE")
    print("----> print() <----- = print('DU DU DU DU MAX VERSTAPPEN') = DU DU DU DU DU MAX VERSTAPPEN")

def choice(PrintRun,Printinfo):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INFO")
    print("2 --- RUN THE CODE ")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        Printinfo()
    
    elif tachyon == '2':
        PrintRun()
    
    else:
        ("invalid selection")
    input("Press any key to go back")

def input_info():
    print("INFORMATION ABOUT INPUT FUNCTION")
    print("The input() Function allows us to enter words and numbers")
    print("The input() function lets the user type values.")
    print("Example: name = input('Enter name: ')")
    print("")
def input_run():
    print("\n--- RUNNING INPUT FUNCTION EXAMPLE ---")
    name = input("Enter your name: ")
    print("Hello,", name)

def eval_info():
    print("\n--- INFORMATION ABOUT THE ---> eval(input()) ---")
    print("eval(input()) evaluates what the user types as Python code .")
    print("Useful for math expressions like: 5 * (3 + 2)")
    print(" WARNING: eval can run ANY code, so you might mistake it for int sometimes.")
    print("---------HOW IT WORKS---------")
    print("1.You give eval() a string that contains a valid Python expression (like a math problem or a list definition).")
    print("2.eval() reads that string as if you had typed the code directly into your program.")
    print("3.It figures out the answer or result of that code.")
    print("4.It gives the result back to you. ")

def eval_run():
    n1= eval(input("enter the first number:"))
    n2= eval (input("enter the second number:"))
    s = n1+n2
    d = n1-n2
    p = n1*n2
    q= n1/ n2
    print("\the sum of",n1, "and",n2,"is",s)
    print("the difference of",n1,"and",n2,"is",d)
    print("the product of",n1,"and",n2,"is",p)
    print("the quotient of",n1,"and",n2,"is",q)
    print(n1,"exponent by",n2, "is",n1**n2)
    print("the remainder of",n1,"and",n2,"is",n1 % n2)
    print("the floor division of",n1,"and",n2, "is",n1/n2)

def choice2(input_info,input_run,):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INPUT")
    print("2 --- RUN THE CODE ")
    print("3 --- EVAL + INPUT")
    print("4 --- INFORMATION ABOUT EVAL +INPUT")
    print("5 --- INT + EVAL")
    print("6 --- INFORMATION ABOUT INT +INPUT")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        input_info()
    
    elif tachyon == '2':
        input_run()
    
    else:
        ("invalid selection")
    input("Press any key to go back")

while True:
    os.system

    
    print("LEARN THE DIFFERENT FUNCTIONS")
    print("++++++++++++++++++++++++++++++\n")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION")
    print("C - IF, ELSE FUNCTION")
    print("D - LOOP FUNCTION")
    print("E - EXIT SYSTEM")

    hutao = input("ENTER YOUR CHOICE TRAVELER:").lower().strip()

    if hutao == 'a':
        choice(Printinfo,PrintRun,)
        continue
    elif hutao =='b':
        choice2(input_info,input_run)
        continue


    else:
        ("what are you doing???")
