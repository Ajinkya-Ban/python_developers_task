'''
Student Managament System
Operations
------------------
1. Add Student --> Field --> id, name, mobile, marks, city
2. Display all student
3. Search Student
4. Update marks 
5. Delete Student by using id
6. Exit
Complete the project with validations
'''
from colorama import Fore,Back,Style,init
init()

#emplty list
stud = []
while True:
    print("---------------Student Managament System App---------------")
    print("-" * 80)
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student By using ID")
    print("4. Update the Marks By using ID")
    print("5. Delete the Student By using ID")
    print("6. Exit")
    print("-" * 80)
    choice = input("Enter the choice = ").strip()
    if choice == "":
        print(Fore.RED + "Please enter the choice"+Style.RESET_ALL)
    elif not choice.isdigit():
        print(Fore.RED + "Only digit allowed"+Style.RESET_ALL)
   
    else:
     choice = int(choice)
     match choice:
            case 1:
                id = input("Enter the student id = ").strip()
                if id == "":
                    print("Please enter student id")
                    continue
                if not id.isdigit():
                    print("Only digit allowed")
                    continue
                # check id already exist
                found = False
                for s in stud:
                    if s[0] == id:
                        found = True
                        break
                if found:
                    print(f"{id} already exist")
                id = int(id)

                name = input("Enter the name of student =").strip().title()
                if name == "":
                    print("Please enter the name")
                    continue
                if not name.replace(" ","").isalpha():
                    print("Only Character allowed")
                    continue
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Thanks for using our App. Visit again")
                break
            case _:
                print("Invalid choce")



