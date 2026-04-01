def Add_student(register):
    Add = 'yes'
    while Add == 'yes':
        id = len(register) + 1
        Name = str(input('Name the student: '))
        if Name.isnumeric():
            print('name invalid')
            continue
        Years = int(input('Years the student: '))
        Course_program = str(input('Which course or program?: '))
        if Course_program.isnumeric():
            print('Course_program inavlid')
            continue
        State = input('Assed / deactivated: ')
        # Create new dictionary the student
        add = { 'ID': id, 'name': Name, 'years': Years, 'Course_program': Course_program, 'state': State}
        register.append(add)
        print(f'{Name} add register exit !!')
        Add = input(' wishes add stdent: (yes/no)').lower()
