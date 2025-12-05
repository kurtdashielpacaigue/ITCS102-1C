import os
import random
from activity23_1 import GreetWithName, FunctionWithReturn, Greetperson, Factorial


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
    

    print("\n THE CODE IN THE 2ND OPTION")

    print("if age < 13:")
    print("print(You are a child.")
    print("elif age < 20:")
    print("    print(You are a teenager.")
    print("else:")
    print("  print(You are an adult.")
    input("Press any key to go back")
    
def if_run():
    os.system('cls')
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
    os.system('cls')
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
    
    print("\n THE CODE IN THE 2ND OPTION")


    print(" months=['jan','feb','mar','apr','may','jun','jul']")

    print(" print(months)")

    print("  months.reverse()")
    print("  print(months)")
    input("\nPress any key to go back")

def listrun():
    os.system('cls')
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

def whileinfo():
    os.system('cls')
    print("\n--- INFORMATION ABOUT WHILE TRUE LOOP---")
    print("A while True loop runs forever until something stops it")
    print("This is usually the Break statement which stops it")
    print("A while True loop is a coding instruction that essentially means: Keep doing this set of actions forever, unless I explicitly tell you to stop. ")
    print("Basically,Because the loop runs indefinitely, you must use a break statement inside \nan if condition to stop it when a certain event happens. ")
    

    print("Example:")
    print("while True:")
    print("    user = input('Enter something: ')")
    print("    if user == 'stop':")
    print("        break")
    print("\nIn your code:")
    print("- 'while c == True:' keeps looping until the player guesses the number.")
    print("- If the guess is correct, 'break' stops the loop.")
    print("- The loop counts how many tries the player used.\n")

    print("\n THE CODE IN THE 2ND OPTION")
    print("TRY YOUR LUCK")
    print("________________")

    print("a = random.randint(1, 10)")
    print("b = 0")
    print("c = True")

    print("e = input(Enter Your Name--> )")

    print("while c == True:")
    print("    d = eval(input(Enter a number 1–10 ---> )")
    print("    b += 1")
    print("    if d == a:")
    print("       print(Winner)")
    print("       break")
    print("    else:")
    print("          print(Choose Again)")

    print("    print(fHi {e}, Your Tries is {b})")


    input("Press any key to go back...")

def whilerun():
    os.system('cls')
    print("\n--- RUNNING WHILE TRUE FUNCTION CODE ---\n")

    print("TRY YOUR LUCK")
    print("________________")

    a = random.randint(1, 10)
    b = 0
    c = True

    e = input("Enter Your Name--> ")

    while c == True:
        d = eval(input("Enter a number 1–10 ---> "))
        b += 1
        if d == a:
            print("Winner")
            break
        else:
            print("Choose Again")

    print(f"Hi {e}, Your Tries is {b}")

    input("\nPress any key to go back...")

def choice8(whileinfo,whilerun):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INFO")
    print("2 --- RUN THE CODE ")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        whileinfo()
    
    elif tachyon == '2':
        whilerun()
    
    else:
        ("invalid selection")

def dictionaryinfo():
    os.system('cls')
    print("\n--- INFORMATION ABOUT DICTIONARIES ---")
    print("\n--- INFORMATION ABOUT DICTIONARIES ---\n")
    print("A dictionary in python is a collection of data stored in KEY : VALUE pairs.")
    print("Unlike lists, dictionaries are unordered and you access items using keys instead of indices.")
    print("\nKey Points:")
    print("1. Dictionaries use curly braces {} to store items.")
    print("2. Each item is a pair: key : value.")
    print("3. Keys must be unique, but values can repeat.")
    print("4. You can change, add, or remove items in a dictionary.")
    print("5. Access values by using their key, not by position.")
    print(" a dictionary is a simple, efficient way to store information in key-value pairs.\n Think of it like a real-world dictionary: you look up a word\n (the key) to get its definition (the value). ")

    print("\n--- RUNNING CODE EXAMPLE FOR DICTIONARY ---\n")

    
    print("    TheList = ['RB', 'NM', 'DREAM', 'SOLAR', 'CIRCLES', 'BB', 'DONE']")
    print("    print(Example List:, TheList)")
    print("    print(Accessing the 6th item in the list (index 5):, TheList[5]) ")

    
    print("    TheD = {")
    print("        'SOLAR' : 'SOL',")
    print("        'DEFEATED' : 'CIRLCES',")
    print("        'RGB' : 'RB',")
    print("        'DR' : 'DREAM',")
    print("        'NM' : 'NIGHTMARE'")
    print("    }")
    print("    print(\nDictionary Example:, TheD)")
    print("    print(Accessing the value of 'SOLAR':, TheD['SOLAR'])")


    print("\nOther useful dictionary operations:")
    print("- Add new item: TheD['NEWKEY'] = 'NewValue'")
    print("- Change value: TheD['SOLAR'] = 'NEWVAL'")
    print("- Remove item: del TheD['DEFEATED']")
    print("- Check if key exists: 'SOLAR' in TheD  # returns True or False\n")
    input("\nPress any key to go back...")

