def Update_student(students_list):
    if not students_list:
        print('The student list is empty.')
        return

    print('\n--- Current list of students ---')
    for index, student in enumerate(students_list):
        print(f"{index + 1}. {student['name']} - Age: {student['years']} - Course: {student['Course_program']} - State: {student['state']}")

    try:
        student_id = int(input('\nEnter the ID (number) of the student to update: ')) - 1
        
        if 0 <= student_id < len(students_list):
            student = students_list[student_id]
            
            print(f"Updating data for: {student['name']}")
            
            student['years'] = int(input(f"New age (current: {student['years']}): "))
            student['Course_program'] = input(f"New course (current: {student['Course_program']}): ")
            student['state'] = input(f"New state (current: {student['state']}): ")
            
            print(f"\nStudent {student['name']} updated successfully!!")
        else:
            print("Error: That ID does not exist in the list.")
            
    except ValueError:
        print('Error: Please enter a valid NUMBER for the ID and Age.')

