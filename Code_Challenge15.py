import os

os.system('cls')
print('DLL STUDENT INFORMATION SYSTEM')
print('+++++++++++++++++')
stud_record ={}
while True:
    print("select from the following options")
    print("A - Adding The Student Record")
    print("B - Search Student Record")
    print("C - Edit Student Record")
    print("D - Delete Student Record")
    print("E - Print All Record")
    print("F - Export Data")
    print("G - Exit System")

    choice = input("Input your choice --->").lower().strip()

    if choice == 'a':
        print("add student record")

        student_id = input("student id number ")
        first_name = input("input student first name").upper
        last_name = input("input student last name").upper
        course = input("input student course").upper
        section = input("input student section").upper
        email = input ("input email").upper

        stud_record[student_id] = [first_name,last_name,course,section,email]
        print("Data saved succesfully")
        os.system('cls')
        continue
    elif choice == 'b':
        pass
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        pass
        continue
    else:
        print("Invalid Choice, Re-enter code")
        continue
