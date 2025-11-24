import os
import json
os.system('cls')
print('DLL STUDENT INFORMATION SYSTEM')
print('+++++++++++++++++')
stud_record ={}
while True:
    print("select from the following options")
    print("A - Adding The Student Record")
    print("B - Print All Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit All Record")
    print("F - Export Data")
    print("G - IMPORT DATA")
    print("H - EXIT SYSTEM")

    choice = input("Input your choice --->").lower().strip()

    if choice == 'a':
        print("add student record")

        student_id = input("student id number ")
        first_name = input("input student first name").upper()
        last_name = input("input student last name").upper()
        course = input("input student course").upper()
        section = input("input student section").upper()
        email = input ("input email").upper()

        stud_record[student_id] = [first_name,last_name,course,section,email]
        print("Data saved succesfully")
        os.system('cls')
        continue
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORDS")
        print("================================")

        for id,info in stud_record.items():
            print(f"STUDENT{id} = RECORD = {info}")
        continue
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        search_id = input("INPUT STUDENT ---->").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND{search_id}")
                print("==========")
                for id in stud_record[search_id]:
                    print(f"---{id}")
                print("=================")

            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETE RECORD")

        search_id = input("INPUT STUDENT ---->").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND{search_id}")
                print("==========")
                for id in stud_record[search_id]:
                    print(f"---{id}")
                print("=================")

                stud_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        search_id = input("INPUT STUDENT ---->").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND{search_id}")
                print("==========")
                for id in stud_record[search_id]:
                    print(f"---{id}")
                print("=================")
                first_name = input("input student first name").upper()
                last_name = input("input student last name").upper()
                course = input("input student course").upper()
                section = input("input student section").upper()
                email = input ("input email").upper()

                stud_record[search_id][0]= first_name
                stud_record[search_id][1]= last_name
                stud_record[search_id][2]= course
                stud_record[search_id][3]= section
                stud_record[search_id][4]= email
                ("Data Printed Succefully")


            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'f':
        print("EXPORT DATA")
        with open('student_record.json','w') as new_file:
            json.dump(stud_record,new_file,indent=4)

        print("DATA EXPORTED SUCCESFULY")
        continue

    elif choice == 'g':
        print("EXPORT DATA")
        with open('student_record.json','r') as new_file:
            imported_student = json.load(new_file)

        stud_record = imported_student

        print("DATA IMPORTED SUCCESFULY")
        continue


    elif choice == 'h':
        print("System Exit")
        continue
    else:
        print("Invalid Choice, Re-enter code")
        continue