def dictionaryrun():
    os.system('cls')
    print("\n--- RUNNING CODE EXAMPLE FOR DICTIONARY ---\n")

 
    TheList = ['RB', 'NM', 'DREAM', 'SOLAR', 'CIRCLES', 'BB', 'DONE']
    print("Example List:", TheList)
    print("Accessing the 6th item in the list (index 5):", TheList[5]) 

    
    TheD = {
        'SOLAR' : 'SOL',
        'DEFEATED' : 'CIRLCES',
        'RGB' : 'RB',
        'DR' : 'DREAM',
        'NM' : 'NIGHTMARE'
    }
    print("\nDictionary Example:", TheD)
    print("Accessing the value of 'SOLAR':", TheD['SOLAR'])  

    input("\nPress any key to go back...")

def choice9(dictionaryinfo,dictiornaryrun):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INFO")
    print("2 --- RUN THE CODE ")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        dictionaryinfo()
    
    elif tachyon == '2':
        dictiornaryrun()
    
    else:
        ("invalid selection")    

def functionrun():
    os.system('cls')
    print("\n--- RUNNING FUNCTION EXAMPLES ---\n")

    
    def Function():
        print("umamusume")
        print("agnes tachyon")
        print("4 time world champion")

    Function()  

    
    GreetWithName('lerbon')
    Greetperson('agnes', 'kyoto', '67')

    print(f"\nI want to get the summation of {FunctionWithReturn(9)}")
    print(f"I want to get the summation of {FunctionWithReturn(11) + 25}")
    print(f"I want to get the summation of {Factorial(6)}")

    input("\nPress any key to go back...")

def functioninfo():
    os.system('cls')
    print("\n--- INFORMATION ABOUT FUNCTIONS IN PYTHON ---\n")
    print("In Python, functions are defined using the 'def' keyword.")
    print("Functions allow you to group code together and reuse it multiple times.\n")

    print("Key points about functions:")
    print("1. Use 'def function_name(parameters):' to define a function.")
    print("2. Functions can take inputs (parameters) and optionally return a value.")
    print("3. Call a function using its name and parentheses: function_name(args)")
    print("4. Using functions helps organize code and avoid repetition.\n")
    
    print("So Basically a function is a named reusable block of code that only runs when it is called. Think of it as a small, specialized machine: \nyou give it an input (parameters), \nit does a specific task (the code inside), and it gives you an output (a return value). ")


    print("Example from my code:")
    print("def Function():")
    print("    print('umamusume')")
    print("    print('agnes tachyon')")
    print("    print('4 time world champion')")
    print("Function()  # calls the function\n")

    print("Other examples in my code:")
    print("- GreetWithName('lerbon')  * calls function with one parameter")
    print("- FunctionWithReturn(9)  * returns a value")
    print("- Factorial(6)  * returns factorial of 6\n")

    input("Press any key to go back...")

def choice10(functioninfo,functionrun):
    os.system('cls')
    print("What do you wanna know")
    print("1 --- INFORMATION ABOUT INFO")
    print("2 --- RUN THE CODE ")
    tachyon =input("Enter Your Choice")

    if tachyon == '1':
        functioninfo()
    
    elif tachyon == '2':
        functionrun()
    
    else:
        ("invalid selection")  
   
while True:
    os.system('cls')

    
    print("LEARN THE DIFFERENT FUNCTIONS")
    print("++++++++++++++++++++++++++++++\n")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION") 
    print("C - EVAL FUNCTION")
    print("D - INT FUNCTION")
    print("E - IF ELSE ELIF FUNCTION")
    print("F - LOOP FUNCTION")
    print("G - LIST FUNCTION")
    print("H - WHILE TRUE FUNCTION")
    print("I - DICTIONARY FUNCTION")
    print("J - DEF - FUNCTION")
    print("K - EXIT SYSTEM")

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

    elif hutao =='h':
        choice8(whileinfo,whilerun)
        continue

    elif hutao =='i':
        choice9(dictionaryinfo,dictionaryrun)
        continue
    
    elif hutao =='j':
        choice10(functionrun,functioninfo)
        continue
    
    elif choice == 'h':
        print("System Exit")
        break
    else:
        ("what are you doing ??? Try again son")
        continue
        
