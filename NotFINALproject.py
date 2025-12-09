import os




def Printinfo():
    os.system('cls')
    print("n\The Print Allows us to show things on screen Whether it be a Variable or Function")
    print("n\----> print() <----- = print('DU DU DU DU MAX VERSTAPPEN') =")
    print("\n--- INFORMATION ABOUT PRINT FUNCTION ---")
    print("The print() function displays text on the screen.")
    print("Example: print('Hello')")
    input("Press any key to go back")

    
def PrintRun():
    os.system('cls')
    print("---This is The Print Function---")
    print("Hello! Im Max Verstappen and im the print() function running")
    print("EXAMPLE")
    print("----> print() <----- = print('DU DU DU DU MAX VERSTAPPEN') = DU DU DU DU DU MAX VERSTAPPEN")
    input("Press any key to go back")

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
    

def input_info():
    os.system('cls')
    print("INFORMATION ABOUT INPUT FUNCTION")
    print("The input() Function allows us to enter words and numbers")
    print("The input() function lets the user type values.")
    print("Example: name = input('Enter name: ')")
    print("Code in the 2nd Option")

    print("\n--- RUNNING INPUT FUNCTION EXAMPLE ---")
    print("name = input(Enter your name: ")
    print("Hello,, name")
    input("Press any key to go back")

def input_run():
    os.system('cls')
    print("\n--- RUNNING INPUT FUNCTION EXAMPLE ---")
    name = input("Enter your name: ")
    print("Hello,", name)

def choice2(input_info,input_run):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INPUT")
    print("2 --- RUN THE CODE ")
   
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        input_info()
    
    elif tachyon == '2':
        input_run()

    
    
        
    
    
    else:
        ("invalid selection")
    

def eval_info():
    os.system('cls')
    print("\n--- INFORMATION ABOUT THE ---> eval(input()) ---")
    print("eval(input()) evaluates what the user types as Python code .")
    print("Useful for math expressions like: 5 * (3 + 2)")
    print(" WARNING: eval can run ANY code, so you might mistake it for int sometimes.")
    print("---------HOW IT WORKS---------")
    print("1.You give eval() a string that contains a valid Python expression (like a math problem or a list definition).")
    print("2.eval() reads that string as if you had typed the code directly into your program.")
    print("3.It figures out the answer or result of that code.")
    print("4.It gives the result back to you. ")

    print("Code in the 2nd option")

    print("n1= eval(input(enter the first number:")
    print("n2= eval (input(enter the second number:")
    print("s = n1+n2")
    print("d = n1-n2")
    print("p = n1*n2")
    print("q= n1/ n2")
    print("\the sum of ,n1, and ,n2,is,s")
    print("the difference of, n1,and, n2,is, d")
    print("the product of, n1,and,n2,is,p")
    print("the quotient of, n1, and n2 is,q")
    print("n1,exponent by,n2, is,n1**n2")
    print("the remainder of,n1,and,n2,is,n1 % n2")
    print("the floor division of,n1,and,n2, is,n1/n2")
    input("Press any key to go back")

def eval_run():
    os.system('cls')
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
    input("Press any key to go back")

def choice3(eval_run,eval_info):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INPUT")
    print("2 --- RUN THE CODE ")
   
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        eval_info()
    
    elif tachyon == '2':
        eval_run()

def int_run():
    os.system('cls')
    print("\n --- INT+INPUT EXAMPLE RUN ---")

    n1 =int(input("Enter first whole number:"))
    n2 = int(input("Enter second whole number"))

    print("\n --- Results ---")
    print("Addition:",n1 + n2)
    print("Subtraction:",n1-n2)
    print("Multiplication:",n1*n2)
    print("Division:",n1/n2)
    input("Press any key to go back")

def int_info():
    os.system('cls')
    print("\n--- INFORMATION ABOUT THE ---> int(input()) ---")
    print("The int() function converts user input into a whole number (integer).")
    print("Example: age = int(input('Enter age:))")
    print("If you type the letters, the program will show an error")
    print("An int function in programming is essentially a mini-program (or sub-program) designed specifically \nto calculate and provide back a single, whole number (integer)")
    
    print("\n THE CODE IN THE 2ND OPTION")

    print("n1 =int(input(Enter first whole number:")
    print("n2 = int(input(Enter second whole number")

    print("\n --- Results ---")
    print("Addition:,n1 + n2")
    print("Subtraction:,n1-n2")
    print("Multiplication:n1*n2")
    print("Division:,n1/n2")
    input("Press any key to go back")
