from Register_student import *

def List_student(sheck):
    if not sheck:
        print('The student list is empty.')
    else:
        print('='*50)
        print('List empty !!')
        print('='*50) 
        for list in sheck:
            print(f"ID: {list['ID']}")
            print(f"name: {list['name']}")
            print(f"year: {list['years']}")
            print(f"Course_program: {list['Course_program']}")
            print(f"state: {list['state']}")
            print("-" * 20)