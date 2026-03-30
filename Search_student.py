from Check_student import *

def search(search_student):
    if not search_student:
        print('the student is not found')
        return
    search_id = input('Search student by resgister: ').strip().lower()
    found_register = [student for student in search_student if student['name'].lower()== search_id]

    if found_register:
        print(f'\n Found {len(found_register)} student(s) matching : ')
        for student in found_register:
            print(f'ID {student['ID']}')
            print(f' name {student['name']}')
            print(f'years {student['years']}')
            print(f'Course_program {student['Course_program']}')
            print(f'state {student['state']}')
            print('='*50)