def choice4(int_info,int_run):

    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INPUT")
    print("2 --- RUN THE CODE ")
   
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        int_info()
    
    elif tachyon == '2':
        int_run()

    
    
        
    
    
    else:
        ("invalid selection")
    
def if_info():
    os.system('cls')
    print("\n--- INFORMATION ABOUT IF / ELIF / ELSE ---")
    print("This function basically allows you to let your program choose.")
    print("IF = checks a condition.")
    print("ELIF = checks another condition if the first is false.")
    print("ELSE = runs when all conditions are false.")
    print("\nExample:")
    print("\n---Code in the 2nd Option ---")
    print("age = int(input(Enter your age: ")

    print("if age < 13:")
    print("print(You are a child.")
    print("elif age < 20:")
    print("    print(You are a teenager.")
    print("else:")
    print("  print(You are an adult.")
    input("Press any key to go back")
    
def if_run():
    print("\n--- RUNNING IF/ELIF/ELSE EXAMPLE ---")
    age = int(input("Enter your age: "))

    if age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")
    input("Press any key to go back")
    

def choice5(if_run,if_info):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INPUT")
    print("2 --- RUN THE CODE ")
   
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        if_info()
    
    elif tachyon == '2':
        if_run()
    
    else:
        ("invalid choice")
       

def loop_info():
    os.system('cls')
    print("\n--- INFORMATION ABOUT LOOPS ---")
    print("Loops repeat actions many times automatically")
    print("A for loop in Python iterates over the items of any sequence, such as a list, tuple, \nor the sequence of numbers produced by range(). The range() function generates these numbers on the fly, " \
    "which is memory efficient, especially for large sequences. ")
    print("\nFor loop repeats a fixed number of times")
    print("Example: for i in range(5): print(i)")
    print("\nCODE IN THE 2ND OPTION")
    print("for code in range(11,0,-1):")
    print("print(code)")
    print("Result")
    print("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11")
    input("Press any key to go back")
    print("for code in range(...):")
    print("This loop picks each number from the range one by one and assigns it to the variable code")

    print("print(code)")
    print("Prints the current number")
    input("Press any key to go back")
def loop_run():
    for code in range(11,0,-1):
     print(code)

     
     

def choice6(loop_run,loop_info):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INFO")
    print("2 --- RUN THE CODE ")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        loop_info()
    
    elif tachyon == '2':
        loop_run()
    
    else:
        ("invalid selection")
    
def listinfo():
    print("The List Function allows us to store items in a single variable")
    print("\n--->list()<--- is used to create a list")
    print("---INFO ABOUT THIS FUNCTION---")
    print("A list is basically a ordered collection of elements that can be any data type.\nNumbers,Strings,Booleans and even other lists")
    print("Example: months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']")
    print("\nWe can use various list methods such as:")
    print("listreverse() to reverse the order of items.")
    print(" sort() to sort the list in ascending order.")
    print("Example:")
    print("months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']")
    print("months.reverse() * Reverses the list.")
    print("months.sort() * Sorts the list alphabetically.")
    input("\nPress any key to go back")

def listrun():
     months=['jan','feb','mar','apr','may','jun','jul']

     print(months)

     months.reverse()
     print(months)

     input("\nPress any key to go back")
    




def choice7(listrun,listinfo):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INFO")
    print("2 --- RUN THE CODE ")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        listinfo()
    
    elif tachyon == '2':
        listrun()
    
    else:
        ("invalid selection")
    
while True:
    os.system

    
    print("LEARN THE DIFFERENT FUNCTIONS")
    print("++++++++++++++++++++++++++++++\n")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION") 
    print("C - EVAL FUNCTION")
    print("D - INT FUNCTION")
    print("E - IF ELSE ELIF FUNCTION")
    print("F - LOOP FUNCTION")
    print("F - LIST FUNCTION")
    print("G - EXIT SYSTEM")

    hutao = input("ENTER YOUR CHOICE TRAVELER:").lower().strip()

    if hutao == 'a':
        choice(Printinfo,PrintRun,)
        continue
    elif hutao =='b':
        choice2(input_info,input_run,)
        continue
    
    elif hutao == 'c': 
        choice3(eval_run,eval_info)
        continue

    elif hutao =='d':
        choice4(int_info,int_run)
        continue

    elif hutao =='e':
        choice5(if_run,if_info)
        continue

    elif hutao =='f':
        choice6(loop_run,loop_info)
        continue
    
    elif hutao =='g':
        choice7(listrun,listinfo)
        continue

    else:
        ("what are you doing???")
