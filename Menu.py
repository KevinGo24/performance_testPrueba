#---- import --- #
from Register_student import Add_student
from Check_student import List_student
from Search_student import search
from Uptade_student import  Update_student
from Delete_student import Delete_student
#----  --- #
Student = []
institution = 'yes'
def Menu():
    global institution
    while institution == 'yes':
        print('='*72)
        print('='*10, 'institution educational', '='*10)
        print('='*72)
        print('1 - Register new students ')
        print('2 - Check the student list.')
        print('3 - Search for student')
        print('4 - Update student information')
        print('5 - Delete student')
        print('6 - Exit')
        print('='*72)   
        Users = int(input('Which option do you wish to choose?'))
        if Users == 1:
            Add_student(Student)
        elif Users == 2:
            List_student(Student)
        elif Users == 3:
            search(Student)
        elif Users == 4:
            Update_student(Student)
        elif Users == 5:
            Delete_student(Student)
        elif Users == 6:
            institution = 'no'
            print("Exit System...")
            break
    else:
        print("Option no valid.")
    if Users < 1 or Users > 6:
        print("Option no valid. please, selecction one optión the 1 al 6.")
