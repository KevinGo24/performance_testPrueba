def Delete_student(students_list):
    if not students_list:
        print('The student list is empty.')
        return

    
    print("\n--- Current List ---")
    for i, student in enumerate(students_list):
        print(f"{i + 1}. {student['name']}")

    try:
        
        student_id = int(input('\nEnter the ID (number) of the student to delete: ')) - 1
        
        
        if 0 <= student_id < len(students_list):
            
            removed_student = students_list.pop(student_id)
            print(f"Student '{removed_student['name']}' successfully deleted.")
        else:
            print("Error: That ID number does not exist.")
            
    except ValueError:
        print('Error: Please enter a valid NUMBER, not text.')
